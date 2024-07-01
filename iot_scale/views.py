import paho.mqtt.client as mqtt
from django.db.models.signals import post_save
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.dispatch import receiver
from rest_framework import status
from datetime import datetime, time
from threading import Timer, Thread
from .models import RelaySchedule
import time as time_lib
from sineas_project.settings import MQTT_server, MQTT_port, MQTT_user, MQTT_password
import pytz

# Configurar las credenciales MQTT
MQTT_SERVER = MQTT_server
MQTT_PORT = MQTT_port
MQTT_USER = MQTT_user
MQTT_PASSWORD = MQTT_password

# Inicializar el cliente MQTT
mqtt_client = mqtt.Client("DjangoClient")
mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

last_state = None


def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT con código de resultado " + str(rc))
    # Enviar el último estado almacenado
    if last_state:
        mqtt_client.publish('relay/control', last_state)
        print(f"Último estado enviado al reconectar: {last_state}")


def on_disconnect(client, userdata, rc):
    print("Desconectado del broker MQTT con código de resultado " + str(rc))


mqtt_client.on_connect = on_connect
mqtt_client.on_disconnect = on_disconnect


def mqtt_connect():
    mqtt_client.connect(MQTT_SERVER, MQTT_PORT, 60)
    mqtt_client.loop_start()


def monitor_connection():
    global last_state
    while True:
        # Obtener el último estado guardado si no está en memoria
        if last_state is None:
            last_state_instance = RelaySchedule.objects.filter(last_state__isnull=False).last()
            if last_state_instance:
                last_state = last_state_instance.last_state

        if mqtt_client.is_connected() and last_state:
            mqtt_client.publish('relay/control', last_state)
            print(f"Último estado enviado: {last_state}")
            # Esperar un tiempo mínimo antes de volver a enviar para evitar flooding
            time_lib.sleep(1)  # Verificar cada segundo


Thread(target=monitor_connection, daemon=True).start()

mqtt_connect()


def schedule_relay_action(message, target_time, timezone):
    now = datetime.now(pytz.utc)
    today = now.date()
    target_datetime = datetime.combine(today, target_time)

    tz = pytz.timezone(timezone)
    target_datetime_local = tz.localize(target_datetime)
    target_datetime_utc = target_datetime_local.astimezone(pytz.utc)

    delay = (target_datetime_utc - now).total_seconds()

    if delay < 0:
        return {'error': 'La hora especificada ya pasó.'}

    def execute_action():
        global last_state
        if message == 'on':
            mqtt_client.publish('relay/control', 'on')
        elif message == 'off':
            mqtt_client.publish('relay/control', 'off')

        RelaySchedule.objects.update(last_state=message)
        last_state = message

    Timer(delay, execute_action).start()

    return {'status': f'Relé programado para {message} a las {target_datetime_utc.strftime("%H:%M %Z")}.'}


@api_view(['POST'])
def control_relay(request):
    message = request.data.get('message')
    hour_str = request.data.get('hora')
    timezone = request.data.get('timezone')

    if not message or not hour_str or not timezone:
        return Response({'error': 'Mensaje, hora y zona horaria son requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        target_time = datetime.strptime(hour_str, "%H:%M").time()
    except ValueError:
        return Response({'error': 'Formato de hora inválido. Use HH:MM.'}, status=status.HTTP_400_BAD_REQUEST)

    result = schedule_relay_action(message, target_time, timezone)

    return Response(result, status=status.HTTP_200_OK)


@receiver(post_save, sender=RelaySchedule)
def ejecutar_control_rele(sender, instance, created, **kwargs):
    if created:
        message = instance.message
        target_time = instance.time
        timezone = instance.timezone

        result = schedule_relay_action(message, target_time, timezone)
        print(f"Ejecutando acción de relé basada en programación creada: {result}")
        instance.last_state = message  # Guardar el último estado en el modelo
        instance.save()

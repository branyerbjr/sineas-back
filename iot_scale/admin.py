from django.contrib import admin
from .models import RelaySchedule


@admin.register(RelaySchedule)
class RelayScheduleAdmin(admin.ModelAdmin):
    list_display = ('message', 'time', 'timezone', 'hogar', 'dispositivo')
    list_filter = ('timezone', 'hogar', 'dispositivo')

# Generated by Django 5.0.6 on 2024-06-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hogar',
            name='timezone',
            field=models.CharField(default='UTC', max_length=100),
        ),
    ]

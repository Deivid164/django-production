# Generated by Django 5.0.6 on 2024-11-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_tareas_rotulo_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tareas',
            name='rotulo_fecha',
        ),
        migrations.AddField(
            model_name='tareas',
            name='rotulo_fecha_fecha1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tareas',
            name='rotulo_fecha_fecha2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
# Generated by Django 5.0.6 on 2024-11-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_remove_tareas_rotulo_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='rotulo_fecha_fecha1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='rotulo_fecha_fecha2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

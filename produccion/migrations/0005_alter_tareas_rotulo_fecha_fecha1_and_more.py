# Generated by Django 5.0.6 on 2024-11-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0004_alter_tareas_rotulo_fecha_fecha1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='rotulo_fecha_fecha1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='rotulo 1 fecha'),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='rotulo_fecha_fecha2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='rotulo 2 fecha'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-11-05 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField(verbose_name='hora de inicio')),
                ('linea', models.CharField(max_length=255)),
                ('producto', models.CharField(max_length=255)),
                ('trabajadores', models.CharField(max_length=100, verbose_name='trabajador')),
                ('producto_terminado', models.CharField(max_length=255, verbose_name='producto terminado')),
                ('und_producidas', models.IntegerField(verbose_name='unidades producidas')),
                ('hora_termino', models.TimeField(verbose_name='hora de termino')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de productos')),
            ],
        ),
    ]

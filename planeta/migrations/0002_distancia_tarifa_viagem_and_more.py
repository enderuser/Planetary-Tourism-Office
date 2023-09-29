# Generated by Django 4.2.5 on 2023-09-29 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planeta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distancia_km', models.FloatField()),
                ('planeta_destino', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='distancias_destino', to='planeta.planeta')),
                ('planeta_origem', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='distancias_partida', to='planeta.planeta')),
            ],
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tarifa_de_destino', to='planeta.planeta')),
                ('origem', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tarifa_de_origem', to='planeta.planeta')),
            ],
        ),
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='viagens_de_destino', to='planeta.planeta')),
                ('distancia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='planeta.distancia')),
                ('origem', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='viagens_de_origem', to='planeta.planeta')),
                ('tarifa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='planeta.tarifa')),
            ],
        ),
        migrations.DeleteModel(
            name='DistanciaEntrePlanetas',
        ),
    ]
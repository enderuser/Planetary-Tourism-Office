from django.db import models
from datetime import datetime

class Planet(models.Model):
    name = models.CharField(max_length=100)
    diametro_km = models.FloatField()
    massa_kg = models.CharField(max_length=50)
    distancia_media_ao_sol_km = models.CharField(max_length=50)
    periodo_orbital_dias = models.CharField(max_length=50)
    temperatura_media_celsius = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.name
    
class DistanciaEntrePlanetas(models.Model):
    planeta_origem = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='distancias_partida')
    planeta_destino = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='distancias_destino')
    distancia_km = models.FloatField()
    tarifa = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Distância entre {self.planeta_origem.name} e {self.planeta_destino.name}'
    
class Travel(models.Model):
    departure = models.ForeignKey(Planet, on_delete=models.DO_NOTHING, related_name='trips_of_departure')
    arriving = models.ForeignKey(Planet, on_delete=models.DO_NOTHING, related_name='trips_of_arriving')
    data = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'Travel departure {self.departure} for {self.arriving} a {self.data} the {self.time}'

def search_travel(departure, arriving, data):
    data_formatada = datetime.strptime(data, '%Y-%m-%d').date()
    trips = Travel.objects.filter(departure=departure, arriving=arriving, data=data_formatada)
    return trips
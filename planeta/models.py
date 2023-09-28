from django.db import models

class Planeta(models.Model):
    nome = models.CharField(max_length=100)
    diametro_km = models.FloatField()
    massa_kg = models.FloatField()
    distancia_media_ao_sol_km = models.FloatField()
    periodo_orbital_dias = models.FloatField()
    temperatura_media_celsius = models.FloatField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class DistanciaEntrePlanetas(models.Model):
    planeta_origem = models.ForeignKey(Planeta, on_delete=models.CASCADE, related_name='distancias_partida')
    planeta_destino = models.ForeignKey(Planeta, on_delete=models.CASCADE, related_name='distancias_destino')
    distancia_km = models.FloatField()

    def __str__(self):
        return f'Distância entre {self.planeta_origem.nome} e {self.planeta_destino.nome}'
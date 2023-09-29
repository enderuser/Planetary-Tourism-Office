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
    
class Distancia(models.Model):
    planeta_origem = models.ForeignKey(Planeta, on_delete=models.DO_NOTHING, related_name='distancias_partida')
    planeta_destino = models.ForeignKey(Planeta, on_delete=models.DO_NOTHING, related_name='distancias_destino')
    distancia_km = models.FloatField()

    def __str__(self):
        return f'Distância entre {self.planeta_origem.nome} e {self.planeta_destino.nome}'
    
class Tarifa(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    origem = models.ForeignKey(Planeta, on_delete=models.DO_NOTHING, related_name='tarifa_de_origem')
    destino = models.ForeignKey(Planeta, on_delete=models.DO_NOTHING, related_name='tarifa_de_destino')

    def __str__(self):
        return f'Valor de {self.origem.nome} para {self.destino.nome}: R$ {self.valor}'

class Viagem(models.Model):
    origem = models.ForeignKey(Planeta, on_delete=models.DO_NOTHING, related_name='viagens_de_origem')
    destino = models.ForeignKey(Planeta, on_delete=models.DO_NOTHING, related_name='viagens_de_destino')
    data = models.DateField()
    horario = models.TimeField()
    tarifa = models.ForeignKey(Tarifa, on_delete=models.DO_NOTHING)
    distancia = models.ForeignKey(Distancia, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Viagem de {self.origem.nome} para {self.destino.nome} em {self.data} às {self.horario}'

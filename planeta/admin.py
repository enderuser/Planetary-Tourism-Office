from django.contrib import admin
from .models import Planeta

# Register your models here.
class PlanetaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'diametro_km', 'massa_kg', 'distancia_media_ao_sol_km', 'periodo_orbital_dias', 'temperatura_media_celsius')
    list_filter = ('nome',)  # Adicione outros campos se desejar filtrar por eles
    search_fields = ('nome',)

admin.site.register(Planeta, PlanetaAdmin)


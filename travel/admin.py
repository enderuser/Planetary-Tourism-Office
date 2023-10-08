from django.contrib import admin
from .models import Planet, DistanciaEntrePlanetas, Travel

class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'diametro_km', 'massa_kg', 'distancia_media_ao_sol_km', 'periodo_orbital_dias', 'temperatura_media_celsius')
    list_filter = ('name',)  # Adicione outros campos se desejar filtrar por eles
    search_fields = ('name',)

admin.site.register(Planet, PlanetAdmin)

class DistanceAdmin(admin.ModelAdmin):
    list_display = ('planeta_origem', 'planeta_destino', 'distancia_km')
    list_filter = ('planeta_origem',) 
    search_fields = ('planeta_origem',)

admin.site.register(DistanciaEntrePlanetas, DistanceAdmin)

class TravelAdmin(admin.ModelAdmin):
    list_display = ('departure', 'arriving', 'data', 'time')
    list_filter = ('departure',)
    search_fields = ('departure',)

admin.site.register(Travel, TravelAdmin)

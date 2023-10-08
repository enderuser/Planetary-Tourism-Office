from django.urls import path
from . import views

urlpatterns = [
    # Outras rotas...
    path('create_planet/', views.create_planet, name='create_planet'),
    path('list_planets/', views.list_planets, name='list_planets'),
    path('list_distances/', views.list_distances, name='list_distances'),
    path('create_distance/', views.create_distance, name='create_distance'),
    path('create_travel/', views.create_travel, name='create_travel'),
    path('search_trips/', views.search_trips, name='search_trips'),
    path('planet/<int:pk>/', views.detail_planet, name='detail_planet'),
]

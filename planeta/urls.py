from django.urls import path
from . import views

urlpatterns = [
    # Outras rotas...
    path('criar/', views.criar_planeta, name='criar_planeta'),
    path('lista/', views.lista_planetas, name='lista_planetas'),
]

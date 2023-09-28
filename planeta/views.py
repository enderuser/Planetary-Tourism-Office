from django.shortcuts import render, redirect
from .models import Planeta, DistanciaEntrePlanetas
from .forms import PlanetaForm, DistanciaForm

def criar_planeta(request):
    if request.method == 'POST':
        form = PlanetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_planetas')  # Redirecionar para a lista de planetas após a criação bem-sucedida
    else:
        form = PlanetaForm()

    return render(request, 'criar_planeta.html', {'form': form})

def lista_planetas(request):
    planetas = Planeta.objects.all()
    return render(request, 'lista_planetas.html', {'planetas': planetas})

def criar_distancia(request):
    if request.method == 'POST':
        form = DistanciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_distancias')  # Redireciona para a lista de distâncias após a criação bem-sucedida
    else:
        form = DistanciaForm()

    return render(request, 'criar_distancia.html', {'form': form})

def lista_distancias(request):
    distancias = DistanciaEntrePlanetas.objects.all()
    return render(request, 'lista_distancias.html', {'distancias': distancias})


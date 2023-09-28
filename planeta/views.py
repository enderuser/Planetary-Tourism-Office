from django.shortcuts import render, redirect
from .models import Planeta
from .forms import PlanetaForm

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
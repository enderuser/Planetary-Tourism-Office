from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlanetForm, DistanciaForm, PesquisaViagemForm, TravelForm
from .models import Planet, DistanciaEntrePlanetas, Travel
from django.core.paginator import Paginator

def create_planet(request):
    if request.method == 'POST':
        form = PlanetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_planets')
    else:
        form = PlanetForm()

    return render(request, 'create_planets.html', {'form': form})

def list_planets(request):
    planets = Planet.objects.all()
    return render(request, 'list_planets.html', {'planets': planets})

def detail_planet(request, pk):
    planeta = get_object_or_404(Planet, pk=pk)

    return render(request, 'detail_planet.html', {'planeta': planeta})

def list_distances(request):
    distances = DistanciaEntrePlanetas.objects.all()

    paginator_list_distances = Paginator(distances, 12)
    page_list_distances = request.GET.get('page')

    distances = paginator_list_distances.get_page(page_list_distances)

    return render(request, 'list_distance.html', {'distances': distances})

def create_distance(request):
    if request.method == 'POST':
        form = DistanciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_distances')
    else:
        form = DistanciaForm()

    return render(request, 'create_distance.html', {'form': form})

def create_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TravelForm()

    return render(request, 'create_travel.html', {'form': form})

def search_trips(request):
    if request.method == 'POST':
        form = PesquisaViagemForm(request.POST)
        if form.is_valid():
            departure = form.cleaned_data['departure']
            arriving = form.cleaned_data['arriving']
            data = form.cleaned_data['data']

            viagens = Travel.objects.filter(departure=departure, arriving=arriving, data=data)
            
            return render(request, 'results_search.html', {'viagens': viagens, 'form': form})

    else:
        form = PesquisaViagemForm()

    return render(request, 'search_trips.html', {'form': form})

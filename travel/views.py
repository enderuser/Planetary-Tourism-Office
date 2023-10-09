from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlanetForm, DistanciaForm, PesquisaViagemForm, TravelForm
from .models import Planet, DistanciaEntrePlanetas, Travel
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_planet(request):
    if request.method == 'POST':
        form = PlanetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_planets')
    else:
        form = PlanetForm()

    return render(request, 'create_planets.html', {'form': form})

@csrf_exempt
def list_planets(request):
    planets = Planet.objects.all()
    return render(request, 'list_planets.html', {'planets': planets})

@csrf_exempt
def detail_planet(request, pk):
    planeta = get_object_or_404(Planet, pk=pk)

    return render(request, 'detail_planet.html', {'planeta': planeta})

@csrf_exempt
def list_distances(request):
    distances = DistanciaEntrePlanetas.objects.all()

    paginator_list_distances = Paginator(distances, 12)
    page_list_distances = request.GET.get('page')

    distances = paginator_list_distances.get_page(page_list_distances)

    return render(request, 'list_distance.html', {'distances': distances})

@csrf_exempt
def create_distance(request):
    if request.method == 'POST':
        form = DistanciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_distances')
    else:
        form = DistanciaForm()

    return render(request, 'create_distance.html', {'form': form})

@csrf_exempt
def create_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TravelForm()

    return render(request, 'create_travel.html', {'form': form})

@csrf_exempt
def detail_travel(request, travel_id):
    viagem = get_object_or_404(Travel, id=travel_id)
    return render(request, 'detail_travel.html', {'viagem': viagem})

@csrf_exempt
def search_trips(request):
    if request.method == 'POST':
        
        departure_id = request.POST.get('departure')
        arriving_id = request.POST.get('arriving')
        data = request.POST.get('data')

        viagens = Travel.objects.filter(departure_id=departure_id, arriving_id=arriving_id, data=data)
        
        return render(request, 'results_search.html', {'viagens': viagens})

    else:
        form = PesquisaViagemForm()

    return render(request, 'search_trips.html', {'form': form})

@csrf_exempt
def search_earth_trips(request):

    departure_earth_id = 3

    viagens = Travel.objects.filter(departure_id=departure_earth_id)
    
    return render(request, 'search_departure.html', {'viagens': viagens})
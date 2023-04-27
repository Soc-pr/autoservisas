from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Vehicle, VehicleModel, Order


def index(request):
    num_vehicles = Vehicle.objects.all().count()
    num_vehicle_models = VehicleModel.objects.all().count()

    context = {
        'num_vehicles': num_vehicles,
        'num_vehicle_models': num_vehicle_models,
    }

    return render(request, 'index.html', context=context)


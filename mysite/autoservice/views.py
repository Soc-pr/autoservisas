from django.shortcuts import render
from django.http import HttpResponse
from .models import Service, Vehicle, VehicleModel, Order


def index(request):
    num_vehicles = Vehicle.objects.all().count()
    num_vehicle_models = VehicleModel.objects.all().count()
    num_services = Service.objects.all().count()
    num_completed_orders = Order.objects.filter(status__exact='d').count(),


    context = {
        'num_vehicles': num_vehicles,
        'num_vehicle_models': num_vehicle_models,
        'num_services': num_services,
        'num_completed_orders': num_completed_orders

    }

    return render(request, 'index.html', context=context)


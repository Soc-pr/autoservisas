from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service, Vehicle, VehicleModel, Order, OrderLine
from django.views import generic


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

def vehicles(request):
    vehicles = Vehicle.objects.all()
    context = {
         'vehicles': vehicles
    }
    return render(request, 'vehicles.html', context=context)

def vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'vehicle.html', context=context)

class OrderListView(generic.ListView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'orders'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = 'order'


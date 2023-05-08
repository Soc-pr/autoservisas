from django.shortcuts import render, get_object_or_404
from .models import Service, Vehicle, VehicleModel, Order, OrderLine
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q


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
    paginator = Paginator(Vehicle.objects.all(), 4)
    page_number = request.GET.get('page')
    paged_vehicles = paginator.get_page(page_number)
    context = {
         'vehicles': paged_vehicles
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
    paginate_by = 3
    template_name = 'orders.html'
    context_object_name = 'orders'

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order.html"
    context_object_name = 'order'

def search(request):
    query = request.GET.get('query')
    search_results = Vehicle.objects.filter(Q(plate__icontains=query) | Q(vehicle_model__maker__icontains=query) |
                                            Q(vin_code__icontains=query) | Q(client__icontains=query) |
                                            Q(vehicle_model__modelis__icontains=query))
    return render(request, 'search.html', {'vehicles': search_results, 'query': query})
from django.contrib import messages
from django.contrib.auth.forms import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_protect

from .models import Service, Vehicle, VehicleModel, Order


def index(request):
    num_vehicles = Vehicle.objects.all().count()
    num_vehicle_models = VehicleModel.objects.all().count()
    num_services = Service.objects.all().count()
    num_completed_orders = Order.objects.filter(status__exact='d').count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_vehicles': num_vehicles,
        'num_vehicle_models': num_vehicle_models,
        'num_services': num_services,
        'num_completed_orders': num_completed_orders,
        'num_visits': num_visits,

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


class MyOrderListView(generic.ListView):
    model = Order
    template_name = "my_orders.html"
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')

from django.contrib import admin

from .models import VehicleModel, Service, Vehicle, Order, OrderLine


# Register your models here.

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ("date", "vehicle")
    inlines = [OrderLineInLine]


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ("service", "order", "quantity")
    list_editable = ["quantity"]


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("vehicle_model", "vin_code", "plate", "client")
    list_filter = ['client', 'vehicle_model__maker', 'vehicle_model__modelis']
    search_fields = ['plate', "vin_code"]

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    list_editable = ['price']


admin.site.register(VehicleModel)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)

from django.contrib import admin

from .models import VehicleModel, Service, Vehicle, Order, OrderLine


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ("date", "vehicle")


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ("service", "order", "quantity")


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("vehicle_model", "plate", "client")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


def display_orderline(self):
    return ", ".join(orderline.service for orderline in self.orderline.all())


display_orderline.short_description = "Bele"

admin.site.register(VehicleModel)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)

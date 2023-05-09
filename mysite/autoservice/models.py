from django.contrib.auth.models import User
from django.db import models
import datetime
import pytz
utc=pytz.UTC


class VehicleModel(models.Model):
    maker = models.CharField("Gamintojas", max_length=50)
    modelis = models.CharField("Modelis", max_length=50)

    def __str__(self):
        return f"{self.maker} {self.modelis}"

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = "Automobilių modeliai"


class Service(models.Model):
    name = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite paslaugos pavadinimą')
    price = models.IntegerField('Kaina', help_text='Įveskite paslaugos kainą')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"


class Vehicle(models.Model):
    plate = models.CharField('Valst_Numeris', max_length=7)
    vehicle_model = models.ForeignKey(to="VehicleModel", max_length=50,
                                      on_delete=models.SET_NULL, null=True)
    vin_code = models.CharField('VIN', max_length=15)
    client = models.CharField('Klientas', max_length=25)
    photo = models.ImageField(verbose_name="Nuotrauka", upload_to="vehicles", null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle_model} ({self.plate})"

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"


class Order(models.Model):
    date = models.DateField("Data", null=True, blank=True)
    vehicle = models.ForeignKey(to="Vehicle", verbose_name='Automobilis',
                                max_length=50, on_delete=models.SET_NULL,
                                null=True)
    deadline = models.DateTimeField(verbose_name="Terminas", null=True, blank=True)
    owner = models.ForeignKey(to=User, verbose_name="Savininkas", on_delete=models.SET_NULL, null=True, blank=True)

    def deadline_over(self):
        return self.deadline and datetime.datetime.today().replace(tzinfo=utc) > self.deadline.replace(tzinfo=utc)

    def total(self):
        total_sum = 0
        for line in self.lines.all():
            total_sum += line.sum()
        return total_sum

    ORDER_STATUS = (
        ('p', 'Priimta'),
        ('r', 'Remontuojama'),
        ('d', 'Darbai baigti'),
    )

    status = models.CharField(verbose_name="Būsena",
                              max_length=1, choices=ORDER_STATUS,
                              blank=True, default='p')

    def __str__(self):
        return f"{self.vehicle}"

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"


class OrderLine(models.Model):
    service = models.ForeignKey(to="Service", verbose_name='Paslauga',
                                max_length=50, on_delete=models.SET_NULL,
                                null=True)
    order = models.ForeignKey(to="Order", verbose_name='Užsakymas',
                              max_length=50, on_delete=models.SET_NULL, null=True, related_name='lines')
    quantity = models.IntegerField(verbose_name='Kiekis')

    def sum(self):
        return self.service.price * self.quantity

    def __str__(self):
        return f"{self.order.vehicle} ({self.order.date}): {self.service} - {self.quantity}"

    class Meta:
        verbose_name = "Užsakymo eilutė"
        verbose_name_plural = "Užsakymo eilutės"

from django.db import models


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
    price = models.CharField('Kaina', max_length=5, help_text='Įveskite paslaugos kainą')

    def __str__(self):
        return f"{self.name} = {self.price}"

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"


class Vehicle(models.Model):
    plate = models.CharField('Valst_Numeris', max_length=7)
    vehicle_model = models.ForeignKey(to="VehicleModel", max_length=50,
                                      on_delete=models.SET_NULL, null=True)
    vin_code = models.CharField('VIN', max_length=15)
    client = models.CharField('Klientas', max_length=25)

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
    ORDER_STATUS = (
        ('p', 'Priimta'),
        ('r', 'Remontuojama'),
        ('d', 'Darbai baigti'),
    )

    status = models.CharField(verbose_name="Būsena",
                              max_length=1, choices=ORDER_STATUS,
                              blank=True, default='p')

    def __str__(self):
        return f"{self.vehicle} ({self.date}) {self.status}"

    class Meta:
        verbose_name = "Užsakymas"
        verbose_name_plural = "Užsakymai"


class OrderLine(models.Model):
    service = models.ForeignKey(to="Service", verbose_name='Paslauga',
                                max_length=50, on_delete=models.SET_NULL,
                                null=True)
    order = models.ForeignKey(to="Order", verbose_name='Užsakymas',
                              max_length=50, on_delete=models.SET_NULL, null=True)
    quantity = models.CharField(verbose_name='Kiekis', max_length=2)

    def __str__(self):
        return f"{self.order.vehicle} ({self.order.date}): {self.service} - {self.quantity}"

    class Meta:
        verbose_name = "Užsakymo eilutė"
        verbose_name_plural = "Užsakymo eilutės"

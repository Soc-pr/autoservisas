# Generated by Django 4.2 on 2023-05-09 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autoservice', '0005_vehicle_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Savininkas'),
        ),
        migrations.AlterField(
            model_name='order',
            name='vehicle',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.vehicle', verbose_name='Automobilis'),
        ),
    ]
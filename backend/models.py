from multiprocessing import managers
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Manager(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)


class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    manager = models.ForeignKey(
        Manager, on_delete=models.CASCADE, related_name='stores')
    net_sales = models.FloatField()


class Furniture(models.Model):

    class FurnitureState(models.TextChoices):
        NEW = 'NEW', _('New')
        USED = 'USED', _('Used')
        BAD = 'BAD', _('Bad')
        UNUSABLE = 'UNUSABLE', _('Unusable')

    class FurnitureStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE', _('Available')
        SOLD = 'SOLD', _('Sold')

    name = models.CharField(max_length=100)
    state = models.CharField(
        max_length=100, choices=FurnitureState.choices, default=FurnitureState.NEW)
    price = models.FloatField()
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name='furnitures')
    status = models.CharField(
        max_length=100, choices=FurnitureStatus.choices, default=FurnitureStatus.AVAILABLE)

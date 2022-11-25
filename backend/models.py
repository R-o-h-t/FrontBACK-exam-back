from multiprocessing import managers
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class GenderChoice(models.TextChoices):
    M = 'M', "Male"
    F = 'F', "Female"


class RoleChoice(models.TextChoices):
    A = 'A', "Admin"
    U = 'U', "User"


class User(models.Model):
    id: models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    civil = models.CharField(
        max_length=1, choices=GenderChoice.choices, default=GenderChoice.F)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(
        max_length=1, choices=RoleChoice.choices, default=RoleChoice.U)

    def __str__(self):
        return self.civil + ' ' + self.firstname + '"' + self.username + '"' + self.lastname


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    kilometers = models.FloatField()
    daily_price = models.FloatField()
    available = models.BooleanField()
    # image (url)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.brand + ' ' + self.model + ' (' + str(self.year) + ')'


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    days = models.IntegerField(null=True, blank=True)
    kilometers = models.FloatField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username + ' ' + self.vehicle.brand + ' ' + self.vehicle.model + ' (' + str(self.vehicle.year) + ')'

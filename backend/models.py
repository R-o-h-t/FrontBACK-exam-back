from multiprocessing import managers
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(models.Model):
    id: models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    civil = models.CharField(max_length=1, choices=[('M', 'F')])
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', 'U')])

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
    image = models.ImageField(
        upload_to='images/vehicles', null=True, blank=True)

    def __str__(self):
        return self.brand + ' ' + self.model + ' (' + str(self.year) + ')'


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField()
    days = models.IntegerField()
    kilometers = models.FloatField()
    total_price = models.FloatField()

    def __str__(self):
        return self.user.username + ' ' + self.vehicle.brand + ' ' + self.vehicle.model + ' (' + str(self.vehicle.year) + ')'

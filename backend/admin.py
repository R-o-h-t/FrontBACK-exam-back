from django.contrib import admin

from backend import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Vehicle)
admin.site.register(models.Booking)

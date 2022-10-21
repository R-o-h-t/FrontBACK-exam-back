from django.contrib import admin

from backend import models

# Register your models here.
admin.site.register(models.Manager)
admin.site.register(models.Store)
admin.site.register(models.Furniture)

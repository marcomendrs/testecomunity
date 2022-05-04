from django.contrib import admin
from catalogo import models
# Register your models here.
@admin.register(models.Modelo)
class ModeloAdmin(admin.ModelAdmin):
    pass

@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    pass

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    pass
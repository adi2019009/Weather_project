from django.contrib import admin

# Register your models here.
from .models import CityWeatherData

admin.site.register(CityWeatherData)
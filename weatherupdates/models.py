from statistics import mode
from django.db import models

# Create your models here.


class CityWeatherData(models.Model):
    city = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.TextField()
    temperature = models.TextField()
    country_code = models.CharField(max_length=10)
    wind = models.TextField()
    humidity = models.TextField()
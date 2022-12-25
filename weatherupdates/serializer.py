from rest_framework import serializers
from .models import CityWeatherData


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityWeatherData
        fields = '__all__'
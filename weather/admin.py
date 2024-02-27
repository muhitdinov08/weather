from django.contrib import admin

from weather.models import Weather


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ['city_name']
    search_fields = ['city_name']

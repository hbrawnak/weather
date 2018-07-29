from django.shortcuts import render
import requests
from .models import City

# Create your views here.

def index(request):

    key = '806fc11050d77b8f86428810573a0b2f'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + key

    city = 'Tongi'

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data}

    return render(request, 'weather/index.html', context)

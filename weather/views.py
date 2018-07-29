from django.shortcuts import render
import requests

# Create your views here.

def index(request):

    key = '806fc11050d77b8f86428810573a0b2f'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + key

    city = 'Chittagong'

    r  = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather': city_weather}

    return render(request, 'weather/index.html', context)

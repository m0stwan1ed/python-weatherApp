import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    appId = 'c03ae73b6f1a49b21051e3a8976f6583'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appId

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    allCities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
        }
        allCities.append(city_info)

    context = {'allInfo': allCities, 'form': form}
    return render(request, 'weather/index.html', context)

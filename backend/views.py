from django.http import JsonResponse
from django.shortcuts import render
import json
from backend.models import Weather
from datetime import datetime
def index(request):
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.method == 'POST':
        data = json.loads(request.body)
        temperature = data['temperature']
        humidity = data['humidity']
        dataset= {Weather:WeatherHandle(request,temperature,humidity),Season : SeasonHandle(request,server_time)}
        return JsonResponse(dataset)
def WeatherHandle(request, temperature, humidity):
    if (temperature>10 and humidity>10):
        return "Sunny"
    elif(temperature<10 and humidity<10):
        return "Rainy"
    elif(temperature>10 and humidity<10):
        return "Cloudy"
    elif(temperature<10 and humidity>10):
        return "Snowy"
    else:
        return "Foggy"
def SeasonHandle(request,server_time):
    month = datetime.strptime(server_time, "%Y-%m-%d %H:%M:%S").month
    if((month == 1) | (month == 2) |(month ==12)):
        return "Winter"
    elif(month>=3 & month <= 5):
        return "Spring"
    elif(month>=6 & month <= 8):
        return "Summer"
    else:
        return "Fall"





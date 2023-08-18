from django.shortcuts import render, HttpResponse
import requests
import json

def home(request):
    url_weather = "https://api.tomorrow.io/v4/weather/realtime?location=laboulaye&units=metric&apikey=0dZxpn6zuemhdICzqDp2Rfe1tcjpd3m2"
    headers_weather = {"accept": "application/json"}
    response_weather = requests.get(url_weather, headers=headers_weather)
    data_weather = json.loads(response_weather.text)

    url_dollar_official = 'https://dolarapi.com/v1/dolares/oficial'
    response_dollar_official = requests.get(url_dollar_official)
    data_dollar_official = json.loads(response_dollar_official.text)

    url_dollar_blue = 'https://dolarapi.com/v1/dolares/blue'
    response_dollar_blue = requests.get(url_dollar_blue)
    data_dollar_blue = json.loads(response_dollar_blue.text)

    context = {
        'weather': data_weather,
        'dollar_official': data_dollar_official,
        'dollar_blue': data_dollar_blue
    }

    return render(request, 'appLaboulayeNews/home.html', context)

def news(request):
    return render()


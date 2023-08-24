from django.shortcuts import render, HttpResponse, get_object_or_404
import requests
import json
from appLaboulayeNews.models import Category, News
import markdown
import math



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


def home(request, current_page = 1):

    news_for_page = 8

    start = (current_page - 1) * news_for_page

    page = {
        'back': current_page - 1,
        'next': current_page + 1,
        'last': math.ceil(News.objects.count()/news_for_page)
    }        
    recent_news = News.objects.order_by('-id')[start:start + news_for_page]

    if page['back'] <1:
        page['back'] = 1

    categories = Category.objects.all()

    context = {
        'categories': categories,
        'page': page,
        'recent_news': recent_news,
        'weather': data_weather,
        'dollar_official': data_dollar_official,
        'dollar_blue': data_dollar_blue
    }
    return render(request, 'appLaboulayeNews/home.html', context)

def news(request, id):
    
    news = News.objects.get(pk=id)

    contenido_markdown = news.body
    contenido_html = markdown.markdown(contenido_markdown)

    news.body = contenido_html

    context = {
        'news': news,
        'weather': data_weather,
        'dollar_official': data_dollar_official,
        'dollar_blue': data_dollar_blue
    }
    return render(request, 'appLaboulayeNews/news.html', context)

def category(request,cat, current_page = 1):
    news_for_page = 8
    cat = get_object_or_404(Category, name=cat)
    start = (current_page - 1) * news_for_page
    
    page = {
        'back': current_page - 1,
        'next': current_page + 1,
        'last': math.ceil(News.objects.filter(category=cat).count()/news_for_page)
    }        
    
    recent_news = News.objects.filter(category=cat).order_by('-id')[start:start + news_for_page]

    if page['back'] <1:
        page['back'] = 1

    categories = Category.objects.all()

    context = {
        'categories': categories,
        'page': page,
        'recent_news': recent_news,
        'weather': data_weather,
        'dollar_official': data_dollar_official,
        'dollar_blue': data_dollar_blue
    }
    return render(request, 'appLaboulayeNews/categories.html', context)
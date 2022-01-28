from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):    
    return HttpResponse("<h1>Главная страница</h1>")


def groups_posts(request, slug):
    return HttpResponse("<h2>Страницы сообществ</h2>")



from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    template = 'posts/index.html'   
    return render(request, template)

def groups_posts(request, slug):
    return HttpResponse("<h2>Страницы сообществ</h2>")




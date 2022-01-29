# posts/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('groups/<slug>', views.groups_posts),
]

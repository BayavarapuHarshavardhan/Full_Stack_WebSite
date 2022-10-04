from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
   path('update', views.update, name="update"),
    path('about', views.about, name="about"),
]
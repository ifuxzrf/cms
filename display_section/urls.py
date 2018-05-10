from django.contrib import admin
from django.urls import path
from display_section import views

urlpatterns = [
    path('', views.index, name='index'),
]

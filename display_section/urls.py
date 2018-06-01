from django.contrib import admin
from django.urls import path
from display_section import views

urlpatterns = [
    path('', views.ThingsView.as_view(), name='index'),
    path('form/', views.form1, name='form'),
]

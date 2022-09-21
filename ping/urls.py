from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('v1/record-ip-address/', views.record_ip, name="record-ip")
]
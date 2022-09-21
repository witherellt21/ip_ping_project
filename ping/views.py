from django.shortcuts import render, redirect
# from django.views.generic import RedirectView
import requests

from .models import ip_address

def home(request):
    return render(request, 'ping/home.html')


def record_ip(request):
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()
    new = ip_address(ip_address = ip['ip'])
    new.save()
    return redirect('home')
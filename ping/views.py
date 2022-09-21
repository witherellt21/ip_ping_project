from django.shortcuts import render, redirect
# from django.views.generic import RedirectView
import requests


def home(request):
    return render(request, 'ping/home.html')


def record_ip(request):
    #print(request.method)
    #response = requests.get('http:')
    print(request)
    return redirect('home')
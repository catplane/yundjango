from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponse("hello world")


def say(request):
    # 对于未指明namespace的，reverse(路由name)
    # 对于指明namespace的，reverse(命名空间namespace: 路由name)
    url = reverse('index')
    print(url)
    return redirect(url)


def weather(request, city, year):
    print(city)
    print(year)
    return HttpResponse('OK')

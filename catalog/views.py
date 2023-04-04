from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Главная страница сайта Мир книг.</h1>")


# Create your views here.

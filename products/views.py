from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1> index page </h1>')

def about(request):
    return HttpResponse('<h1> about page </h1>')

def index3(request):
    return HttpResponse('<h1> index3 page </h1>')
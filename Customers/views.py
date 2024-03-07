from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_a(request):
    return HttpResponse('aaaaaaaaa')

def index_b(request):
    return HttpResponse('bbbbbbbbbbbbb')

def index_c(request):
    return HttpResponse('cccccccccc')
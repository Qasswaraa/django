from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index-page'),
    path('about', views.about, name='about-page'),
    path('index3/', views.index3, name='index3-page'),
]
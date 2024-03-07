from django.urls import path
from . import views

urlpatterns = [

    path('index_a', views.index_a, name='index-A'),
    path('index_b', views.index_b, name='about-B'),
    path('index_c', views.index_c, name='index3-C'),
]
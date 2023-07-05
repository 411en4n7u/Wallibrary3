from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('agregar-producto', views.agregar_producto, name='agregar-producto'),
]

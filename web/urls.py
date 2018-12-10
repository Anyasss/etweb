from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_producto, name='lista_producto'),
]

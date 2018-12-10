from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_producto, name='lista_producto'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/new', views.nuevo_producto, name='nuevo_producto'),
]

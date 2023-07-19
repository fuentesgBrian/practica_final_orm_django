from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertar_lab, name='insertar_lab'),
    path('mostrar/', views.mostrar_lab, name='mostrar_lab'),
]

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prueba/',views.PruebaView.as_view()),
    path('pruebaLista/',views.PruebaListView.as_view()),
    path('pruebaPruebas/',views.ListarPruebasListView.as_view()),
    path('pruebaCreate/',views.PruebaCreateView.as_view()),
]
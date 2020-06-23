from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)
#import models
from .models import Prueba

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumero'
    queryset = ['1','10','20','30']


class ListarPruebasListView(ListView):
    template_name = "home/template_pruebas.html"
    model = Prueba
    context_object_name = 'lista'   


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    fields = ['titulo','subtitulo','cantidad']


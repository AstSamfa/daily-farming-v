from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

from .models import Requisito, Cuidado, Cultivo


#mostrar el contenido de index.html
def index(request):
    return render(request,"cultivos/index.html")


class RequisitoListado(ListView):
    model = Requisito


class RequisitoCrear(SuccessMessageMixin, CreateView):
    model = Requisito
    form = Requisito
    fields = "__all__"
    success_message = 'Requisito creado correctamente'

    def get_success_url(self):
        return reverse('leer')


class RequisitoDetalle(DetailView):
    model = Requisito


class RequisitoActualizar(SuccessMessageMixin, UpdateView):
    model = Requisito
    form = Requisito
    fields = "__all__"
    success_message = 'Requisito actualizado correctamente'

    def get_success_url(self):
        return reverse('leer')


class RequisitoEliminar(SuccessMessageMixin, DeleteView):
    model = Requisito
    form = Requisito
    fields = "__all__"

    def get_success_url(self):
        success_message = 'Requisito eliminado correctamente'
        messages.success(self.request, success_message)
        return reverse('leer')


class CuidadoListado(ListView):
    model = Cuidado


class CuidadoCrear(SuccessMessageMixin, CreateView):
    model = Cuidado
    form = Cuidado
    fields = '__all__'
    success_message = 'Cuidado creado exitosamente'
    
    def get_success_url(self):
        return reverse('leerCuidado')


class CuidadoDetalle(DetailView):
    model = Cuidado


class CuidadoActualizar(SuccessMessageMixin, UpdateView):
    model = Cuidado
    form = Cuidado
    fields = '__all__'
    success_message = 'Cuidado actualizado exitosamente!'
    
    def get_success_url(self):
        return reverse('leerCuidado')


class CuidadoEliminar(SuccessMessageMixin, DeleteView):
    model = Cuidado
    form = Cuidado
    fields = 'all'
    
    def get_success_url(self):
        success_message = 'Cuidado eliminado exitosamente!'
        messages.success(self.request, success_message)
        return reverse('leerCuidado')


class CultivoListado(ListView):
    model = Cultivo


class CultivoCrear(SuccessMessageMixin, CreateView):
    model = Cultivo
    form = Cultivo
    fields = '__all__'
    success_message = 'Cultivo creado exitosamente'
    
    def get_success_url(self):
        return reverse('leerCultivo')


class CultivoDetalle(DetailView):
    model = Cultivo


class CultivoActualizar(SuccessMessageMixin, UpdateView):
    model = Cultivo
    form = Cultivo
    fields = '__all__'
    success_message = 'Cultivo actualizado exitosamente!'
    
    def get_success_url(self):
        return reverse('leerCultivo')


class CultivoEliminar(SuccessMessageMixin, DeleteView):
    model = Cultivo
    form = Cultivo
    fields = 'all'
    
    def get_success_url(self):
        success_message = 'Cultivo eliminado exitosamente!'
        messages.success(self.request, success_message)
        return reverse('leerCultivo')


def prueba(request):
    return render(request,"cultivos/funciones.html")
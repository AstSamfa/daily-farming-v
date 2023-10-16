"""
URL configuration for dailyfarming project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cultivos.views import *

from cultivos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('funcion/', views.prueba, name="prueba"),

    #* cultivos - Requisito
    path('requisito/', RequisitoListado.as_view(template_name = "requisito/index.html"), name='leer'),
    path('requisito/detalles/<int:pk>', RequisitoDetalle.as_view(template_name = "requisito/detalles.html"), name='detallesRequisito'),
    
    #* cultivos - Cuidado
    path('cuidado/',    CuidadoListado.as_view(template_name = "cuidado/tabla.html"), name='leerCuidado'),
    path('cuidado/detalles/<int:pk>', CuidadoDetalle.as_view(template_name = "cuidado/detalles.html"), name='detallesCuidado'),
    
    #* cultivos - Cultivo
    path('cultivo/',    CultivoListado.as_view(template_name = "cultivos/tabla.html"), name='leerCultivo'),
    path('cultivo/detalles/<int:pk>', CultivoDetalle.as_view(template_name = "cultivo/detalles.html"), name='detallesCultivo'), 
    path('cultivo/crear', CultivoCrear.as_view(template_name = "cultivo/crear.html"), name='crearCultivo'),
    path('cultivo/editar/<int:pk>', CultivoActualizar.as_view(template_name = "cultivo/actualizar.html"), name='actualizarCultivo'), 
    path('cultivo/eliminar/<int:pk>', CultivoEliminar.as_view(), name='eliminarCultivo'),
]

urlpatterns += staticfiles_urlpatterns()
from django.urls import path
from . import views


urlpatterns = [
    path("dentistas/", views.listar_dentistas, name='Lista_Dentistas'),
    path("insertar_dentista/", views.insertar_dentista, name='Insertar_Dentista'),
]

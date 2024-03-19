from django.urls import path
from . import views


urlpatterns = [
    path('details/', views.pacientes, name='Pacientes'),
    path('details/edit/<int:pk>/', views.pacient_edit, name='edit'),
    path('details/information/<int:pk>/', views.patient_information, name='information'),
    path('insertar_dentista/', views.insertar_dentista, name='insertar_dentista'),
    path('dentistas/', views.listar_dentistas, name='lista_dentistas'),
    path('insertar_paciente/', views.insertar_paciente, name='insertar_paciente'),
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('insertar_tratamiento/', views.insertar_tratamiento, name='insertar_tratamiento'),
    path('tratamientos/', views.listar_tratamientos, name='listar_tratamientos'),
    path('insertar_historial/', views.insertar_historial, name='insertar_historial'),
    path('listar_historiales/', views.listar_historiales, name='listar_historiales'),
    path('agregar_tratamiento_paciente/', views.agregar_tratamiento_paciente, name='agregar_tratamiento_paciente'),




    ]
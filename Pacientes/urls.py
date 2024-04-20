from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('details/', views.pacientes, name='Pacientes'),
    path('details/edit/<int:pk>/', views.pacient_edit, name='edit'),
    path('details/information/<int:pk>/', views.patient_information, name='information'),
    path('insertar_paciente/', views.insertar_paciente, name='insertar_paciente'),
    path('insertar_tratamiento/', views.insertar_tratamiento, name='insertar_tratamiento'),
    path('tratamientos/', views.listar_tratamientos, name='listar_tratamientos'),
    path('insertar_historial/', views.insertar_historial, name='insertar_historial'),
    path('listar_historiales/', views.listar_historiales, name='listar_historiales'),
    path('agregar_tratamiento_paciente/', views.agregar_tratamiento_paciente, name='agregar_tratamiento_paciente'),
    path('insertar_tipo_imagen_medica/', views.insertar_tipo_imagen_medica, name='insertar_tipo_imagen_medica'),
    path('insertar_imagen_medica/', views.insertar_imagen_medica, name='insertar_imagen_medica'),

    path('eliminar/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),

    path('ver_imagenes_tipos/', views.ver_imagenes_tipos, name='ver_imagenes_tipos'),
    path('ver_imagenes_medicas/', views.ver_imagenes_medicas, name='ver_imagenes_medicas'),

    path('dentistas/edit/<int:pk>/', views.dentista_edit, name='edit_dentista'),
    path('dentistas/information/<int:dentista_id>/', views.dentista_information, name='dentista_information'),
    path('dentistas/delete/<int:pk>/', views.dentista_delete, name='delete_dentista'),
    path('pacientes-inactivos/', views.pacientes_inactivos, name='pacientes_inactivos'),
    path('admin/', admin.site.urls),
    path('agendas/add/', views.agenda_create, name='agenda'),
    path('agendas/', views.AgendaList, name='agenda_list'),
    path('agendas/finalizado/', views.AgendaListFinalizado, name='agenda_list_finalizado'),

    


]
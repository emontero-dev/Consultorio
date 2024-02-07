from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.pacientes, name='Pacientes'),
    path('details/edit/<int:pk>/', views.pacient_edit, name='edit'),
    path('details/information/<int:pk>/', views.patient_information, name='information'),]
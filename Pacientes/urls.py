from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.pacientes, name='Pacientes'),
               ]
"""Urls asociados a las rutas de las paginas"""
from django.urls import path
from .views import home, medico, pacientes, reservar, index, registrar_reserva_html
from . import views

urlpatterns = [
    path('', home, name = "home"),
    path('home', home, name = "home"),
    path('Medico', medico, name = "Medico"),
    path('Pacientes', pacientes, name = "Pacientes"),
    path('Reservar', reservar, name = "Reservar"),
    path('Index', index, name = "Index"),
    path('RegistrarReserva', registrar_reserva_html, name = "RegistrarReserva"),
    path('registrarMedico/', views.registrarmedico),
    path('eliminarMedico/<id>', views.eliminarmedico),
    path('registrarPaciente/', views.registrarpaciente),
    path('eliminarPaciente/<id>', views.eliminarpaciente),
    path('registrarReserva/', views.nuevareserva),
    path('eliminarReserva/<id>', views.eliminarreserva),
    path('anularReserva/<id>', views.anular_reserva),
    path('confirmarReserva/<id>', views.confirmar_reserva)
    ]

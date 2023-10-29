"""Creacion del panel de admin"""
from django.contrib import admin
#Imports de las tablas a utilizar
from .models import Agenda, Bloque, Box, Ciudad, Contrato, Especialidad
from .models import FormaPago, HistorialPago, Paciente, Prevision, Profesional, Rol, Usuario

#Tablas a visualizar para registrar datos
admin.site.register(Agenda)
admin.site.register(Bloque)
admin.site.register(Box)
admin.site.register(Ciudad)
admin.site.register(Contrato)
admin.site.register(Especialidad)
admin.site.register(FormaPago)
admin.site.register(HistorialPago)
admin.site.register(Paciente)
admin.site.register(Prevision)
admin.site.register(Profesional)
admin.site.register(Rol)
admin.site.register(Usuario)

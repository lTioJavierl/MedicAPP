"""Creacion de las tablas para la base de datos en SQLite"""
from django.db import models

class Bloque(models.Model):
    """Creacion tabla Bloque"""
    Descripcion = models.CharField(max_length=50, null=False)
    Estado = models.CharField(max_length=50, null=False)
    HoraInicio = models.CharField(max_length=50, null=False)
    HoraFin = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.Descripcion)

class Ciudad(models.Model):
    """Creacion tabla Ciudad"""
    NombreCiudad = models.CharField(max_length=30, null=False)
    Region = models.CharField(max_length=30, null=False)
    Pais = models.CharField(max_length=25, null=False)

    def __str__(self):
        return str(self.NombreCiudad)

class Rol(models.Model):
    """Creacion tabla Rol"""
    NombreRol = models.CharField(max_length=50, null=False)
    CargoRol = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.NombreRol)

class Prevision(models.Model):
    """Creacion tabla Prevision"""
    NombrePrevision = models.CharField(max_length=50, null=False)
    Cobertura = models.CharField(max_length=50, null=True)
    Tramo = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.NombrePrevision)

class FormaPago(models.Model):
    """Creacion tabla FormaPago"""
    TipoFormaPago = models.CharField(max_length=50, null=False)
    NombreFormaPago = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.NombreFormaPago)

class Especialidad(models.Model):
    """Creacion tabla Especialidad"""
    NombreEspecialidad = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.NombreEspecialidad)

class Box(models.Model):
    """Creacion tabla Box"""
    Descripcion = models.CharField(max_length=50, null=False)
    ValorMensual = models.CharField(max_length=50, null=False)
    FechaRegistro = models.DateField(null=False)

    def __str__(self):
        return str(self.Descripcion)

class Usuario(models.Model):
    """Creacion tabla Usuario"""
    IdRol = models.ForeignKey(Rol, on_delete=models.PROTECT, null=False)
    NombreUsuario = models.CharField(max_length=50, null=False)
    Contrasena = models.CharField(max_length=50, null=False)
    FechaUltimoIngreso = models.DateField(null=False)
    Estado = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.NombreUsuario)

class Profesional(models.Model):
    """Creacion tabla Profesional"""
    RutProfesional = models.CharField(max_length=50, null=False)
    IdCiudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, null=False)
    IdEspecialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, null=False)
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    Nombres = models.CharField(max_length=80, null=False)
    ApellidoP = models.CharField(max_length=30, null=False)
    ApellidoM = models.CharField(max_length=30, null=False)
    Direccion = models.CharField(max_length=30, null=True)
    Telefono = models.CharField(max_length=30, null=False)
    Email = models.CharField(max_length=50, null=False)
    Tarifa = models.CharField(max_length=30, null=False)
    Estado = models.CharField(max_length=50, null=False)
    FechaRegistro = models.DateField(null=False)

    def __str__(self):
        return str(self.RutProfesional)

class Contrato(models.Model):
    """Creacion tabla Contrato"""
    RutProfesional = models.ForeignKey(Profesional, on_delete=models.PROTECT, null=False)
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=False)
    FechaContrato = models.DateField(null=False)
    Porcentaje = models.CharField(max_length=15, null=False)
    Estado = models.CharField(max_length=50, null=False)
    FechaInicio = models.DateField(null=False)
    FechaFin = models.DateField(null=False)
    FechaRegistro = models.DateField(null=False)

    def __str__(self):
        return str(self.RutProfesional)

class HistorialPago(models.Model):
    """Creacion tabla HistorialPago"""
    RutProfesional = models.ForeignKey(Profesional, on_delete=models.PROTECT, null=False)
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    IdContrato = models.ForeignKey(Contrato, on_delete=models.PROTECT, null=False)
    IdFormaPago = models.ForeignKey(FormaPago, on_delete=models.PROTECT, null=False)
    FechaHoraPago = models.DateTimeField(null=False)
    Mes = models.CharField(max_length=15, null=False)
    Ano = models.CharField(max_length=10, null=False)
    ValorPago = models.CharField(max_length=50, null=False)
    ValorCancelar = models.CharField(max_length=50, null=False)
    EstadoPago = models.CharField(max_length=50, null=False)
    Descripcion = models.CharField(max_length=50, null=False)
    FechaRegistro = models.DateField(null=False)

    def __str__(self):
        return str(self.RutProfesional)

class Paciente(models.Model):
    """Creacion tabla Paciente"""
    RutPaciente = models.CharField(max_length=50, null=False)
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    IdCiudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, null=False)
    IdPrevision = models.ForeignKey(Prevision, on_delete=models.PROTECT, null=False)
    Nombres = models.CharField(max_length=80, null=False)
    NombreSocial = models.CharField(max_length=50, null=False)
    ApellidoP = models.CharField(max_length=30, null=False)
    ApellidoM = models.CharField(max_length=30, null=False)
    OrdenApellido = models.BooleanField(null=False)
    FechaNac = models.DateField(null=False)
    Email = models.CharField(max_length=50, null=False)
    Telefono = models.CharField(max_length=20, null=False)
    Direccion = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.RutPaciente)

class Agenda(models.Model):
    """Creacion tabla Agenda"""
    RutProfesional = models.ForeignKey(Profesional, on_delete=models.PROTECT, null=False)
    RutPaciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=False)
    IdBloque = models.ForeignKey(Bloque, on_delete=models.PROTECT, null=False)
    IdBox = models.ForeignKey(Box, on_delete=models.PROTECT, null=False)
    FechaHoraSolicitud = models.DateTimeField(null=False)
    FechaAtencion = models.DateField(null=False)
    Estado = models.CharField(max_length=50, null=False)
    Tarifa = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.RutPaciente)

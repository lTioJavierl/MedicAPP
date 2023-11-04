"""Rutas aplicacion"""

from django.shortcuts import render, redirect
from .models import Profesional, Ciudad, Especialidad, Usuario
from .models import Prevision, Paciente, Agenda, Bloque, Box
from django.contrib import messages

def home(request):
    """Ruta pagina home"""
    return render(request, 'app/home.html')

def medico(request):
    """Ruta pagina medicos"""
    medicos = Profesional.objects.all()
    ciudades = Ciudad.objects.all()
    especialidades = Especialidad.objects.all()
    usuarios = Usuario.objects.all()
    return render(request, 'app/Medico.html', {"Medicos": medicos, "Ciudades": ciudades,
    "Especialidades": especialidades,"Usuarios": usuarios})

def registrarmedico(request):
    """Registra un nuevo médico"""
    rut = request.POST['txt-RutM']
    ciudad_id = request.POST['select-Ciudad']
    ciudad = Ciudad.objects.get(id=ciudad_id)
    especialidad_id = request.POST['select-Especialidad']
    especialidad = Especialidad.objects.get(id=especialidad_id)
    usuario_id = request.POST['select-Usuario']
    usuario = Usuario.objects.get(id=usuario_id)
    nombres = request.POST['txt-nombres']
    apellidop = request.POST['txt-apep']
    apellidom = request.POST['txt-apem']
    direccion = request.POST['txt-direccion']
    telefono = request.POST['txt-telefono']
    email = request.POST['txt-email']
    tarifa = request.POST['txt-tarifa']
    estado = request.POST['txt-estado']
    fecharegistro = request.POST["txt-fecha-registro"]

    Profesional.objects.create(
        RutProfesional= rut,
        IdCiudad= ciudad,
        IdEspecialidad = especialidad,
        IdUsuario = usuario,
        Nombres = nombres,
        ApellidoP = apellidop,
        ApellidoM = apellidom,
        Direccion = direccion,
        Telefono = telefono,
        Email = email,
        Tarifa = tarifa,
        Estado = estado,
        FechaRegistro = fecharegistro)
    messages.success(request, "Medico registrado con exito")
    return redirect('Medico')

def eliminarmedico(request, id):
    """Funcion eliminar medico"""
    medicosd = Profesional.objects.get(id = id)
    medicosd.delete()
    messages.success(request, "Medico eliminado con exito")

    return redirect('Medico')

def pacientes(request):
    """Ruta pagina pacientes"""
    pacientes1 = Paciente.objects.all()
    ciudades = Ciudad.objects.all()
    usuarios = Usuario.objects.all()
    previsiones = Prevision.objects.all()
    return render(request, 'app/Pacientes.html', {"Pacientes": pacientes1, "Ciudades": ciudades,
                  "Usuarios": usuarios, "Previsiones": previsiones})

def registrarpaciente(request):
    """Funcion registrar paciente"""
    rut = request.POST['txt-RutP']
    usuario_id = request.POST['select-Usuario']
    usuario = Usuario.objects.get(id=usuario_id)
    ciudad_id = request.POST['select-Ciudad']
    ciudad = Ciudad.objects.get(id=ciudad_id)
    prevision_id = request.POST['select-Prevision']
    prevision = Prevision.objects.get(id=prevision_id)
    nombres = request.POST['txt-nombres']
    nombre_s = request.POST['txt-nombresocial']
    apellidop = request.POST['txt-apep']
    apellidom = request.POST['txt-apem']
    if 'orden-apellido' in request.POST:
        orden_ap = request.POST.get('orden-apellido') == 'on'
    else:
        orden_ap = False
    fecha_nacimiento = request.POST["txt-fecha-nacimiento"]
    email = request.POST['txt-email']
    telefono = request.POST['txt-telefono']
    direccion = request.POST['txt-direccion']

    Paciente.objects.create(
        RutPaciente = rut,
        IdUsuario = usuario,
        IdCiudad = ciudad,
        IdPrevision = prevision,
        Nombres = nombres,
        NombreSocial = nombre_s,
        ApellidoP = apellidop,
        ApellidoM = apellidom,
        OrdenApellido = orden_ap,
        FechaNac = fecha_nacimiento,
        Email = email,
        Telefono = telefono,
        Direccion = direccion)
    messages.success(request, "Paciente registrado con exito")
    return redirect('Pacientes')

def eliminarpaciente(request, id):
    """Funcion eliminar paciente"""
    paciente_e = Paciente.objects.get(id = id)
    paciente_e.delete()
    messages.success(request, "Paciente eliminado con exito")

    return redirect('Pacientes')

def reservar(request):
    """Ruta pagina reservas"""
    agenda = Agenda.objects.all()
    return render(request, 'app/Reservar.html', {"Agendas": agenda})

def registrar_reserva_html(request):
    """Ruta pagina registro de reservas"""
    medicos = Profesional.objects.all()
    pacientes = Paciente.objects.all()
    bloque = Bloque.objects.all()
    box = Box.objects.all()
    return render(request, 'app/RegistrarReserva.html', {"Medicos": medicos, 
    "Pacientes": pacientes, "Bloques": bloque, "Boxes": box})

def nuevareserva(request):
    """Funcion registro de reserva"""
    rutp_id = request.POST.get('select-Profesional')
    rutp = Profesional.objects.get(id=rutp_id)
    rutpa_id = request.POST.get('select-Paciente')
    rutpa = Paciente.objects.get(id=rutpa_id)
    bloque_id = request.POST.get('select-Bloque')
    bloque = Bloque.objects.get(id=bloque_id)
    box_id = request.POST.get('select-Box')
    box = Box.objects.get(id=box_id)
    fecha_solicitud = request.POST.get('txt-fecha-solicitud')
    hora_solicitud = request.POST.get('txt-hora-solicitud')
    fecha_hora_soli = f"{fecha_solicitud} {hora_solicitud}"
    fecha_atencion = request.POST.get('txt-fecha-atencion')
    estado = request.POST.get('txt-estado')
    tarifa = request.POST.get('txt-tarifa')

    Agenda.objects.create(
        RutProfesional=rutp,
        RutPaciente=rutpa,
        IdBloque=bloque,
        IdBox=box,
        FechaHoraSolicitud=fecha_hora_soli,
        FechaAtencion=fecha_atencion,
        Estado=estado,
        Tarifa=tarifa
    )
    messages.success(request, "Reserva agendada con exito")
    return redirect('Reservar')

def eliminarreserva(request, id):
    """Funcion eliminar reserva"""
    reserva = Agenda.objects.get(id = id)
    reserva.delete()
    messages.success(request, "Reserva eliminada con exito")

    return redirect('Reservar')

def anular_reserva(request, id):
    """Funcion anular reserva"""
    reserva = Agenda.objects.get(id = id)
    if reserva.Estado == "Anulada" or reserva.Estado == "anulada":
        messages.error(request, "Reserva ya se encuentra anulada")
    else:
        reserva.Estado = "Anulada"
        reserva.save()
        messages.success(request, "Reserva anulada con exito")
    return redirect('Reservar')

def confirmar_reserva(request, id):
    """Funcion anular reserva"""
    reserva = Agenda.objects.get(id = id)
    if reserva.Estado == "Confirmada" or reserva.Estado == "confirmada":
        messages.error(request, "Reserva ya se encuentra confirmada")
    else:
        reserva.Estado = "Confirmada"
        reserva.save()
        messages.success(request, "Reserva confirmada con exito")
    return redirect('Reservar')

def index(request):
    """Ruta index (base bootstrap de herencia para las paginas)"""
    return render(request, 'app/Index.html')

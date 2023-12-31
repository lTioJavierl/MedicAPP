# Generated by Django 4.2.6 on 2023-10-22 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50)),
                ('Estado', models.CharField(max_length=50)),
                ('HoraInicio', models.CharField(max_length=50)),
                ('HoraFin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50)),
                ('ValorMensual', models.CharField(max_length=50)),
                ('FechaRegistro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCiudad', models.CharField(max_length=30)),
                ('Region', models.CharField(max_length=30)),
                ('Pais', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaContrato', models.DateField()),
                ('Porcentaje', models.CharField(max_length=15)),
                ('Estado', models.CharField(max_length=50)),
                ('FechaInicio', models.DateField()),
                ('FechaFin', models.DateField()),
                ('FechaRegistro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreEspecialidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TipoFormaPago', models.CharField(max_length=50)),
                ('NombreFormaPago', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prevision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombrePrevision', models.CharField(max_length=50)),
                ('Cobertura', models.CharField(max_length=50)),
                ('Tramo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreRol', models.CharField(max_length=50)),
                ('CargoRol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreUsuario', models.CharField(max_length=50)),
                ('Contrasena', models.CharField(max_length=50)),
                ('FechaUltimoIngreso', models.DateField()),
                ('Estado', models.CharField(max_length=50)),
                ('IdRol', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RutProfesional', models.CharField(max_length=50)),
                ('Nombres', models.CharField(max_length=80)),
                ('ApellidoP', models.CharField(max_length=30)),
                ('ApellidoM', models.CharField(max_length=30)),
                ('Direccion', models.CharField(max_length=30)),
                ('Telefono', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('Tarifa', models.CharField(max_length=30)),
                ('Estado', models.CharField(max_length=50)),
                ('FechaRegistro', models.DateField()),
                ('IdCiudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.ciudad')),
                ('IdEspecialidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.especialidad')),
                ('IdUsuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RutPaciente', models.CharField(max_length=50)),
                ('Nombres', models.CharField(max_length=80)),
                ('NombreSocial', models.CharField(max_length=50)),
                ('ApellidoP', models.CharField(max_length=30)),
                ('ApellidoM', models.CharField(max_length=30)),
                ('OrdenApellido', models.BooleanField()),
                ('FechaNac', models.DateField()),
                ('Email', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=20)),
                ('Direccion', models.CharField(max_length=50)),
                ('IdCiudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.ciudad')),
                ('IdPrevision', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.prevision')),
                ('IdUsuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaHoraPago', models.DateTimeField()),
                ('Mes', models.CharField(max_length=15)),
                ('Ano', models.CharField(max_length=10)),
                ('ValorPago', models.CharField(max_length=50)),
                ('ValorCancelar', models.CharField(max_length=50)),
                ('EstadoPago', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=50)),
                ('FechaRegistro', models.DateField()),
                ('IdContrato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.contrato')),
                ('IdFormaPago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.formapago')),
                ('IdUsuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario')),
                ('RutProfesional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.profesional')),
            ],
        ),
        migrations.AddField(
            model_name='contrato',
            name='IdUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='RutProfesional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.profesional'),
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaHoraSolicitud', models.DateTimeField()),
                ('FechaAtencion', models.DateField()),
                ('Estado', models.CharField(max_length=50)),
                ('Tarifa', models.CharField(max_length=50)),
                ('IdBloque', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.bloque')),
                ('IdBox', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.box')),
                ('RutPaciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.paciente')),
                ('RutProfesional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.profesional')),
            ],
        ),
    ]

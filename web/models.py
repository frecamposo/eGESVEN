# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# class User(AbstractUser):
#     phone = models.CharField(max_length=10,unique=True, blank=True, null=True, validators=[RegexValidator(
#     regex=r"^\d{10}", message="Phone number must be 10 digits only.")])
#     address = models.TextField(max_length=50, null=True, blank=True)
#     dob = models.DateField(null=True, blank=True)
#     otp = models.CharField(max_length=6, null=True, blank=True)
#     otp_expiry = models.DateTimeField(blank=True, null=True)
#     max_otp_try = models.CharField(max_length=2, default=3)
#     otp_max_out = models.DateTimeField(blank=True, null=True)

class Categoria(models.Model):
    idcategoria = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categoria'


class Comuna(models.Model):
    idcomuna = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'comuna'


class DetalleVenta(models.Model):
    idproducto = models.OneToOneField('Productos', models.DO_NOTHING, db_column='idproducto', primary_key=True)  # The composite primary key (idproducto, idventa) found, that is not supported. The first column is selected.
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa')
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_venta'
        unique_together = (('idproducto', 'idventa'),)


class Envios(models.Model):
    idenvio = models.IntegerField(primary_key=True)
    patente = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='patente')
    idventa = models.OneToOneField('Venta', models.DO_NOTHING, db_column='idventa')
    idestado = models.ForeignKey('EstadoEnvio', models.DO_NOTHING, db_column='idestado')
    fecha_recepcion = models.DateField()
    fecha_entrega = models.DateField()
    direccion_entrega = models.CharField(max_length=120)
    fono_contacto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'envios'


class EstadoEnvio(models.Model):
    idestado = models.BooleanField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'estado_envio'


class Galeria(models.Model):
    idfoto = models.IntegerField(primary_key=True)  # The composite primary key (idfoto, idproducto) found, that is not supported. The first column is selected.
    foto = models.TextField()
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto')

    class Meta:
        managed = False
        db_table = 'galeria'
        unique_together = (('idfoto', 'idproducto'),)


class MetodoPago(models.Model):
    idmetodopago = models.BooleanField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'metodo_pago'


class Perfil(models.Model):
    idperfil = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'perfil'


class Productos(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    valoracion = models.IntegerField()
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria')

    class Meta:
        managed = False
        db_table = 'productos'


class Repartidor(models.Model):
    idrepartidor = models.IntegerField(primary_key=True)
    rut_rep = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido_pat = models.CharField(max_length=60)
    apellido_mat = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120)
    fono = models.IntegerField()
    idcomuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='idcomuna')

    class Meta:
        managed = False
        db_table = 'repartidor'


class UserPerfil(models.Model):
    fecha = models.DateField(primary_key=True)  # The composite primary key (fecha, rut, idperfil) found, that is not supported. The first column is selected.
    rut = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='rut')
    idperfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='idperfil')

    class Meta:
        managed = False
        db_table = 'user_perfil'
        unique_together = (('fecha', 'rut', 'idperfil'),)


class Usuarios(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=45)
    apellido_pat = models.CharField(max_length=50)
    apellido_mat = models.CharField(max_length=50)
    correo = models.CharField(max_length=60)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=120)
    contrasena=models.CharField(max_length=120)
    idcomuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='idcomuna')

    class Meta:
        managed = False
        db_table = 'usuarios'


class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    anio = models.IntegerField()
    kilometraje = models.IntegerField()
    capacidad_kilos = models.IntegerField()
    idrepartidor = models.ForeignKey(Repartidor, models.DO_NOTHING, db_column='idrepartidor')

    class Meta:
        managed = False
        db_table = 'vehiculo'


class Venta(models.Model):
    idventa = models.IntegerField(primary_key=True)
    subtotal = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()
    idusuario = models.FloatField()
    fecha = models.DateField()
    rut = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='rut')
    idmetodopago = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='idmetodopago')

    class Meta:
        managed = False
        db_table = 'venta'

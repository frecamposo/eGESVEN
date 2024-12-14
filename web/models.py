
from django.db import models


class Categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Comuna(models.Model):
    idcomuna = models.SmallAutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    # class Meta:
    #     managed = False
    #     db_table = 'comuna'

    def __str__(self):
        return self.descripcion
    
class DetalleVenta(models.Model):
    idproducto = models.OneToOneField('Productos', models.DO_NOTHING, db_column='idproducto', primary_key=True)  # The composite primary key (idproducto, idventa) found, that is not supported. The first column is selected.
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa')
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    total = models.IntegerField()

    # class Meta:
    #     managed = False
    #     db_table = 'detalle_venta'
    #     unique_together = (('idproducto', 'idventa'),)

class Envios(models.Model):
    idenvio = models.AutoField(primary_key=True)
    patente = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='patente')
    idventa = models.OneToOneField('Venta', models.DO_NOTHING, db_column='idventa')
    idestado = models.ForeignKey('EstadoEnvio', models.DO_NOTHING, db_column='idestado')
    fecha_recepcion = models.DateField()
    fecha_entrega = models.DateField()
    direccion_entrega = models.CharField(max_length=120)
    fono_contacto = models.IntegerField()

    # class Meta:
    #     managed = False
    #     db_table = 'envios'


class EstadoEnvio(models.Model):
    idestado = models.BooleanField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    # class Meta:
    #     managed = False
    #     db_table = 'estado_envio'


class Galeria(models.Model):
    idfoto = models.AutoField(primary_key=True)  # The composite primary key (idfoto, idproducto) found, that is not supported. The first column is selected.
    foto = models.ImageField(upload_to='galeria')
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto')

    # class Meta:
    #     managed = False
    #     db_table = 'galeria'
    #     unique_together = (('idfoto', 'idproducto'),)


class MetodoPago(models.Model):
    idmetodopago = models.BooleanField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    # class Meta:
    #     managed = False
    #     db_table = 'metodo_pago'


class Perfil(models.Model):
    idperfil = models.CharField(primary_key=True, max_length=1)
    descripcion = models.CharField(max_length=60)

    # class Meta:
    #     managed = False
    #     db_table = 'perfil'


class Productos(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='fotos',default='fotos/no-disponible.jpg')
    valoracion = models.IntegerField()
    idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='idcategoria')

    # class Meta:
    #     managed = False
    #     db_table = 'productos'


class Repartidor(models.Model):
    idrepartidor = models.AutoField(primary_key=True)
    rut_rep = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido_pat = models.CharField(max_length=60)
    apellido_mat = models.CharField(max_length=60)
    direccion = models.CharField(max_length=120)
    fono = models.IntegerField()
    idcomuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='idcomuna')

    # class Meta:
    #     managed = False
    #     db_table = 'repartidor'


class UserPerfil(models.Model):
    iduser_perfil = models.AutoField(primary_key=True)
    fecha = models.DateField()
    rut = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='rut')
    idperfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='idperfil')

    # class Meta:
    #     managed = False
    #     db_table = 'user_perfil'


class Usuarios(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=45)
    apellido_pat = models.CharField(max_length=50)
    apellido_mat = models.CharField(max_length=50)
    correo = models.CharField(max_length=60)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=120)
    contrasena = models.CharField(max_length=120)
    idcomuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='idcomuna')

    # class Meta:
    #     managed = False
    #     db_table = 'usuarios'


class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    anio = models.IntegerField()
    kilometraje = models.IntegerField()
    capacidad_kilos = models.IntegerField()
    idrepartidor = models.ForeignKey(Repartidor, models.DO_NOTHING, db_column='idrepartidor')

    # class Meta:
    #     managed = False
    #     db_table = 'vehiculo'


class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    subtotal = models.IntegerField()
    iva = models.IntegerField()
    total = models.IntegerField()
    idusuario = models.FloatField()
    fecha = models.DateField()
    rut = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='rut')
    idmetodopago = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='idmetodopago')

    # class Meta:
    #     managed = False
    #     db_table = 'venta'

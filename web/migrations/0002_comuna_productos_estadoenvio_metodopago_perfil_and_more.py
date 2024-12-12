# Generated by Django 5.1.4 on 2024-12-12 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idcomuna', models.SmallAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idproducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('foto', models.ImageField(default='fotos/no-disponible.jpg', upload_to='fotos')),
                ('valoracion', models.IntegerField()),
                ('idcategoria', models.ForeignKey(db_column='idcategoria', on_delete=django.db.models.deletion.DO_NOTHING, to='web.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoEnvio',
            fields=[
                ('idestado', models.BooleanField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('idmetodopago', models.BooleanField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('idperfil', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('idfoto', models.AutoField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(upload_to='galeria')),
                ('idproducto', models.ForeignKey(db_column='idproducto', on_delete=django.db.models.deletion.DO_NOTHING, to='web.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('idrepartidor', models.AutoField(primary_key=True, serialize=False)),
                ('rut_rep', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_pat', models.CharField(max_length=60)),
                ('apellido_mat', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=120)),
                ('fono', models.IntegerField()),
                ('idcomuna', models.ForeignKey(db_column='idcomuna', on_delete=django.db.models.deletion.DO_NOTHING, to='web.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido_pat', models.CharField(max_length=50)),
                ('apellido_mat', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=60)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=120)),
                ('contrasena', models.CharField(max_length=120)),
                ('idcomuna', models.ForeignKey(db_column='idcomuna', on_delete=django.db.models.deletion.DO_NOTHING, to='web.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='UserPerfil',
            fields=[
                ('iduser_perfil', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('idperfil', models.ForeignKey(db_column='idperfil', on_delete=django.db.models.deletion.DO_NOTHING, to='web.perfil')),
                ('rut', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.DO_NOTHING, to='web.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('anio', models.IntegerField()),
                ('kilometraje', models.IntegerField()),
                ('capacidad_kilos', models.IntegerField()),
                ('idrepartidor', models.ForeignKey(db_column='idrepartidor', on_delete=django.db.models.deletion.DO_NOTHING, to='web.repartidor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idventa', models.AutoField(primary_key=True, serialize=False)),
                ('subtotal', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('total', models.IntegerField()),
                ('idusuario', models.FloatField()),
                ('fecha', models.DateField()),
                ('idmetodopago', models.ForeignKey(db_column='idmetodopago', on_delete=django.db.models.deletion.DO_NOTHING, to='web.metodopago')),
                ('rut', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.DO_NOTHING, to='web.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Envios',
            fields=[
                ('idenvio', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_recepcion', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('direccion_entrega', models.CharField(max_length=120)),
                ('fono_contacto', models.IntegerField()),
                ('idestado', models.ForeignKey(db_column='idestado', on_delete=django.db.models.deletion.DO_NOTHING, to='web.estadoenvio')),
                ('patente', models.ForeignKey(db_column='patente', on_delete=django.db.models.deletion.DO_NOTHING, to='web.vehiculo')),
                ('idventa', models.OneToOneField(db_column='idventa', on_delete=django.db.models.deletion.DO_NOTHING, to='web.venta')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('idproducto', models.OneToOneField(db_column='idproducto', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='web.productos')),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('total', models.IntegerField()),
                ('idventa', models.ForeignKey(db_column='idventa', on_delete=django.db.models.deletion.DO_NOTHING, to='web.venta')),
            ],
        ),
    ]

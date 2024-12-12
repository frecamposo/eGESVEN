

from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='IND'),
    path('login', login,name='LOGIN'),
    path('login_admin', login_admin,name='LOGIN_A'),
    path('base', base,name='BASE'),
    path('administrador', admin,name='ADM'),
    path('grabar_producto', grabar_producto,name='GRA_PRO'),
    path('modificar_producto', modificar_producto,name='MOD_PROD'),
    path('insertar_galeria', insertar_galeria,name='IG'),
    
    path('ver_producto/<id>/', producto,name='V_PRO'),
    path('eliminar_producto/<id>/', eliminar_producto,name='ELI_PRO'),
    path('registrar_usuario/', registrar_usuario,name='REG_USU'),
    path('cerrar/',cerrar_sesion,name='CS'),
    path('agregar_carrito/<id>/', agregar_carrito,name='AG_CAR'),
    path('agregar_carrito_cant/<id>/<cant>/', agregar_carrito_cant,name='AG_CAR_C'),    
    
    path('vaciar_carrito/', vaciar_carro,name='VACIAR_CARRO'),
]

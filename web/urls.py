

from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='IND'),
    path('login', login,name='LOGIN'),
    path('login_admin', login_admin,name='LOGIN_A'),
    path('base', base,name='BASE'),
    path('administrador', admin,name='ADM'),
    path('grabar_producto', grabar_producto,name='GRA_PRO'),
    path('eliminar_producto/<id>/', eliminar_producto,name='ELI_PRO'),
    path('registrar_usuario/', registrar_usuario,name='REG_USU'),
    path('cerrar/',cerrar_sesion,name='CS'),

]

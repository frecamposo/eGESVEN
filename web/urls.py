

from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='IND'),
    path('login', login,name='LOGIN'),
    path('base', base,name='BASE'),
    path('administrador', admin,name='ADM'),
    path('grabar_producto', grabar_producto,name='GRA_PRO'),
    path('eliminar_producto/<id>/', eliminar_producto,name='ELI_PRO'),
]

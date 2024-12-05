

from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='IND'),
    path('login', login,name='LOGIN'),
]

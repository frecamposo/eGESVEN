from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as login_aut,logout
from django.contrib.auth.decorators import login_required,permission_required
from .models import *
from django.contrib.auth.models import User
import requests

def index(request):
    return render(request,'index.html')

def login(request):
    contexto={}
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    if request.method == 'POST':
        usuario= request.POST.get('txtUsuario')
        correo= request.POST.get('txtCorreo')        
        try:
            sql="select u.rut,u.nombre,u.apellido_pat,u.correo,p.idperfil from usuarios u inner join user_perfil up on up.rut = u.rut inner join perfil p on up.idperfil = p.idperfil where u.nombre='"+usuario+"' and u.correo='"+correo+"'  "
            # usu=Usuarios.objects.get(nombre=usuario,correo=correo)
            print(sql)
            usuarios= Usuarios.objects.raw(sql)
            x=0
            for u in usuarios:
                print(u.rut)
                x=u.idperfil
            if x==0:
                contexto["mensaje"]="No Existe"
            else:    
                contexto["mensaje"]=""
                if int(x)==1:
                    datos=Productos.objects.all()
                    contexto["data"]=datos
                    print(datos)
                    return render(request, "admin.html",contexto)
        except  BaseException as error:
            contexto["mensaje"]=error
    return render(request,'login.html',contexto)

def base(request):
    return render(request,'base.html')

def admin(request):
    return render(request,'admin.html')

def grabar_producto(request):
    contexto={}
    datos=Productos.objects.all()
    contexto["data"]=datos
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    if request.method == 'POST':
        print("aqui")
        try:
            prod=Productos()
            prod.idproducto=request.POST.get('codigo')
            prod.nombre=request.POST.get('nombre')
            prod.descripcion=request.POST.get('descripcion')
            prod.precio=request.POST.get('precio')
            cat= Categoria.objects.get(idcategoria=request.POST.get('catego'))
            prod.idcategoria=cat
            prod.stock=request.POST.get('stock')
            prod.valoracion=0
            try:
                prod.save()
                contexto["mensaje"]="Grabo Producto"            
            except BaseException as error:
                contexto["mensaje"]=error
        except BaseException as error:
            contexto["mensaje"]=error                        
    return render(request,'admin.html',contexto)

def eliminar_producto(request,id):
    contexto={}
    try:
        pro=Productos.objects.get(idproducto=id)
        pro.delete()
        contexto["mensaje"]="Elimio Reg"
        datos=Productos.objects.all()
        contexto["data"]=datos
        categorias=Categoria.objects.all()
        contexto["categorias"]=categorias        
    except BaseException as error:
        contexto["mensaje"]=error
    return render(request,'admin.html',contexto)
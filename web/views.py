from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as login_aut,logout
from django.contrib.auth.decorators import login_required,permission_required
from .models import *
from django.contrib.auth.models import User,Group
import requests
from django.contrib.auth.hashers import make_password,check_password
from datetime import datetime
import asyncio

from geopy.geocoders import Nominatim

def lugar(request):
   contexto={}
   dire=''
   try:
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
        if request.method=='POST':
            dire=request.POST.get('lugar')
            location = geolocator.geocode(dire)
        print(location.latitude, location.longitude)
        contexto["pos"]={"lat":location.latitude,"lng":location.longitude}
        contexto["direccion"]=dire
   except BaseException as error:
       contexto["mensaje"]="no se ubico la direccion, ingresela nuevamente"
   return render(request,"pedido.html",contexto)


def vaciar_carro(request):
    if  'carrito' in request.session:
        del request.session['carrito']
        del request.session['total']

    contexto={}
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    productos= Productos.objects.all()
    contexto["productos"]=productos
    return render(request,'index.html',contexto)
  
  
def agregar_carrito_cant(request,id,cant):
    if "carrito" in request.session:
        lista= request.session.get("carrito",[])
        total= request.session.get("total")
    else:
        lista= []
        total={"cantidad":0,"total":0}
    reg= Productos.objects.get(idproducto=id)
    dato={
        "id":reg.idproducto,"nombre":reg.nombre,"precio":reg.precio,"imagen":reg.foto.url
    }
    sub_total= total["total"]+reg.precio
    cant_total = total["cantidad"]+cant
    total={"cantidad":cant_total,"total":sub_total}
    request.session["total"]=total
    lista.append(dato)     
    request.session["carrito"]=lista
    
    lista_recuperada=request.session.get('carrito',[])
    contexto={}
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    productos= Productos.objects.all()
    contexto["productos"]=productos
    contexto["carrito"]=lista_recuperada
    contexto["total"]=request.session.get('total')
    return render(request,'index.html',contexto)
           

def agregar_carrito(request,id):
    if "carrito" in request.session:
        lista= request.session.get("carrito",[])
        total= request.session.get("total")
    else:
        lista= []
        total={"cantidad":0,"total":0}
    reg= Productos.objects.get(idproducto=id)
    dato={
        "id":reg.idproducto,"nombre":reg.nombre,"precio":reg.precio,"imagen":reg.foto.url
    }
    sub_total= total["total"]+reg.precio
    cant_total = total["cantidad"]+1
    total={"cantidad":cant_total,"total":sub_total}
    request.session["total"]=total
    lista.append(dato)     
    request.session["carrito"]=lista
    
    lista_recuperada=request.session.get('carrito',[])
        
    contexto={}
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    productos= Productos.objects.all()
    contexto["productos"]=productos
    contexto["carrito"]=lista_recuperada
    contexto["total"]=request.session.get('total')
    return render(request,'index.html',contexto)
    
def index(request):    
    lista_recuperada=request.session.get('carrito',[])
    contexto={}
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    productos= Productos.objects.all()
    contexto["productos"]=productos
    contexto["carrito"]=lista_recuperada
    return render(request,'index.html',contexto)

def login(request):
    contexto={}
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    productos= Productos.objects.all()
    contexto["productos"]=productos
    if request.method == 'POST':
        usuario= request.POST.get('txtUsuario')
        correo= request.POST.get('txtCorreo')        
        pass1=request.POST.get('txtPassword')
        try:
            sql="select u.rut,u.nombre,u.apellido_pat,u.correo,p.idperfil,u.contrasena from web_usuarios u inner join web_userperfil up on up.rut = u.rut inner join web_perfil p on up.idperfil = p.idperfil where u.nombre='"+usuario+"' and u.correo='"+correo+"' "
            # usu=Usuarios.objects.get(nombre=usuario,correo=correo)
            usu=Usuarios.objects.get(nombre=usuario,correo=correo)
            print("aqui va")
            print(usu)
            print(sql)
            usuarios= Usuarios.objects.raw(sql)
            x=0
            p=''
            for u in usuarios:
                x=u.idperfil
                p=u.contrasena
            if check_password(pass1, p):
                print("La contraseña es válida")
            else:
                print("La contraseña no es válida")
                x=0
            if x==0:
                contexto["mensaje"]="No Existe"
            else:    
                contexto["mensaje"]=""
                if x=='U':
                    datos=Productos.objects.all()
                    contexto["data"]=datos
                    print(datos)
                    
                    user = authenticate(request,username=usuario,password=pass1)            
                    request.session["perfil"]='Usuario'
                    login_aut(request,user)
                    
                    return render(request, "index.html",contexto)
        except  BaseException as error:
            contexto["mensaje"]=error
    return render(request,'login.html',contexto)

def base(request):
    return render(request,'base.html')

def admin(request):
    contexto={}
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    productos= Productos.objects.all()
    contexto["data"]=productos    
    return render(request,'admin.html',contexto)

def modificar_producto(request):
    contexto={}
    productos= Productos.objects.all()
    contexto["productos"]=productos    
    datos=Productos.objects.all()
    contexto["data"]=datos
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    if request.method == 'POST':
        print("aqui")
        try:
            prod=Productos.objects.get(idproducto=request.POST.get('mod_codigo'))
            prod.nombre=request.POST.get('mod_nombre')
            prod.descripcion=request.POST.get('mod_descripcion')
            prod.precio=request.POST.get('mod_precio')
            cat= Categoria.objects.get(idcategoria=request.POST.get('mod_catego'))
            prod.idcategoria=cat
            prod.stock=request.POST.get('mod_stock')
            ima  = request.FILES.get("mod_foto")
            if ima is not None:
                prod.foto= ima
            prod.valoracion=0
            try:
                prod.save()
                contexto["mensaje"]="Modificar Producto"            
            except BaseException as error:
                contexto["mensaje"]=error
        except BaseException as error:
            contexto["mensaje"]=error                        
    return render(request,'admin.html',contexto)


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
            prod.nombre=request.POST.get('nombre')
            prod.descripcion=request.POST.get('descripcion')
            prod.precio=request.POST.get('precio')
            cat= Categoria.objects.get(idcategoria=request.POST.get('catego'))
            prod.idcategoria=cat
            prod.stock=request.POST.get('stock')
            ima  = request.FILES.get("foto")
            if ima is not None:
                prod.foto= ima
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

def registrar_usuario(request):
    contexto={}
    comuna=Comuna.objects.all()
    contexto["comunas"]=comuna
    per=Perfil.objects.get(descripcion='Usuario')
    if request.method == 'POST':
        try:
            reg=Usuarios()
            reg.rut=request.POST.get('rut')
            reg.dv=request.POST.get('dv')
            reg.nombre=request.POST.get('nombre')
            reg.apellido_pat=request.POST.get('appaterno')
            reg.apellido_mat=request.POST.get('apmaterno')
            reg.correo=request.POST.get('correo')
            reg.direccion=request.POST.get('direccion')
            reg.telefono=request.POST.get('telefono')
            hashed_password = make_password(request.POST.get('pass1'))
            reg.contrasena=hashed_password
            comuna = Comuna.objects.get(idcomuna=request.POST.get('comuna'))
            reg.idcomuna=comuna
            try:
                reg.save()
                contexto["mensaje"]="Grabo Usuario"
                up=UserPerfil()
                up.fecha=datetime.now()
                up.rut=reg
                per=Perfil.objects.get(idperfil='U')
                up.idperfil=per
                up.save()    
                try:
                    us= User()
                    us.username=request.POST.get('nombre')
                    us.first_name=request.POST.get('appaterno')
                    us.last_name=request.POST.get('apmaterno')
                    us.email= request.POST.get('correo')
                    us.set_password(request.POST.get('pass1'))
                    us.save()
                    
                    grupo = Group.objects.get(name='usuarios')
                    us.groups.add(grupo)
                    contexto["mensaje"]="usuario Grabado"
                except:
                    contexto["mensaje"]="problemas al grabar el usuario, revise sus datos"        
            except BaseException as error:
                contexto["mensaje"]=error
        except BaseException as error:
            contexto["mensaje"]=error                       
    return render(request,'registrar_usuario.html',contexto)

@login_required(login_url='/login/')
def cerrar_sesion(request):
    contexto={}
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    productos= Productos.objects.all()
    contexto["productos"]=productos
    logout(request)
    return render(request, 'index.html',contexto)

def login_admin(request):
    contexto={}
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request,username=usuario,password=password)
        print("usuario:",usuario)
        print("pass",password)
        if user is not None:
            datos=Productos.objects.all()
            contexto["data"]=datos
            categorias=Categoria.objects.all()
            contexto["categorias"]=categorias
            request.session["perfil"]='Administrador'
            login_aut(request,user)
            return render(request,'admin.html',contexto)
        else:
            contexto["mensaje"]="usuario o Contraseña Incorrecta"
    return render(request, 'login_admin.html',contexto)

def insertar_galeria(request):
    contexto={}
    categorias=Categoria.objects.all()
    contexto["categorias"]=categorias
    productos= Productos.objects.all()
    contexto["data"]=productos    
    
    if request.POST:
        img_codigo = request.POST.get("img_codigo")
        prod= Productos.objects.get(idproducto=img_codigo)
        foto = request.FILES.get("img_foto")

        gale = Galeria()
        gale.foto = foto
        gale.idproducto = prod
        gale.save()
        
        contexto["mensaje"] = "Agrego Imagen para "+prod.nombre
    return render(request,'admin.html',contexto)

def producto(request,id):
    contexto={}
    categorias=Categoria.objects.all()
    pro=Productos.objects.get(idproducto=id)
    fotos= Galeria.objects.filter(idproducto=pro)
    
    contexto["categorias"]=categorias
    contexto["fotos"]=fotos
    contexto["producto"]=pro
    return render(request,'producto.html',contexto)

def realizar_pedido(request):
    return render(request,"pedido.html")
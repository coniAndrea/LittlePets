from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from django.contrib import messages
from .serializers import ProductosSerializer, MarcaSerializer

# Create your views here.

class MarcaViewset(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        return productos    

def home(request):
    productos = Producto.objects.all()
    data ={
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def login(request):
    return render(request, 'app/login.html')    

def registro(request):    
     return render(request, 'app/registration/registro.html')

def alimento(request):    
     return render(request, 'app/alimento.html')    

def servicios(request):    
     return render(request, 'app/servicios.html')    

def agregar_producto(request):
     
    data={
        'form':ProductoForm()
       }
     
    if request.method == 'POTS':
        formulario = ProductoForm(data=request.POTS, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "producto registrado")
        else:
            data['form'] = formulario

    return render(request,'app/crud_producto/agregar.html', data)


def listar_producto(request):

    productos = Producto.objects.all()

    data ={
        'productos': productos
    }
    
    return render(request,'app/crud_producto/listar.html',data)

def modificar_producto(request, id):
    producto = Producto.objects.get(id=id)

    data ={
        'form':ProductoForm(instance=Producto)
    }
    if request.method == 'POST':
       formulario = ProductoForm(data=request.POST, intance=Producto, files=request.FILES)
       if formulario.is_valid():
          formulario.save()
          messages.success(request,"Modificado Correctamente")
          return redirect(to="listar_producto") 
          
          data['form']=formulario

   
    return render(request,'app/crud_producto/modificar.html',data)

def eliminar_producto(request,id):
   producto =Producto.objects.get(id=id)    
   producto.delete()
   messages.success(request, "Eliminado Correctamente")  
   return redirect(to="listar_producto")

# REGISTRO

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method =='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user =authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Te has registrado correctamente")
            return redirect (to="home")
        data['form']=formulario    
    return render(request,'registration/registro.html', data)  
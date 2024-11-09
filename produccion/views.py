from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from produccion.models import Tareas
from django.contrib import messages
from .models import ProductoA, ProductoB, ProductoC
# Create your views here.


def IniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.html', {"form": AuthenticationForm, "error": "Usuario o contraseña no es invalido."})

        login(request, user)
        return redirect('form_tarea')


@login_required
def Form_tareas(request):
    if request.method =="POST":
        tarea = Tareas()

        tarea.fecha= request.POST.get("fecha")
        tarea.hora_inicio= request.POST.get("horaInicio")
        tarea.linea = request.POST.get('linea')
        tarea.producto = request.POST.get("producto")
        tarea.trabajadores= request.POST.get("trabajadores")
        tarea.producto_terminado= request.POST.get("productoTerminado")
        tarea.und_producidas= request.POST.get("undProducidas")
        tarea.rotulo_fecha_fecha1= request.POST.get("fecha1")
        tarea.rotulo_fecha_fecha2= request.POST.get("fecha2")
        tarea.hora_termino= request.POST.get("horaTermino")
        tarea.cantidad= request.POST.get("cantidad")
        
        tarea.save()
        messages.success(request, ".")

        return render(request, "form_tareas.html")
    
    productos_a = ProductoA.objects.filter()
    productos_b = ProductoB.objects.filter()
    productos_c = ProductoC.objects.filter()
    return render(request, 'form_tareas.html', {'productos_a': productos_a,'productos_b':productos_b,'productos_c':productos_c})
    

@login_required    
def Ver_tareas(request):
    tarea = Tareas.objects.filter().order_by('-fecha')

    date= {
        'date': tarea,
    }

    return render(request, 'tareas.html', date)


@login_required
def Salir(request):
    logout(request)
    return redirect('iniciarSesion')



# agregar productos
@login_required
def agregar_productos(request):
    if request.method == 'POST':
        nombre_a = request.POST.get('nombre_a')
        nombre_b = request.POST.get('nombre_b')
        nombre_c = request.POST.get('nombre_c')

        if nombre_a:
            ProductoA.objects.create(nombre=nombre_a)
        if nombre_b:
            ProductoB.objects.create(nombre=nombre_b)
        if nombre_c:
            ProductoC.objects.create(nombre=nombre_c)

        return redirect('agregar_productos')

    productos_a = ProductoA.objects.all()
    productos_b = ProductoB.objects.all()
    productos_c = ProductoC.objects.all()
    return render(request, 'agregar_productos.html', {'productos_a': productos_a, 'productos_b': productos_b, 'productos_c': productos_c})

def eliminar_producto(request, tipo, id):
    if request.method == 'POST':
        if tipo == 'a':
            ProductoA.objects.filter(id=id).delete()
        elif tipo == 'b':
            ProductoB.objects.filter(id=id).delete()
        elif tipo == 'c':
            ProductoC.objects.filter(id=id).delete()
    return redirect('agregar_productos')
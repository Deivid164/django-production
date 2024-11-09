"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from produccion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('https://arturo-product.netlify.app/', views.IniciarSesion, name='iniciarSesion'),
    path('tareas/', views.Ver_tareas, name='tareas'),
    path('form_tareas/', views.Form_tareas, name='form_tarea'),
    path('logout/', views.Salir, name='logout'),

    path('agregar/', views.agregar_productos, name='agregar_productos'),
    path('eliminar_producto/<str:tipo>/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]

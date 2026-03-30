from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), # Ruta para la administración del sitio
    path('', views.home, name='home'), # Ruta para la vista principal home
    path('categoria/', include('categoria.urls')),# Incluye las rutas definidas en la aplicación categoria
    path('producto/', include('producto.urls')),# Incluye las rutas definidas en la aplicación producto
    path('registrarse/', views.registrarse, name='registrarse'), # Ruta para la vista de registro de usuarios
    path('login/', views.login, name='login'),# Ruta para la vista de inicio de sesión
    path('logout/', views.logout, name='logout'), # Ruta para la vista de cierre de sesión
    
]

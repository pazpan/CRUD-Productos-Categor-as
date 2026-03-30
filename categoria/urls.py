from django.urls import path
from . import views

urlpatterns = [
    path('',views.CategoriaL, name="categoria"),# Ruta para la vista que lista las categorías
    path('Guardar_categoria/', views.Guardar_categoria), # Ruta para la vista que guarda una nueva categoría
    path('Editar_categoria/<id_categoria>', views.Editar_categoria,name='Editar_categoria'), # Ruta para la vista que edita una categoría existente, pasando el ID de la categoría como parámetro
    path('Eliminar_categoria/<id_categoria>', views.Eliminar_categoria,name='Eliminar_categoria'),# Ruta para la vista que elimina una categoría existente, pasando el ID de la categoría como parámetro

]

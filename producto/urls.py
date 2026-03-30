from django.urls import path

from . import views


urlpatterns = [
    path('',views.ProductoL, name="producto"), # Ruta para la vista que lista los productos
    path('Guardar_producto/', views.Guardar_producto), # Ruta para la vista que guarda un nuevo producto
    path('Editar_producto/<id_producto>', views.Editar_producto,name='Editar_producto'), # Ruta para la vista que edita un producto existente, pasando el ID del producto como parámetro
    path('Eliminar_producto/<id_producto>', views.Eliminar_producto,name='Eliminar_producto'),  # Ruta para la vista que elimina un producto existente, pasando el ID del producto como parámetro
]

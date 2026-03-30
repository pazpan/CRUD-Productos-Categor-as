from django.db import models

from categoria.models import Categoria

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)  # Campo ID autoincremental 
    nombre = models.CharField(max_length=20) # Campo nombre para almacenar el nombre del producto con una longitud máxima de 20 caracteres

    precio = models.IntegerField(default=0) # Campo precio para almacenar el precio del producto, con valor por defecto de 0
    stock = models.IntegerField(default=0)  # Campo stock para almacenar la cantidad de productos disponibles, con valor por defecto de 0
    creado_en = models.DateTimeField(auto_now_add=True)  # Campo creado_en que almacena la fecha y hora en la que se creó el producto, se establece automáticamente al crear el registro
    actualizado_en = models.DateTimeField(auto_now=True)  # Campo actualizado_en que almacena la fecha y hora en la que se actualizó el producto por última vez, se actualiza automáticamente al guardar el registro
     # Relación con el modelo Categoria, indica que cada producto pertenece a una categoría
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE) # on_delete=models.CASCADE asegura que si se elimina una categoría, también se eliminarán sus productos asociados
    
    
    def __str__(self):
        return self.nombre # Devuelve el nombre del producto al convertir el objeto a cadena
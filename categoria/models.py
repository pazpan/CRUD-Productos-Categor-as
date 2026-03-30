from django.db import models

# Definición del modelo Categoria
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True) # Campo ID autoincremental
    nombre = models.CharField(max_length=20) # Campo nombre con longitud máxima de 20 caracteres
    descripcion = models.CharField(max_length=20)  # Campo descripción con longitud máxima de 20 caracteres

    def __str__(self): # Devuelve el nombre de la categoría al convertir el objeto a cadena
        return self.nombre
    
    

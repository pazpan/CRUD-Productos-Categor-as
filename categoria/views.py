from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from categoria.models import Categoria


# Función para listar categorías
def CategoriaL(request):
    try:
        categorias=Categoria.objects.all()
        return render(request,'categoria.html',
                    context={'categorias':categorias}
                    )
    except Exception as e:# Si ocurriese un error al obtener las categorías, muestra un mensaje de error
            messages.error(request, e)
    
    
# Función para guardar una nueva categoría
def Guardar_categoria(request):
    try:
        if request.method == 'POST':
            nombre = request.POST['nombre']
            descripcion = request.POST['descripcion']
            
            # Crea una nueva categoría con los datos del formulario
            categoria = Categoria.objects.create(nombre=nombre, descripcion=descripcion)
            # Muestra un mensaje de éxito después de guardar la categoría
            messages.success(request, '¡Categoría guardada correctamente!')
            return redirect('/categoria')  # Redirige a la lista de categorías
    except Exception as e:
        # Si ocurre un error al guardar la categoría, muestra un mensaje de error
        messages.error(request, f"No se pudo guardar la categoría: {e}")
    return render(request, 'guardar_categoria.html')
   
    
# Función para editar una categoría existente 
def Editar_categoria(request,id_categoria):
    try:
        if request.method =="POST":
            nombre=request.POST['nombre']
            descripcion=request.POST['descripcion']
        
            # Obtiene la categoría existente por su ID y actualiza los campos    
            categoria=Categoria.objects.get(id_categoria=id_categoria)
            categoria.nombre=nombre
            categoria.descripcion=descripcion

            categoria.save() # Guarda los cambios en la base de datos
            
            # Muestra un mensaje de éxito después de actualizar la categoría
            messages.success(request,"!Categoria actualizada correctamente¡")
            return redirect("/categoria")
        
    except Exception as e: # Si ocurre un error al actualizar la categoría, muestra un mensaje de error
            messages.error(request, f"No se pudo actualizar la categoria: {e}")
  
    # Obtiene la categoría para mostrar en el formulario de edición
    categorias = Categoria.objects.get(id_categoria=id_categoria)
    return render(request,'editar_categoria.html',context={'categorias':categorias})

    
    
    
    
# Función para eliminar una categoría
def Eliminar_categoria(request, id_categoria):
    try:
        # Obtiene la categoría por su ID y la elimina de la base de datos
        categoria = Categoria.objects.get(id=id_categoria)
        categoria.delete()  # Elimina la categoría
        # Muestra un mensaje de éxito después de eliminar la categoría
        messages.success(request, '¡Categoría eliminada correctamente!')
        return redirect('/categoria')  # Redirige a la lista de categorías
    except Exception as e:
        # Si ocurriera un error al eliminar la categoría, muestraria un mensaje de error
        messages.error(request, f"No se pudo eliminar la categoría: {e}")
        return redirect('/categoria')  # Redirige a la lista de categorías en caso de error

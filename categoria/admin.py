from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display =('id_categoria','nombre','descripcion')
    
admin.site.register(Categoria, CategoriaAdmin)


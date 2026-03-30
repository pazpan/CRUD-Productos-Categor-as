from django.contrib import admin
from .models import Producto
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display =('id_producto','nombre','precio','stock','creado_en','actualizado_en','categoria')

admin.site.register(Producto,ProductoAdmin)
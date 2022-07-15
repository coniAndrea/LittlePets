from django.contrib import admin
from .models import Marca, Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    search_fields = ["nombre"]
    list_filter = ["nuevo"]
    list_per_page = 5

class MarcaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]
    search_fields = ["nombre"]
   
    list_per_page = 5

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)

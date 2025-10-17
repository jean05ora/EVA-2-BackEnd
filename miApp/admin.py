from django.contrib import admin
from .models import Polera, Fragancia

# Register your models here.
class PoleraADM(admin.ModelAdmin):
    list_display = ('id', 'nombre_polera', 'precio_polera', 'stock_polera')

class FraganciaADM(admin.ModelAdmin):
    list_display = ('id', 'nombre_fragancia', 'precio_fragancia', 'stock_fragancia')

admin.site.register(Polera, PoleraADM)
admin.site.register(Fragancia, FraganciaADM)

from django.shortcuts import render
from .models import Polera, Fragancia

def main(request):
    return render(request, "main.html")

def poleras(request):
    context = {}

    poleras = Polera.objects.all

    context['poleras'] = poleras

    return render(request,"poleras.html", context)

def fragancias(request):
    context = {}

    fragancias = Fragancia.objects.all

    context['fragancias'] = fragancias

    return render(request,"fragancias.html", context)

def detalles_productos(request, id):
    context = {}

    poleras = Polera.objects.get(id=id)
    fragancias = Fragancia.objects.get(id=id)

    context['poleras'] = poleras 
    context['fragancias'] = fragancias

    return render(request, "detalles_producto.html", context)
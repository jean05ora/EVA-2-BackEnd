from django.shortcuts import render
from .models import Polera, Fragancia

def index(request):
    return render(request, "index.html")

def generic(request):
    return render(request, "generic.html")

def elements(request):
    return render(request, "elements.html")

####
######
#######

def main(request):
    return render(request, "main.html")

def categorias(request):
    context = {}
    polera = Polera.objects.all()
    fragancia = Fragancia.objects.all()

    context['polera'] = polera
    context['fragancia'] = fragancia

    return render(request, "categorias.html", context)

def poleras(request):
    context = {}

    polera = Polera.objects.all()

    context['polera'] = polera

    return render(request,"poleras.html", context)

def fragancias(request):
    context = {}

    fragancia = Fragancia.objects.all()

    context['fragancia'] = fragancia

    return render(request,"fragancias.html", context)

def detalles_productos(request, id):
    context = {}

    polera = Polera.objects.filter(id=id).first()
    fragancia = Fragancia.objects.filter(id=id).first()

    context['polera'] = polera
    context['fragancia'] = fragancia

    return render(request, "detalles_producto.html", context)
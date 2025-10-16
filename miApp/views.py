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

def detalles_fragancia(request, id):
    context = {}

    fragancia = Fragancia.objects.get(id=id)

    context['fragancia'] = fragancia

    return render(request, "detalles_fragancia.html", context)

def detalles_polera(request, id):
    context = {}

    polera = Polera.objects.get(id=id)

    context['polera'] = polera

    return render(request, "detalles_polera.html", context)
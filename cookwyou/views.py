from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from urllib.parse import urlencode 
from .models import Receta




def index(request):

    if request.method == "POST":
        nombre = request.POST['nombre']
        mail = request.POST['mail']
        mensaje = request.POST['mensaje']
        insert = Receta(nombre=nombre, mail=mail, mensaje=mensaje)
        insert.save()

    return render(request, "index.html")
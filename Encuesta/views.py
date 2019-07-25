from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from Encuesta.models import Persona
from Encuesta.models import Vehiculo

# Create your views here.

def Listar_Personas(request):
    listado = ""
    for q in Persona.objects.all():
        listado += "<li>%s</li>" % q
        
    respuesta = """
            <html><body><h1>Personas</h1>
            <ul>%s</ul>
            </body></html>"""
    return HttpResponse(respuesta % listado)

#CON EL USUARIO DE DJANGO VIENE EN EL REQUEST

def Listar_Autos(request):
    listado = Vehiculo.objects.all()
    return render_to_response("Autos.html",{'listado':listado,'usuario':request.user})
    #for q in Vehiculo.objects.filter(request)
    #    if 
    


            
            
        
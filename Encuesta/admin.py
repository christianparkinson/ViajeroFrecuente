from django.contrib import admin
from Encuesta.models import Persona, Vehiculo,Marca,Localidad,Direccion,Provincia,Viaje

admin.site.register(Marca)
admin.site.register(Persona)
admin.site.register(Vehiculo)
admin.site.register(Localidad)
admin.site.register(Provincia)
admin.site.register(Direccion)
admin.site.register(Viaje)

# Register your models here.

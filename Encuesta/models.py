from django.db import models
class CuentaCorriente(models.Model):
    credito = models.IntegerField()
    
    def acreditar(self, importe):
        self.credito = self.credito + importe
    
    def debitar(self,importe):    
        self.credito = self.credito - importe

# Create your models here.
class Persona(models.Model):
        nombre = models.CharField(max_length=100)
        apellido = models.CharField(max_length=100)
        dni = models.CharField(max_length=8)
        cuenta = models.ForeignKey(CuentaCorriente,on_delete=models.CASCADE)
        puntos = models.IntegerField()        
        cantidadvotantes = models.IntegerField()
            
        def __str__(self):
            return self.nombre + ' ' + self.apellido
        
        def calificar(self, calificacion):
            self.puntos = self.puntos +  calificacion
            self.cantidadvotantes = self.cantidadvotantes +1
       
        def obtenerpuntaje(self):
            return self.puntos / self.cantidadvotantes        
        
class Credencial(models.Model):
        username = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
        
        def __str__(self):
            return self.username
               
        
class Usuario(models.Model):
        credencial = models.ForeignKey(Credencial,on_delete=models.CASCADE)
        
        persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
        
        def login(self, credencial):  
            if self.credencial.usuario == credencial.usuario:
                pass
                                         
class Provincia(models.Model):
        provincia=models.CharField(max_length=100)
        
class Localidad(models.Model):   
        localidad = models.CharField(max_length=100)
        provincia= models.ForeignKey(Provincia,on_delete=models.CASCADE)
        
class Direccion(models.Model):
        localidad = models.ForeignKey(Localidad,on_delete=models.CASCADE)
        altura = models.IntegerField()
        direccion = models.CharField(max_length=100)
        
class Marca(models.Model):   
        marca = models.CharField(max_length=100)
        modelo = models.CharField(max_length=100)
        def __str__(self):
            return self.marca + ' ' + self.modelo
             
class Vehiculo(models.Model):
        modelo = models.ForeignKey(Marca,on_delete=models.CASCADE)    
        patente = models.CharField(max_length =8)
        color  = models.CharField(max_length=20)
        cupo = models.IntegerField()
        
        def __str__(self):
            return self.patente + ' ' + self.modelo.marca + ' ' + self.modelo.modelo
        
class Chofer(Persona):
        licencia = models.IntegerField()
        vehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE) 

class EstadoViaje(models.Model):
    descripcion = models.CharField(max_length=20)
    
    def __str__(self):
            return self.descripcion 
 
        
class Viaje(models.Model):
        vehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
        chofer = models.ForeignKey(Chofer,on_delete=models.CASCADE)
        origen = models.ForeignKey(Direccion,on_delete=models.CASCADE,related_name='viajes_desde')  
        destino  = models.ForeignKey(Direccion,on_delete=models.CASCADE,related_name='viajes_hasta')              
        costo  = models.FloatField()
        estado = models.ForeignKey(EstadoViaje, on_delete=models.CASCADE, related_name='estado_viaje')
        pasajeros = models.ManyToManyField(Persona,related_name='pasajeros_viajes')
                       
        def agregarpasajero(self, persona):
            if self.vehiculo.cupo < len(self.pasajeros):
                if persona.cuenta.credito >= self.obtenerimportesiguiente():
                    self.pasajeros.append(Persona)
        
        def obtenercantidadpasajeros(self):
            return len(self.pasajeros)
        
        def obtenerimporte(self):
            return self.costo / len(self.pasajeros)
           
        def obtenerimportesiguiente(self):
            return self.costo / (len(self.pasajeros) +1 )   
                
        def finalizarviaje(self, estadofinalizado):
            self.estado = estadofinalizado
            
            for p in self.pasajeros:
                p.cuenta.debitar(self.obtenerimporte())
            
            self.chofer.cuenta.acreditar(self.costo)
        
        
class Calificacion(models.Model):
    evaluador = models.ForeignKey(Persona,on_delete=models.CASCADE, related_name='persona_evaluadora')
    evaluado = models.ForeignKey(Persona,on_delete=models.CASCADE,related_name='persona_evaluada')
    viaje = models.ForeignKey(Viaje,on_delete=models.CASCADE)
        
    def calificar(self,numero):
        if numero > 0 and numero <= 5:
            self.evaluado.calificar(numero)
        else:
            print ('el rango especificado no es valido')              
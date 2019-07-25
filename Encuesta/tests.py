from Encuesta.models import Chofer,Persona,Viaje,Vehiculo,CuentaCorriente,Calificacion
from django.test import TestCase
from doctest import TestClass

class CuentaCorrienteTest(TestCase):
    def setUp(self):
        cuenta = CuentaCorriente()
        cuenta.credito=300

    def test_initialize(self):
        self.assertEqual(self.cuenta.credito,300)
    
    def test_debitar(self):
        self.cuenta.debitar(100)
        self.assertEqual(self.cuenta.credito,200)

    def test_acreditar(self):
        self.cuenta.acreditar(100)
        self.assertEqual(self.cuenta.credito,300)

class ChoferTest(TestCase):

    def setUp(self):
        chofer = Chofer()
        chofer.nombre="Christian"
        chofer.apellido="Parkinson"
        chofer.dni="28644150"
        chofer.cantidadvotantes = 5
        chofer.puntos = 25
    
    def test_initialize(self):
        self.assertEqual(self.chofer.puntos,25)
        self.assertEqual(self.chofer.cantidadvotantes,5)
        
    def test_Calificar(self):
        self.chofer.Calificar(5)
        self.assertEqual(self.chofer.puntos,30)    
        self.assertEqual(self.chofer.cantidadvotantes,6)
        
    def test_ObtenerPuntaje(self):
        self.assertEqual(self.chofer.obtenerpuntaje(), 5)
        
class PersonaTest(TestCase):

    def setUp(self):
        persona = Persona()
        persona.nombre="Christian"
        persona.apellido="Parkinson"
        persona.dni="28644150"
        persona.cantidadvotantes = 5
        persona.puntos = 25

    
    def test_initialize(self):
        self.assertEqual(self.persona.cantidadViajes,0)
       

    def test_calificar(self):
        self.chofer.calificar(5)
        self.assertEqual(self.chofer.puntos,30)    
        self.assertEqual(self.chofer.cantidadvotantes,6)


class ViajeTest(TestCase):
    def setUp(self):
        viaje=Viaje()
        viaje.chofer = Chofer()
        viaje.vehiculo = Vehiculo()
        viaje.costo =100
        
        
    def test_agregarpasajero(self):
        persona = Persona()
        persona.cuenta.credito = 110
        self.test_agregarpasajero(persona)
        self.assertEqual(self.viaje.obtenercantidadpasajeros,1)
        
        persona = Persona()
        persona.cuenta.credito = 300
        self.test_agregarpasajero(persona)
        self.assertEqual(self.viaje.obtenercantidadpasajeros,2)        
        
        persona = Persona()
        persona.cuenta.credito = 75        
        self.test_agregarpasajero(persona)
        self.assertEqual(self.viaje.obtenercantidadpasajeros,3)
       
        persona = Persona()
        persona.cuenta.credito = 4        
        self.test_agregarpasajero(persona)
        self.assertEqual(self.viaje.obtenercantidadpasajeros,3)
       
        persona = Persona()
        persona.cuenta.credito = 110
        self.test_agregarpasajero(persona)
        self.assertEqual(self.viaje.obtenercantidadpasajeros,4)    
        
        persona = Persona()
        persona.cuenta.credito = 160
        self.test_agregarpasajero(persona)
        self.assertEqual(self.viaje.obtenercantidadpasajeros,4)     
                
    def test_obtenerimporte(self):
        self.assertEqual(self.viaje.obtenerimporte(),25)   
        self.assertEqual(self.viaje.obtenerimportesiguiente(),20)   
        
class CalificacionTest(TestCase):
    def setUp(self):
        calicacion = Calificacion()
        self.calificacion.evaluador = Persona()
        self.calificacion.evaluado = Persona()
        self.viaje = Viaje()
    
        
    def test_calificar(self):
        self.calificacion.calificar(5)
        self.assertEqual(self.evaluado.puntos,5)   
        self.calificacion.calificar(-5)
        self.assertEqual(self.evaluado.puntos,5)
        
import unittest
from pension import *
from datetime import date

class PensionTest(unittest.TestCase):
	def setUp(self):
		self.g = Pension()


	#Casos de prueba basicos

	# test hombre cumple requisitos basicos
	def testHombreBasico(self):
		sexo = 'm'
		anhosServicio = 60
		condicion = 0
		semanas = 750
		self.assertTrue(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'No tiene Pension')

	# test mujer cumple requisitos basicos
	def testMujerBasico(self):
		sexo = 'f'
		anhosServicio = 55
		condicion = 0
		semanas = 750
		self.assertTrue(self.g.verificar(sexo, anhosServicio, semanas, condicion,), 'No tiene Pension')

	# test hombre no tiene anhos para cumplir requisito
	def testHombreNoCumpleAnhosServicioRequisito(self):
		sexo = 'm'
		anhosServicio = 47
		condicion = 0
		semanas = 750
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'tiene Pension, no deberia')

	def testHombreNoCumpleSemanasRequisito(self):
		sexo = 'm'
		anhosServicio = 62
		condicion = 0
		semanas = 645
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'tiene Pension, no deberia')

	def testMujerNoCumpleEdadRequisito(self):
		sexo = 'f'
		anhosServicio = 52
		condicion = 0
		semanas = 751
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'tiene Pension, no deberia')

	def testMujerNoCumpleSemanasRequisito(self):
		sexo = 'f'
		anhosServicio = 59
		condicion = 0
		semanas = 733
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'tiene Pension, no deberia')

	def testHombreNoCumpleAmbosRequisito(self):
		sexo = 'm'
		anhosServicio = 47
		condicion = 0
		semanas = 745
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'tiene Pension, no deberia')

	def testMujerNoCumpleAmbosRequisito(self):
		sexo = 'f'
		anhosServicio = 59
		condicion = 0
		semanas = 733
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'tiene Pension, no deberia')

	#Casos de prueba con trabajos en condiciones que ponen en riesgo la salud.
	def testHombreCumpleConReduccionRequisito(self):
		sexo = 'm'
		edad = 55
		condicion = 5
		semanas = 750
		self.assertTrue(self.g.verificar(sexo, edad, semanas, condicion), 'No tiene Pension')

	def testMujerConReduccionArticulo162(self):
		sexo = 'f'
		edad = 59
		condicion = 1
		semanas = 750
		self.assertTrue(self.g.verificar(sexo, edad, semanas, condicion), 'No tiene Pension')

if __name__ == '__main__':
	unittest.main()
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
		sexo = 'h'
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
		self.assertTrue(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'tiene Pension, no deberia')

if __name__ == '__main__':
	unittest.main()
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
		edad = 60
		condicion = 0
		semanas = 750
		self.assertTrue(self.g.verificar(sexo, edad, semanas, condicion), 'No tiene Pension')

	def testMujerBasico(self):
		sexo = 'h'
		edad = 55
		condicion = 0
		semanas = 750
		self.assertTrue(self.g.verificar(sexo, edad, semanas, condicion,), 'No tiene Pension')

if __name__ == '__main__':
	unittest.main()
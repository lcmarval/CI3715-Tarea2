import unittest
from pension import *
from datetime import date

class PensionTest(unittest.TestCase):
	def setUp(self):
		self.g = Pension()

	# test hombre cumple requisitos basicos
	def testHombreBasico(self):
		sexo = 'm'
		edad = 60
		condicion = 0
		semanas = 750
		self.assertTrue(Pension.verificar(sexo, edad, semanas, condicion, date(1994,2,13)), 'No tiene Pension')

if __name__ == '__main__':
	unittest.main()
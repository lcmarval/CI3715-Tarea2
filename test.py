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
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'tiene Pension, no deberia')

	def testHombreNoCumpleSemanasRequisito(self):
		sexo = 'm'
		anhosServicio = 62
		condicion = 0
		reduccion = 0
		semanas = 645
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'No tiene Pension')

	def testMujerNoCumpleEdadRequisito(self):
		sexo = 'h'
		anhosServicio = 52
		condicion = 0
		reduccion = 0
		semanas = 751
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'No tiene Pension')

	def testMujerNoCumpleSemanasRequisito(self):
		sexo = 'h'
		anhosServicio = 59
		condicion = 0
		reduccion = 0
		semanas = 733
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'No tiene Pension')

	def testHombreNoCumpleAmbosRequisito(self):
		sexo = 'm'
		anhosServicio = 47
		condicion = 0
		reduccion = 0
		semanas = 745
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'No tiene Pension')

	def testMujerNoCumpleAmbosRequisito(self):
		sexo = 'h'
		anhosServicio = 59
		condicion = 0
		reduccion = 0
		semanas = 733
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'No tiene Pension')

if __name__ == '__main__':
	unittest.main()
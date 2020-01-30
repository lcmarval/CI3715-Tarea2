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
		self.assertTrue(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'No tiene Pension')

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
		anhosServicio = 55
		condicion = 5
		semanas = 750
		self.assertTrue(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'No tiene Pension')

	def testMujerConReduccionArticulo162(self):
		sexo = 'f'
		anhosServicio = 59
		condicion = 1
		semanas = 750
		self.assertTrue(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'No tiene Pension')

	# Artuclo 162 falso
	def testHombreCumpleConReduccionRequisitoAnhosInsuficientes(self):
		sexo = 'm'
		anhosServicio = 53
		condicion = 5
		semanas = 750
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'Tiene Pension, No debe')

	def testMujerConReduccionArticulo162AnhosInsuficientes(self):
		sexo = 'f'
		anhosServicio = 40
		condicion = 1
		semanas = 750
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'Tiene Pension, no debe')

	# Casos Maliciosos
	def testHombreMayuscula(self):
		self.assertFalse(self.g.verificar('M', 60, 750, 0), 'Tiene pension, es Mayuscula')

	def testMujerMayuscula(self):
		self.assertFalse(self.g.verificar('F', 55, 750, 0), 'Tiene pension, es Mayuscula')

	def testParametroSexoIncorrecto(self):
		sexo = 'n'
		anhosServicio = 59
		condicion = 1
		semanas = 750
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'Tiene pension, sin saber sexo')

	def testParametroAnhosServicioIncorrecto(self):
		sexo = 'm'
		anhosServicio = 'sesenta'
		condicion = 1
		semanas = 750
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'Tiene pension, Anhos tipo incorrecto')
	
	def testParametroCondicionFloatIncorrecto(self):
		sexo = 'f'
		anhosServicio = 54
		condicion = 1.1 # incorrecto ?
		semanas = 750
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'Tiene pension, Condicion tipo incorrecto')

	def testParametroSemanasRedondeaIncorrecto(self):
		sexo = 'f'
		anhosServicio = 56
		condicion = 0
		semanas = 749.6
		self.assertFalse(self.g.verificar(sexo, anhosServicio, semanas, condicion), 'Tiene pension, Redondea semanas tipo incorrecto')


if __name__ == '__main__':
	unittest.main()
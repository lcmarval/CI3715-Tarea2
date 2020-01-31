import unittest
from pension import *
from datetime import date

MASCULINO = 'm'
FEMENINO = 'f'
A_SERVIVICIO_M = 60
A_SERVIVICIO_F = 55
SEMANAS_CORRECTAS = 750
CONDICION_SALUDABLE = 0

class PensionTest(unittest.TestCase):

	def setUp(self):
		self.g = Pension()

	#Casos de prueba basicos

	# test hombre cumple requisitos basicos
	def testHombreBasico(self):
		self.assertTrue(self.g.verificar(MASCULINO, A_SERVIVICIO_M, SEMANAS_CORRECTAS, CONDICION_SALUDABLE), 'No tiene Pension')

	# test mujer cumple requisitos basicos
	def testMujerBasico(self):
		self.assertTrue(self.g.verificar(FEMENINO, A_SERVIVICIO_F, SEMANAS_CORRECTAS, CONDICION_SALUDABLE), 'No tiene Pension')

	# test hombre no tiene anhos para cumplir requisito
	def testHombreNoCumpleAnhosServicioRequisito(self):
		self.assertFalse(self.g.verificar(MASCULINO, A_SERVIVICIO_F - 5, SEMANAS_CORRECTAS, CONDICION_SALUDABLE), 'tiene Pension, no deberia')

	def testHombreNoCumpleSemanasRequisito(self):
		self.assertFalse(self.g.verificar(MASCULINO, A_SERVIVICIO_M + 2, SEMANAS_CORRECTAS - 5, CONDICION_SALUDABLE), 'tiene Pension, no deberia')

	def testMujerNoCumpleEdadRequisito(self):
		self.assertFalse(self.g.verificar(FEMENINO, A_SERVIVICIO_F - 2, SEMANAS_CORRECTAS + 1, CONDICION_SALUDABLE), 'tiene Pension, no deberia')

	def testMujerNoCumpleSemanasRequisito(self):
		self.assertFalse(self.g.verificar(FEMENINO, A_SERVIVICIO_M - 1, SEMANAS_CORRECTAS - 15, CONDICION_SALUDABLE), 'tiene Pension, no deberia')

	def testHombreNoCumpleAmbosRequisito(self):
		self.assertFalse(self.g.verificar(MASCULINO, A_SERVIVICIO_F - 5, SEMANAS_CORRECTAS - 15, CONDICION_SALUDABLE), 'tiene Pension, no deberia')

	def testMujerNoCumpleAmbosRequisito(self):
		self.assertFalse(self.g.verificar(FEMENINO, A_SERVIVICIO_F - 5, SEMANAS_CORRECTAS - 22, CONDICION_SALUDABLE), 'tiene Pension, no deberia')

	#Casos de prueba con trabajos en condiciones que ponen en riesgo la salud.
	def testHombreCumpleConReduccionRequisito(self):
		self.assertTrue(self.g.verificar(MASCULINO, A_SERVIVICIO_F, SEMANAS_CORRECTAS, CONDICION_SALUDABLE + 5), 'No tiene Pension')

	def testMujerConReduccionArticulo162(self):
		self.assertTrue(self.g.verificar(FEMENINO, A_SERVIVICIO_F - 1, SEMANAS_CORRECTAS, CONDICION_SALUDABLE + 1), 'No tiene Pension')

	# Artuclo 162 falso
	def testHombreCumpleConReduccionRequisitoAnhosInsuficientes(self):
		self.assertFalse(self.g.verificar(MASCULINO, A_SERVIVICIO_F - 2, SEMANAS_CORRECTAS, 5), 'Tiene Pension, No debe')

	def testMujerConReduccionArticulo162AnhosInsuficientes(self):
		self.assertFalse(self.g.verificar(FEMENINO, 40, SEMANAS_CORRECTAS, 1), 'Tiene Pension, no debe')

	# Casos Maliciosos
	def testHombreMayuscula(self):
		self.assertFalse(self.g.verificar('M', A_SERVIVICIO_M, SEMANAS_CORRECTAS, CONDICION_SALUDABLE), 'Tiene pension, es Mayuscula')

	def testMujerMayuscula(self):
		self.assertFalse(self.g.verificar('F', A_SERVIVICIO_F, SEMANAS_CORRECTAS, CONDICION_SALUDABLE), 'Tiene pension, es Mayuscula')

	def testParametroSexoIncorrecto(self):
		self.assertFalse(self.g.verificar('n', A_SERVIVICIO_M - 1, SEMANAS_CORRECTAS, CONDICION_SALUDABLE), 'Tiene pension, sin saber sexo')

	def testParametroSexoBooleano(self):
		self.assertFalse(self.g.verificar(True, A_SERVIVICIO_M - 1, SEMANAS_CORRECTAS, CONDICION_SALUDABLE + 1), 'Tiene pension, sexo Booleano')

	def testParametroAnhosServicioIncorrecto(self):
		self.assertFalse(self.g.verificar(MASCULINO, 'SESENTA', SEMANAS_CORRECTAS, CONDICION_SALUDABLE + 1), 'Tiene pension, Anhos tipo incorrecto')
	
	def testParametroCondicionFloatIncorrecto(self):
		self.assertFalse(self.g.verificar(FEMENINO, A_SERVIVICIO_F - 1, SEMANAS_CORRECTAS, CONDICION_SALUDABLE + 0.1), 'Tiene pension, Condicion tipo incorrecto')

	def testParametroSemanasRedondeaIncorrecto(self):
		self.assertFalse(self.g.verificar(FEMENINO, A_SERVIVICIO_F + 1, SEMANAS_CORRECTAS - 0.4, CONDICION_SALUDABLE), 'Tiene pension, Redondea semanas tipo incorrecto')


if __name__ == '__main__':
	unittest.main()
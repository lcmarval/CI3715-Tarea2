from datetime import date

MASCULINO = 'm'
FEMENINO = 'f'
A_SERVIVICIO_M = 60
A_SERVIVICIO_F = 55
SEMANAS_CORRECTAS = 750
CONDICION_SALUDABLE = 0
MINIMO_ANHOS_CONDICION = 1
MAXIMO_ANHOS_CONDICION = 5

class Pension():

	def __init__(self):
		pass

	def ReduccionArticulo162(self, condicion):
		return condicion == CONDICION_SALUDABLE

	def EsHombre(self, sexo):
		return sexo == MASCULINO

	def EsMujer(self, sexo):
		return sexo == FEMENINO

	def AniosDeServicioHombre(self, anhosServicio):
		return anhosServicio >= A_SERVIVICIO_M 

	def AniosDeServicioMujer(self, anhosServicio):
		return anhosServicio >= A_SERVIVICIO_F

	def RequisitosDeSemanasTrabajadas(self, semanas):
		return semanas >= SEMANAS_CORRECTAS

	def DeUnAnioEnAdelanteDeReduccion(self, condicion):
		return condicion >= MINIMO_ANHOS_CONDICION

	def TopeDeReduccionPosible(self, condicion):
		return condicion <= MAXIMO_ANHOS_CONDICION

	def AniosDeServiciosJuntoConLaReduccionEnHombres(self, anhosServicio, condicion):
		return type(anhosServicio) == int and type(condicion) == int and anhosServicio + condicion >= A_SERVIVICIO_M

	def AniosDeServiciosJuntoConLaReduccionEnMujeres(self, anhosServicio, condicion):
		return type(anhosServicio) == int and type(condicion) == int and anhosServicio + condicion >= A_SERVIVICIO_F

	def verificar(self,sexo, anhosServicio, semanas, condicion):
		if self.EsHombre(sexo):

			if self.ReduccionArticulo162(condicion):

				return (self.AniosDeServicioHombre(anhosServicio) and 
				        self.RequisitosDeSemanasTrabajadas(semanas))

			else:

				return (self.DeUnAnioEnAdelanteDeReduccion(condicion) and 
				        self.TopeDeReduccionPosible(condicion) and 
						self.AniosDeServiciosJuntoConLaReduccionEnHombres(anhosServicio, condicion) and 
						self.RequisitosDeSemanasTrabajadas(semanas))

		elif self.EsMujer(sexo):

			if self.ReduccionArticulo162(condicion):

				return (self.AniosDeServicioMujer(anhosServicio) and 
				        self.RequisitosDeSemanasTrabajadas(semanas))

			else:
				
				return (self.DeUnAnioEnAdelanteDeReduccion(condicion) and 
				        self.TopeDeReduccionPosible(condicion) and 
						self.AniosDeServiciosJuntoConLaReduccionEnMujeres(anhosServicio, condicion) and 
						self.RequisitosDeSemanasTrabajadas(semanas))
			
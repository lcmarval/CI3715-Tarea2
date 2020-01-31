from datetime import date

class Pension():

	def __init__(self):
		pass

	def ReduccionArticulo162(self, condicion):
		return condicion == 0

	def EsHombre(self, sexo):
		return sexo == 'm'

	def EsMujer(self, sexo):
		return sexo == 'f'

	def AniosDeServicioHombre(self, anhosServicio):
		return anhosServicio >= 60

	def AniosDeServicioMujer(self, anhosServicio):
		return anhosServicio >= 55

	def RequisitosDeSemanasTrabajadas(self, semanas):
		return semanas >= 750

	def DeUnAnioEnAdelanteDeReduccion(self, condicion):
		return condicion >= 1

	def TopeDeReduccionPosible(self, condicion):
		return condicion <= 5

	def AniosDeServiciosJuntoConLaReduccionEnHombres(self, anhosServicio, condicion):
		return anhosServicio + condicion >= 60

	def AniosDeServiciosJuntoConLaReduccionEnMujeres(self, anhosServicio, condicion):
		return anhosServicio + condicion >= 55

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
			
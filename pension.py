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

	def verificar(self,sexo, anhosServicio, semanas, condicion):
		if self.EsHombre(sexo):

			if self.ReduccionArticulo162(condicion):

				return (self.AniosDeServicioHombre(anhosServicio) and 
				        self.RequisitosDeSemanasTrabajadas(semanas))

			else:

				return (condicion >= 1 and 
				        condicion <= 5 and 
						(anhosServicio + condicion >= 60) and 
						self.RequisitosDeSemanasTrabajadas(semanas))

		elif self.EsMujer(sexo):

			if self.ReduccionArticulo162(condicion):

				return (self.AniosDeServicioMujer(anhosServicio) and 
				        self.RequisitosDeSemanasTrabajadas(semanas))

			else:
				
				return (condicion >= 1 and 
				        condicion <= 5 and 
						(anhosServicio + condicion >= 55) and 
						self.RequisitosDeSemanasTrabajadas(semanas))
			
from datetime import date

class Pension():

	def __init__(self):
		pass

	def verificar(self,sexo, anhosServicio, semanas, condicion):
		if (sexo == 'm'):
			return (anhosServicio >= 60 and condicion == 0 and semanas >= 750)

		elif (sexo == 'h'):
			return (anhosServicio >= 55 and condicion == 0 and semanas >= 750)
			
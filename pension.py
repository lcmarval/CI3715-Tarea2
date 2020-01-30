from datetime import date

class Pension():

	def __init__(self):
		pass

	def verificar(self,sexo, anhosServicio, semanas, condicion):
		if (anhosServicio >= 60 and sexo == 'm' and condicion == 0 and semanas >= 750):
			return True
		else:
			pass
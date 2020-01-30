from datetime import date

class Pension():

	def __init__(self):
		pass

	def verificar(self,sexo, anhosServicio, semanas, condicion):
		if (sexo == 'm'):

			if ( condicion == 0):

				return (anhosServicio >= 60 and semanas >= 750)

			else:

				return (condicion >= 1 and condicion <= 5 and (anhosServicio + condicion >= 60) and semanas >= 750)

		elif (sexo == 'f'):

			if ( condicion == 0):

				return (anhosServicio >= 55 and semanas >= 750)

			else:
				
				return (condicion >= 1 and condicion <= 5 and (anhosServicio + condicion >= 55) and semanas >= 750)
			
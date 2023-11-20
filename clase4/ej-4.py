# Crear una clase llamada Persona.
class Persona:
	# Con los siguientes atributos privados:
	# •nombre
	# •edad
	# •dni
	def __init__(self, nombre, edad, dni) -> None:
		self.nombre = nombre
		self.edad = edad
		self.dni = dni
# Y los siguientes métodos:
# •mostrar_edad(): retorna la edad de la persona
# •es_mayor_edad(): retorna True si edad es mayor o igual a 18, o False si es menor a 18.
	def mostrar_edad(self): return self.edad

	def es_mayor_edad(self): return self.edad >= 18

# El método constructor __init__ de la clase debe recibir y asignar los valores a cada uno de
# los atributos privados de la clase.

ulises = Persona("Ulises", 18, 44280688)

print(ulises.__dict__)
print(ulises.mostrar_edad())
print(ulises.es_mayor_edad())

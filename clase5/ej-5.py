def empty_string(str):
	return str == ""

# Enunciado

# Crear una clase llamada ListaDeTareas con los siguientes atributos y métodos:
class ListaDeTareas:

	# • Atributo de instancia privado “lista_tareas” de tipo list.
	def __init__(self):
		self.__lista_tareas = []

	# • Método de instancia público “agregarTarea(tarea)”, que recibe como argumento
	# una tarea que debe ser agregada a la lista de tareas (atributo “lista_tareas”) y
	# retorna el string “Tarea agregada correctamente a la lista” ó “La tarea no fue
	# agregada a la lista” en caso que la tarea se haya agregado o no a la lista
	# respectivamente.
	def agregar_tarea(self, tarea):
		if not empty_string(tarea):
			self.__lista_tareas.append(tarea)
			return f"Tarea: '{tarea}' agregada correctamente a la lista"
		else:
			return f"La tarea: '{tarea}' no fue agregada a la lista"


	# • Método de instancia público “quitarTarea(tarea)”, que recibe como argumento una
	# tarea que debe ser eliminada de la lista de tareas (atributo “lista_tareas”) y retorna
	# el string “Tarea eliminada correctamente de la lista” ó “La tarea no fue eliminada de
	# la lista” en caso que la tarea se haya eliminado o no de la lista respectivamente.
	def quitar_tarea(self, tarea):
		if not empty_string(tarea) and tarea in self.__lista_tareas:
			self.__lista_tareas.remove(tarea)
			return f"Tarea: '{tarea}' eliminada correctamente de la lista"
		else:
			return f"La tarea: '{tarea}' no fue eliminada de la lista"

	# • Método de instancia público “mostrarTareas()”, que no recibe ningún argumento y
	# retorna la lista de tareas (atributo “lista_tareas”) .
	# Luego, se debe crear una instancia de ListaDeTareas, agregar tareas a la lista, eliminar
	# tareas de la lista y finalmente imprimir la lista completa de tareas.
	def mostrar_tareas(self): return self.__lista_tareas

	# Nota: el método “quitarTarea(tarea)” debe validar si la tarea a eliminar existe en la lista
	# antes de ser eliminada.


lista_tareas1 = ListaDeTareas()
print(lista_tareas1.agregar_tarea("Hacer el ejercicio 6"))
print(lista_tareas1.agregar_tarea(""))
print(lista_tareas1.agregar_tarea("Gym"))

print(lista_tareas1.quitar_tarea("Gym"))
print(lista_tareas1.quitar_tarea(""))
print(lista_tareas1.quitar_tarea("NoExiste"))

print(lista_tareas1.mostrar_tareas())

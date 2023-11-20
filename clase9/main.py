from typing import List


class ValueError(Exception):
	def __init__(self, value,message="Error: Imposible añadir elementos duplicados") -> None:
		self.value = value
		self.message = message
		super().__init__(message)


	def __str__(self) -> str:
		return f"{self.message} => {self.value}"



# Manejo de Excepciones en Python
# 1. Realiza una función llamada agregar_una_vez(lista, elem) que reciba una lista y
# un elemento. La función debe añadir el elemento al final de la lista con la condición
# de no repetir ningún elemento. Si este elemento ya se encuentra en la lista se debe
# invocar un error de tipo ValueError que debes capturar y mostrar el siguiente
# mensaje en su lugar:
# “Error: Imposible añadir elementos duplicados => [elemento]”
def agregar_una_vez(lista: List, elem):
	try:
		if elem in lista:
			raise ValueError(elem)
		else:
			lista.append(elem)

	except ValueError:
		print(ValueError(elem))




# En una función main() inicializa la lista con: elementos = [1, 5, -2], luego intenta
# añadir los siguientes valores a la lista: 10, -2, "Hola". Para finalizar, muestra el
# contenido de la lista.
def main():
	elementos = [1, 5, -2]
	agregar_una_vez(elementos, 10)
	agregar_una_vez(elementos, -2)
	agregar_una_vez(elementos, "Hola")
	print(elementos)

main()

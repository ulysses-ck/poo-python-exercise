from typing import List
import re
import random


# Crear una clase llamada Password con las siguientes condiciones:
class Password:
	# • Dos atributos de clase privados:
	# 1. LONGITUD. Cuyo valor sea 8 (numérico).
	# 2. CARACTERES_VALIDOS. Cuyo valor sea
	# "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%
	# &+" (string)
	__LONGITUD = 8
	__CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

	# • Dos atributos de instancia privados:
	def __init__(self, longitud) -> None:
		# 1. longitud. Por defecto, será igual al valor del atributo de clase LONGITUD. Y su valor no
		# podrá ser inferior a 6 caracteres ni mayor a 15 caracteres.
		if longitud >= 6 <= 15:
			self.__longitud = longitud
		else:
			self.__longitud = self.__LONGITUD

		# 2. contraseña. Su valor aleatorio deberá ser asignado en el método generarPassword().
		# • Un método inicializador de instancias, con el parámetro longitud cuyo valor se asignará al
		# atributo de instancia. Generará una contraseña aleatoria con esa longitud invocando al
		# método generarPassword().
		self.__contrasenia = self.generar_password()

	# • Dos métodos de instancia públicos, cuya implementación deberá ser:
	# 1. esFuerte(): devuelve un booleano si es fuerte o no. Para que sea fuerte debe tener
	# más de 1 mayúscula, 1 carácter especial, más de 1 minúscula y más de 1 números.
	def es_fuerte(self, value: str) -> bool:
		num_upper_char = re.findall(r"[A-Z]", value)
		num_lower_char = re.findall(r"[a-z]", value)
		num_digit_char = re.findall(r"\d", value)
		num_special_chars = re.findall(r"\W", value)

		return len(num_digit_char) > 1 and len(num_upper_char) > 1 and len(
		    num_special_chars) > 1 and len(num_lower_char) > 1

	# 2. generarPassword(): genera la contraseña del objeto cuyo valor de tipo string tendrá
	# una longitud igual al valor del atributo de instancia “longitud”. Para la generación de la
	# clave puede usar los métodos random.choice() y string.join() de Python.
	def generar_password(self) -> str:
		chars = []
		for _ in range(self.__longitud):
			chars.append(random.choice(self.__CARACTERES_VALIDOS))

		return "".join(chars)

	# • Incluir métodos públicos que permitan obtener y asignar valores (getters y setters) a los
	# atributos de instancia privados.
	# • Sobreescribir el método de instancia __str__(), para que retorne la clave generada y el
	# valor booleano que devuelve el método “es_fuerte()”.
	def get_longitud(self):
		return self.__longitud

	def set_longitud(self, longitud):
		self.__longitud = longitud

	def get_contrasenia(self):
		return self.__contrasenia

	def set_contrasenia(self, contrasenia):
		self.__contrasenia = contrasenia

	def __str__(self) -> str:
		msg = f"{self.get_contrasenia()} is "
		if self.es_fuerte(self.get_contrasenia()):
			return msg + "strong"
		else:
			return msg + "not strong"


# Luego, agregar sentencias de código Python que permitan:
# • Crear una lista de objetos de tipo Password.
# • Crear instancias de Password y agregarlas a la lista. Para cada objeto, se debe ingresar la
# longitud de la clave por teclado. Si el valor ingresado es cero, no se pasará ningún valor
# como argumento al método inicializador.
# • Mostrar cada una de las contraseñas creadas y si es o no fuerte (usar un bucle). Para ello,
# usar este simple formato:
# contraseña1 - valor_booleano1
# contraseña2 - valor_bololeano2
list_password: List[Password] = []

for i in range(5):
	longitud = int(input("Write the length of the new password:\n"))
	new_password = Password(longitud)
	list_password.append(new_password)

for i in range(len(list_password)):
	print(
	    f"password: {list_password[i].get_contrasenia()}\nlength: {list_password[i].get_longitud()}\nPassword {i+1}: {str(list_password[i])}"
	)

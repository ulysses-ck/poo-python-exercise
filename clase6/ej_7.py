# pylint: disable=all
import re
import random


class Password:
	__LONGITUD = 8
	__CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

	def __init__(self, longitud) -> None:
		self.__longitud = longitud if longitud >= 6 and longitud <= 15 else self.__LONGITUD
		self.__contrasenia = self.generar_password()

	def es_fuerte(self, value) -> bool:
		return len(re.findall(r"[A-Z]", value)) > 1 and len(
		    re.findall(r"[a-z]", value)) > 1 and len(re.findall(
		        r"\d", value)) > 1 and len(re.findall(r"\D\W", value)) > 1

	def generar_password(self) -> str:
		return "".join(
		    random.choice(self.__CARACTERES_VALIDOS)
		    for x in range(self.__longitud))

	@property
	def longitud(self)	:
		return self.__longitud

	@longitud.setter
	def longitud(self, longitud):
		self.__longitud = longitud

	@property
	def contrasenia(self):
		return self.__contrasenia

	@contrasenia.setter
	def set_contrasenia(self, contrasenia):
		self.__contrasenia = contrasenia

	def __str__(self) -> str:
		return self.__contrasenia + " is strong" if self.es_fuerte(
		    self.__contrasenia) else " is not strong"


list_password = [
    Password(int(input(f"Write the length for password {x+1}:\n")))
    for x in range(2)
]

[
    print(
        f"password: {password.contrasenia}\nlength: {password.longitud}\nPassword {index+1}: {str(password)}"
    ) for index, password in enumerate(list_password)
]

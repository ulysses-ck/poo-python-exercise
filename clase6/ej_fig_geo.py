# pylint: disable=all
from abc import abstractmethod
from abc import ABCMeta
from math import pi, sqrt


class FiguraGeometrica(metaclass=ABCMeta):

	def __init__(self, color_borde, color_fondo) -> None:
		self.color_fondo = color_fondo
		self.color_borde = color_borde

	@abstractmethod
	def perimetro(self) -> float:
		pass

	@abstractmethod
	def area(self) -> float:
		pass


class Rectangulo(FiguraGeometrica):

	def __init__(self, color_borde, color_fondo, base, altura):
		FiguraGeometrica.__init__(self, color_borde, color_fondo)
		self.base = base
		self.altura = altura

	def perimetro(self) -> float:
		return self.base * 2 + self.altura * 2

	def area(self) -> float:
		return self.base * self.altura


class Circulo(FiguraGeometrica):

	def __init__(self, color_borde, color_fondo, radio):
		FiguraGeometrica.__init__(self, color_borde, color_fondo)
		self.radio = radio

	def perimetro(self) -> float:
		return 2 * pi * self.radio

	def area(self) -> float:
		return pi * self.radio**2


class Triangulo(FiguraGeometrica):

	def __init__(self, color_borde, color_fondo, base, altura):
		FiguraGeometrica.__init__(self, color_borde, color_fondo)
		self.base = base
		self.altura = altura

	def perimetro(self) -> float:
		return sqrt(pow(self.base, 2) +
		            pow(self.altura, 2)) + self.base + self.altura

	def area(self) -> float:
		return self.base * self.altura / 2


MESSAGE_BORDE = "Ingrese color borde: "
MESSAGE_FONDO = "Ingrese color fondo: "
SEPARATOR = "\n==================\n"

print("Triangulo")
color_borde = input(MESSAGE_BORDE)
color_fondo = input(MESSAGE_FONDO)
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
triangulo = Triangulo(color_borde, color_fondo, base, altura)

print(SEPARATOR)

print("Rectangulo")
color_borde = input(MESSAGE_BORDE)
color_fondo = input(MESSAGE_FONDO)
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))
rectangulo = Rectangulo(color_borde, color_fondo, base, altura)

print(SEPARATOR)

print("Circulo")
color_borde = input(MESSAGE_BORDE)
color_fondo = input(MESSAGE_FONDO)
radio = float(input("Ingrese el radio: "))
circulo = Circulo(color_borde, color_fondo, radio)

print(SEPARATOR)

for fig in [triangulo, rectangulo, circulo]:
	print(f"Color borde: {fig.color_borde}")
	print(f"Color fondo: {fig.color_fondo}")
	print(f"Perimetro: {fig.perimetro()}")
	print(f"Area: {fig.area()}")

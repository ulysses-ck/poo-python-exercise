# pylint: disable=all
from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Type, TypeVar, List


# La clase CuentaBancaria, debe contener:
class CuentaBancaria(metaclass=ABCMeta):
	# • Atributos de instancia:
	# o nro_cuenta de tipo string.
	# o cbu de tipo string.
	# o alias de tipo string.
	# o saldo de tipo float.
	# o movimientos de tipo list.
	# • Método constructor:
	# o __init__ (self, *args) para inicializar los atributos de instancia nro_cuenta, cbu, alias y saldo
	# con los valores recibidos como parámetros; y el atributo movimientos como una nueva
	# lista.
	def __init__(self, nro_cuenta: str, cbu: str, alias: str, saldo: float):
		self.__nro_cuenta = nro_cuenta
		self.__cbu = cbu
		self.__alias = alias
		self.__saldo = saldo
		self.__movimientos = []

	@property
	def nro_cuenta(self):
		return self.__nro_cuenta

	@nro_cuenta.setter
	def nro_cuenta(self, nro_cuenta):
		self.__nro_cuenta = nro_cuenta

	@property
	def cbu(self):
		return self.__cbu

	@cbu.setter
	def cbu(self, cbu):
		self.__cbu = cbu

	@property
	def alias(self):
		return self.__alias

	@alias.setter
	def alias(self, alias):
		self.__alias = alias

	@property
	def saldo(self):
		return self.__saldo

	@saldo.setter
	def saldo(self, saldo):
		self.__saldo = saldo

	@property
	def movimientos(self):
		return self.__movimientos

	@movimientos.setter
	def movimientos(self, movimiento):
		self.__movimientos.append(movimiento)

	# • Métodos de instancia:

	# o consultar_saldo (), que retorna el saldo de la cuenta.
	def consultar_saldo(self) -> float:
		return self.__saldo

	# o depositar (monto_a_depositar de tipo float), que retorna un booleano indicando si la
	# operación se realizó correctamente o no. En caso que el depósito se haya realizado
	# correctamente, y luego de haber actualizado el saldo, debe agregar un nuevo elemento a
	# la lista movimientos, donde elemento será una tupla que tendrá los siguientes elementos:
	# fecha de tipo date, “depósito”, monto depositado y saldo.
	def depositar(self, monto_a_depositar: float) -> bool:
		if monto_a_depositar <= 0:
			return False
		else:
			self.saldo += monto_a_depositar
			date = datetime.now().strftime("%D - %H:%M:%S")
			self.__movimientos.append((date, "deposito", monto_a_depositar,
			                      self.__saldo))
			return True

	# instance method to add a new move to movimientos
	def register_move(self, tipo_extraccion, monto):
		date = datetime.now().strftime("%D - %H:%M:%S")
		self.__movimientos.append((date, tipo_extraccion, monto, self.__saldo))

	# • Métodos abstractos:
	# o extraer (monto_a_extraer de tipo float), que retorna un valor booleano. En caso que la
	# extracción se haya realizado correctamente, y luego de haber actualizado el saldo, debe
	# agregar un nuevo elemento a la lista movimientos, donde elemento será una tupla que
	# tendrá los siguientes elementos: fecha de tipo date, “extracción”, monto extraído y saldo.
	@abstractmethod
	def extraer(self, monto_a_extraer) -> float:
		pass

	# o transferir (monto_a_transferir de tipo float, cuenta_destino de tipo CuentaBancaria), que
	# retorna un valor booleano. En caso que la transferencia se haya realizado correctamente,
	# y luego de haber actualizado el saldo, debe agregar un nuevo elemento a la lista
	# movimientos, donde elemento será una tupla que tendrá los siguientes elementos: fecha
	# de tipo date, “transferencia”, monto transferido y saldo.
	@abstractmethod
	def transferir(self, monto_a_transferir) -> float:
		pass


TCuentaBancaria = TypeVar("TCuentaBancaria", bound=CuentaBancaria)


# La clase CajaDeAhorro debe contener:
class CajaDeAhorro(CuentaBancaria):
	# • Atributos de instancia:
	# o monto_limite_extracciones de tipo float.
	# o monto_limite_transferencias de tipo float.
	# o cant_extracciones_disponibles de tipo int.
	# o cant_transferencias_disponibles de tipo int.

	# • Método constructor:
	# o __init__(self, args *) para inicializar los atributos de instancia nro_cuenta, alias, cbu, saldo,
	# monto_limite_extracciones, monto_limite_transferencias, cant_extracciones_disponibles
	# y cant_transferencias_disponibles con los valores recibidos como parámetros.

	def __init__(self, nro_cuenta: str, alias: str, cbu: str, saldo: float,
	             monto_limite_extracciones: float,
	             monto_limite_transferencias: float,
	             cant_extracciones_disponibles: int,
	             cant_transferencias_disponibles: int):
		CuentaBancaria.__init__(self, nro_cuenta, alias, cbu, saldo)
		self.__monto_limite_extracciones: float = monto_limite_extracciones
		self.__monto_limite_transferencias: float = monto_limite_transferencias
		self.__cant_extracciones_disponibles: int = cant_extracciones_disponibles
		self.__cant_transferencias_disponibles: int = cant_transferencias_disponibles

	@property
	def monto_limite_extracciones(self):
		return self.__monto_limite_extracciones

	@monto_limite_extracciones.setter
	def monto_limite_extracciones(self, limite):
		self.__monto_limite_extracciones = limite

	@property
	def monto_limite_transferencias(self):
		return self.__monto_limite_transferencias

	@monto_limite_transferencias.setter
	def monto_limite_transferencias(self, value):
		self.__monto_limite_transferencias = value

	@property
	def cant_extracciones_disponibles(self):
		return self.__cant_extracciones_disponibles

	@cant_extracciones_disponibles.setter
	def cant_extracciones_disponibles(self, cantidad):
		self.__cant_extracciones_disponibles = cantidad

	@property
	def cant_transferencias_disponibles(self):
		return self.__cant_transferencias_disponibles

	@cant_transferencias_disponibles.setter
	def cant_transferencias_disponibles(self, cantidad):
		self.__cant_transferencias_disponibles = cantidad

	# • Métodos de instancia:
	# o extraer (monto_a_extraer de tipo float), que retorna un booleano indicando si la operación
	# se realizó correctamente o no. La extracción se considerará como correcta si
	# monto_a_extraer es mayor a cero, si monto_a_extraer no es superior al saldo, si
	# monto_a_extraer no es superior al monto_limite_extracciones y si la
	# cant_extracciones_disponibles es mayor a cero, en cuyo caso se deberá actualizar el saldo
	# y cant_extracciones_disponibles; e invocar al método heredado para registrar el
	# movimiento.
	def extraer(self, monto_a_extraer: float) -> bool:
		is_valid = monto_a_extraer > 0 and monto_a_extraer <= self.saldo and monto_a_extraer <= self.__monto_limite_extracciones and self.__cant_extracciones_disponibles > 0
		if is_valid:
			self.saldo = self.saldo - monto_a_extraer
			self.register_move("Extraccion", monto_a_extraer)
		return is_valid

	# o transferir (monto_a_transferir de tipo float, cuenta_destino de tipo CuentaBancaria), que
	# retorna un booleano indicando si la operación se realizó correctamente o no. La
	# transferencia se considerará como correcta si monto_a_transferir es mayor a cero, si
	# monto_a_transferir no es superior al saldo, si monto_a_transferir no es superior al
	# monto_limite_transferencias y si la cant_transferencias_disponibles es mayor a cero, en
	# cuyo caso se deberá actualizar el saldo y cant_transferencias_disponibles de la cuenta
	# origen y el saldo de la cuenta destino; e invocar al método heredado para registrar el
	# movimiento.
	def transferir(self, monto_a_transferir: float,
	               cuenta_destino: TCuentaBancaria) -> bool:
		is_valid = monto_a_transferir > 0 and monto_a_transferir <= self.saldo and monto_a_transferir <= self.__monto_limite_transferencias and self.__cant_transferencias_disponibles > 0

		if is_valid:
			self.saldo = self.saldo - monto_a_transferir
			cuenta_destino.saldo = cuenta_destino.saldo + monto_a_transferir
			self.register_move("Transferencia", monto_a_transferir)
			cuenta_destino.register_move("Transferencia", monto_a_transferir)

		return is_valid


# La clase CuentaCorriente debe contener:
class CuentaCorriente(CuentaBancaria):
	# • Atributos de instancia:
	# o monto_maximo_descubierto de tipo float.
	# • Método constructor:
	# o __init__(self, *args) para inicializar los atributos de instancia nro_cuenta, alias, cbu, saldo
	# y monto_maximo_descubierto con los valores recibidos como parámetros.
	def __init__(self, nro_cuenta, cbu, alias, saldo, monto_maximo_descubierto):
		CuentaBancaria.__init__(self, nro_cuenta, cbu, alias, saldo)
		self.__monto_maximo_descubierto: float = monto_maximo_descubierto

	@property
	def monto_maximo_descubierto(self):
		return self.__monto_maximo_descubierto

	@monto_maximo_descubierto.setter
	def monto_maximo_descubierto(self, monto_max):
		self.__monto_maximo_descubierto = monto_max

	# • Métodos de instancia:
	# o extraer (monto_a_extraer de tipo float), que retorna un booleano indicando si la operación
	# se realizó correctamente o no. La extracción se considerará como correcta si
	# monto_a_extraer es mayor a cero, si monto_a_extraer no es superior al saldo más el
	# monto_maximo_descubierto, en cuyo caso se deberá actualizar el saldo; e invocar al
	# método heredado para registrar el movimiento.
	def extraer(self, monto_a_extraer: float) -> bool:
		is_valid = monto_a_extraer > 0 and monto_a_extraer <= self.saldo + self.__monto_maximo_descubierto
		if is_valid:
			self.saldo = self.saldo - monto_a_extraer
			self.register_move("Extraccion", monto_a_extraer)
		return is_valid

	# o transferir (monto_a_transferir de tipo float, cuenta_destino de tipo CuentaBancaria), que
	# retorna un booleano indicando si la operación se realizó correctamente o no. La
	# transferencia se considerará como correcta si monto_a_transferir es mayor a cero, si
	# monto_a_transferir no es superior al saldo más el monto_maximo_descubierto, en cuyo
	# caso se deberá actualizar el saldo de la cuenta origen y el saldo de la cuenta destino; e
	# invocar al método heredado para registrar el movimiento.
	def transferir(self, monto_a_transferir: float,
	               cuenta_destino: TCuentaBancaria) -> bool:
		is_valid = monto_a_transferir > 0 and monto_a_transferir <= self.saldo + self.__monto_maximo_descubierto
		if is_valid:
			self.saldo = self.saldo - monto_a_transferir
			cuenta_destino.saldo = cuenta_destino.saldo + monto_a_transferir
			self.register_move("Transferencia", monto_a_transferir)
			cuenta_destino.register_move("Transferencia", monto_a_transferir)
		return is_valid


# La clase Cliente debe contener:
class Cliente:
	# • Atributos de instancia:
	# o razon_social de tipo string.
	# o cuit de tipo string.
	# o tipo_persona de tipo string (física o jurídica).
	# o domicilio de tipo string.
	# o cuentas_bancarias de tipo list.
	# • Método constructor:
	# o __init__(self, *args) para inicializar los atributos de instancia razon_social, cuit,
	# tipo_persona y domicilio con los valores recibidos como parámetros, y el atributo
	# cuentas_bancarias como una nueva lista.
	def __init__(self, razon_social: str, cuit: str, tipo_persona: str,
	             domicilio: str):
		self.__razon_social = razon_social
		self.__cuit = cuit
		self.__domicilio = domicilio
		self.__tipo_persona = tipo_persona
		self.__cuentas_bancarias: List[TCuentaBancaria] = []

	@property
	def razon_social(self):
		return self.__razon_social

	@razon_social.setter
	def razon_social(self, razon_social):
		self.__razon_social = razon_social

	@property
	def cuit(self):
		return self.__cuit

	@cuit.setter
	def cuit(self, cuit):
		self.__cuit = cuit

	@property
	def domicilio(self):
		return self.__domicilio

	@domicilio.setter
	def domicilio(self, domicilio):
		self.__domicilio = domicilio

	@property
	def tipo_persona(self):
		return self.__tipo_persona

	@tipo_persona.setter
	def tipo_persona(self, tipo_persona):
		self.__tipo_persona = tipo_persona

	@property
	def cuentas_bancarias(self):
		return self.__cuentas_bancarias

	@cuentas_bancarias.setter
	def cuentas_bancarias(self, cuenta_bancaria):
		self.__cuentas_bancarias.append(cuenta_bancaria)

	# • Métodos de instancia:
	# o crear_nueva_cuenta_bancaria (), que retorna un booleano indicando si la operación se
	# realizó correctamente. Para crear una nueva instancia de CuentaBancaria se debe indicar
	# el tipo de cuenta (CajaDeAhorro o CuentaCorriente) e ingresar nro_cuenta, alias, cbu, saldo
	# y demás valores necesarios según el tipo de cuenta. El nuevo objeto CuentaBancaria debe
	# agregarse a la lista cuentas_bancarias.
	def crear_nueva_cuenta_bancaria(self, nueva_cuenta: TCuentaBancaria,
	                                nro_cuenta, alias, cbu, saldo,
	                                *args) -> bool:
		for i in locals():
			if i == None:
				print(f"{i} esta vacio")
				return False
		if issubclass(nueva_cuenta, CuentaCorriente):
			cuenta_creada: CuentaCorriente = nueva_cuenta(
			    nro_cuenta, alias, cbu, saldo, monto_maximo_descubierto=args[0])
			self.__cuentas_bancarias.append(cuenta_creada)
			return True
		elif issubclass(nueva_cuenta, CajaDeAhorro):
			cuenta_creada: CajaDeAhorro = nueva_cuenta(
			    nro_cuenta,
			    alias,
			    cbu,
			    saldo,
			    monto_limite_extracciones=args[0],
			    monto_limite_transferencias=args[1],
			    cant_extracciones_disponibles=args[2],
			    cant_transferencias_disponibles=args[3])
			self.__cuentas_bancarias.append(cuenta_creada)
			return True


# La clase Banco debe contener:
class Banco:
	# • Atributos de instancia:
	# o nombre de tipo string.
	# o domicilio de tipo string.
	# o clientes de tipo list.
	# • Método constructor:
	# o __init__(self, *args) para inicializar los atributos de instancia nombre y domicilio con los
	# valores recibidos como parámetros, y el atributo clientes como una nueva lista.
	def __init__(self, nombre, domicilio) -> None:
		self.__nombre = nombre
		self.__domicilio = domicilio
		self.__clientes: List[Cliente] = []

	@property
	def nombre(self):
		return self.__nombre

	@nombre.setter
	def nombre(self, nombre):
		self.__nombre = nombre

	@property
	def domicilio(self):
		return self.__domicilio

	@domicilio.setter
	def domicilio(self, domicilio):
		self.__domicilio = domicilio

	@property
	def clientes(self):
		return self.__clientes

	@clientes.setter
	def clientes(self, nuevo_cliente):
		self.__clientes.append(nuevo_cliente)

	# • Métodos de instancia:
	# o crear_nuevo_cliente (), que retorna un booleano indicando si la operación se realizó
	# correctamente. Para crear una nueva instancia de Cliente se debe ingresar razon_social,
	# cuit, tipo_persona y domicilio. El nuevo objeto Cliente debe agregarse a la lista clientes.
	def crear_nuevo_cliente(self, razon_social, cuit, tipo_persona, domicilio):
		cliente_nuevo = Cliente(razon_social, cuit, tipo_persona, domicilio)
		self.__clientes.append(cliente_nuevo)


# Para validar el modelo de gestión bancaria implementado, incluya una función main() con las
# instrucciones necesarias para crear un objeto Banco, tres instancias de Clientes (como mínimo)
# cada uno de ellos con dos objetos CuentaBancaria (como mínimo), uno de tipo CajaDeAhorro y
# otro de tipo CuentaCorriente.
# Luego simule varias operaciones de depósito, extracción y transferencias entre las cuentas.
# Finalmente, muestre por pantalla los datos de los clientes del banco, con los saldos de sus cuentas
# y el registro de los movimientos de las mismas.


def main():
	bbva = Banco(nombre="BBVA",
	             domicilio="Buenos Aires, Capital, Avenida Rivadavia 3600")
	bbva.crear_nuevo_cliente(razon_social="Juan Doe",
	                         cuit="20346784210",
	                         tipo_persona="Fiscal",
	                         domicilio="San Juan, San Juan, Peron 2341")
	bbva.crear_nuevo_cliente(razon_social="Manuel Averzara",
	                         cuit="19346254210",
	                         tipo_persona="Fiscal",
	                         domicilio="Mendoza, Potrerillos, Malvinas 2341")
	bbva.crear_nuevo_cliente(razon_social="Ulises Apaza",
	                         cuit="19346254210",
	                         tipo_persona="Fiscal",
	                         domicilio="San Juan, San Juan, Peron 2341")

	cliente_juan = bbva.clientes[0]
	cliente_manuel = bbva.clientes[1]
	cliente_ulises = bbva.clientes[2]

	# CajaDeAhorro
	cliente_juan.crear_nueva_cuenta_bancaria(CajaDeAhorro, "001",
	                                         "Caja De Ahorro 1", "CBU001",
	                                         2000.0, 800.0, 1500.0, 3, 8)
	cliente_manuel.crear_nueva_cuenta_bancaria(CajaDeAhorro, "003",
	                                           "Caja De Ahorro 2", "CBU002",
	                                           3000.0, 1000.0, 2000.0, 2, 6)
	cliente_ulises.crear_nueva_cuenta_bancaria(CajaDeAhorro, "003",
	                                           "Caja De Ahorro 3", "CBU003",
	                                           1000.0, 500.0, 1000.0, 5, 10)

	# CuentasCorrientes
	cliente_juan.crear_nueva_cuenta_bancaria(CuentaCorriente, "101",
	                                         "Caja de Ahorro 1", "CBU101",
	                                         5000.0, 1000.0)
	cliente_manuel.crear_nueva_cuenta_bancaria(CuentaCorriente, "102",
	                                           "Caja de Ahorro 2", "CBU102",
	                                           6000.0, 1200.0)
	cliente_ulises.crear_nueva_cuenta_bancaria(CuentaCorriente, "103",
	                                           "Caja de Ahorro 3", "CBU103",
	                                           7000.0, 1500.0)

	print(
	    f"Saldo de {cliente_juan.razon_social} caja ahorro: {cliente_juan.cuentas_bancarias[0].saldo}"
	)
	print(
	    f"Saldo de {cliente_juan.razon_social} cuenta corriente: {cliente_juan.cuentas_bancarias[1].saldo}"
	)

	print(
	    f"Saldo de {cliente_manuel.razon_social} caja ahorro: {cliente_manuel.cuentas_bancarias[0].saldo}"
	)
	print(
	    f"Saldo de {cliente_manuel.razon_social} cuenta corriente: {cliente_manuel.cuentas_bancarias[1].saldo}"
	)

	print(
	    f"Saldo de {cliente_ulises.razon_social} caja ahorro: {cliente_ulises.cuentas_bancarias[0].saldo}"
	)
	print(
	    f"Saldo de {cliente_ulises.razon_social} cuenta corriente: {cliente_ulises.cuentas_bancarias[1].saldo}"
	)

	juan_caja_ahorro: CajaDeAhorro = cliente_juan.cuentas_bancarias[0]
	ulises_caja_corriente: CuentaCorriente = cliente_ulises.cuentas_bancarias[1]
	manuel_caja_ahorro: CajaDeAhorro = cliente_manuel.cuentas_bancarias[0]

	print(juan_caja_ahorro.depositar(2000))
	print(juan_caja_ahorro.transferir(2000, ulises_caja_corriente))
	print(ulises_caja_corriente.transferir(4000, manuel_caja_ahorro))
	print(manuel_caja_ahorro.extraer(1000))

	print(f"Movimientos juan caja ahorro: {juan_caja_ahorro.movimientos}")
	print(f"Movimientos ulises cuenta_corriente: {ulises_caja_corriente.movimientos}")
	print(f"Movimientos manuel caja ahorro: {manuel_caja_ahorro.movimientos}")

	print(
	    f"Saldo de {cliente_juan.razon_social} caja ahorro: {cliente_juan.cuentas_bancarias[0].saldo}"
	)
	print(
	    f"Saldo de {cliente_juan.razon_social} cuenta corriente: {cliente_juan.cuentas_bancarias[1].saldo}"
	)

	print(
	    f"Saldo de {cliente_manuel.razon_social} caja ahorro: {cliente_manuel.cuentas_bancarias[0].saldo}"
	)
	print(
	    f"Saldo de {cliente_manuel.razon_social} cuenta corriente: {cliente_manuel.cuentas_bancarias[1].saldo}"
	)

	print(
	    f"Saldo de {cliente_ulises.razon_social} caja ahorro: {cliente_ulises.cuentas_bancarias[0].saldo}"
	)
	print(
	    f"Saldo de {cliente_ulises.razon_social} cuenta corriente: {cliente_ulises.cuentas_bancarias[1].saldo}"
	)


main()

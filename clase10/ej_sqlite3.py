# pylint disable=all
import sqlite3

bd = sqlite3.connect("empleados.db")

cursor = bd.cursor()

def create_table():
	query = '''CREATE TABLE Empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nro_legajo INTEGER NOT NULL UNIQUE,
        dni INTEGER NOT NULL UNIQUE,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        area TEXT NOT NULL
        )'''
	cursor.execute(query)
# • Opcion 1 Insertar un registro de empleado.
def insertar_registro(nro_legajo, dni, nombre, apellido, area):
	query = "INSERT INTO empleados (nro_legajo, dni, nombre, apellido, area) values (?, ? ,? ,? ,?)"
	cursor.execute(query, [nro_legajo, dni, nombre, apellido, area])
	bd.commit()
# • Opcion 2 Selecionar un registro de empleado a partir de su numero DNI.
def buscar_por_dni(dni):
	query = "SELECT * FROM empleados WHERE dni=?"
	cursor.execute(query, [dni])

# • Opcion 3 Selecionar todos los empleados o los registros de la tabla.
def get_all_empleados():
	query = "SELECT * FROM empleados"
	for row in cursor.execute(query):
		print(row)

# • Opcion 4 Modificar el area de un empleado en función de su numero de legajo.
def modificar_area_empleado(nro_legajo, area):
	query = "UPDATE empleados SET area=? WHERE nro_legajo=?"
	cursor.execute(query, [area, nro_legajo])
	bd.commit()

# • Opcion 5 Eliminar un empleado a partir del numero de legajo.
def eliminar_empleado(nro_legajo):
	query = "DELETE FROM empleados WHERE nro_legajo=?"
	cursor.execute(query, [nro_legajo])
	bd.commit()
# • Opcion 6 Finalizar.





# Cada opción se tiene que ingresar por teclado. Cada una de las sentencias que van a
# permitir ejecutar cada opción debe estar en una función por separado (salvo la opción
# nro 6). Es decir, la opción 1 “insertar un registro de empleado” tiene su propia función.
# La conexión a la Base de Datos también debe estar en una función por separado, al
# igual que la creación de la tabla es otra función.
# Luego de realizar acciones de modificación de datos INSERT DELETE UPDATE se debe
# cerrar la conexión.
def main():
	create_table()
	while True:
		print("Elige un numero para realizar una operacion")
		print("1 ingresar un empleado")
		print("2 buscar empleado por dni")
		print("3 traer todos los empleados")
		print("4 eliminar empleado por nro_legajo")
		print("5 modificar el area de un empleado por nro de legajo")
		print("6 finalizar programa y conexion de base de datos")

		opcion = int(input("Su eleccion:\n"))

		# • Opcion 1 Insertar un registro de empleado.
		if opcion == 1:
			# 	nro_legajo int not null unique,
			nro_legajo = int(input("Ingrese numero de legajo:\n"))
			# 	dni int not null UNIQUE,
			dni = int(input("Ingrese dni:\n"))
			# 	nombre text not null,
			nombre = input("Ingrese el nombre\n")
			# 	apellido text not null,
			apellido = input("Ingrese el apellido\n")
			# 	area text not null
			area = input("Ingrese el area\n")
			insertar_registro(nro_legajo, dni, nombre, apellido, area)
		# • Opcion 2 Selecionar un registro de empleado a partir de su numero DNI.
		elif opcion == 2:
			dni = input("Ingrese el dni del empleado a buscar\n")
			buscar_por_dni(dni)
		# • Opcion 3 Selecionar todos los empleados o los registros de la tabla.
		elif opcion == 3:
			get_all_empleados()
		# • Opcion 4 Modificar el area de un empleado en función de su numero de legajo.
		elif opcion == 4:
			nro_legajo= input("Ingrese el nro_legajo del empleado a cambiar\n")
			area= input("Ingrese la nueva area del empleado\n")
			modificar_area_empleado(nro_legajo, area)
		# • Opcion 5 Eliminar un empleado a partir del numero de legajo.
		elif opcion == 5:
			nro_legajo = input("Ingrese el nro_legajo del empleado a eliminar\n")
			eliminar_empleado(nro_legajo)
		# • Opcion 6 Finalizar.
		elif opcion == 6:
			bd.close()
			break

main()

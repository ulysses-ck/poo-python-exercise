# Escribe
# un programa en
# Python que solicite al usuario que ingrese 5 números enteros. Luego imprimir el máximo
# y el mínimo
# de los valores ingresados. El programa deberá
# permitir el
# ingreso de valores iguales.
nums = []
for i in range(5):
    num = int(input("Escriba un numero:"))
    nums.append(num)
print(nums)
print(f"Minimo: {min(nums)}")
print(f"Maximo: {max(nums)}")

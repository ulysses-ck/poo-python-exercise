# Escribe
# un programa en
# Python que solicite 5 números enteros al usuario. El mismo debe indicar si
# entre dichos valores hay números duplicados o no, imprimiendo por pantalla “HAY DUPLICADOS” o “SON TODOS
# DISTINTOS”.
nums = []
for i in range(5):
    nums.append(int(input("Escribe un numero: ")))

print(nums)
print("SON TODOS DISTINTOS" if len(set(nums)) == 5 else "HAY DUPLICADOS")

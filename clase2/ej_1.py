# Escribir un programa en Python que pida al usuario
# que ingrese las medidas de la base y la altura de un rectángulo y muestre:
# 1.El perímetro del rectángulo
# 2.El área del rectángulo
base =int(input("Ingrese base rectangulo:\n"))
altura = int(input("Ingrese altura rectangulo:\n"))

print(f"Perimetro: {base*2 + altura * 2}")
print(f"Area: {base * altura}")

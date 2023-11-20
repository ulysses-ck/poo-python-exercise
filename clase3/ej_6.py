from ej_5 import total_seconds

# Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.
hours_1 = int(input("hours 1: "))
minutes_1 = int(input("minutes 1: "))
seconds_1 = int(input("seconds 1: "))

hours_2 = int(input("hours 2: "))
minutes_2 = int(input("minutes 2: "))
seconds_2 = int(input("seconds 2: "))

total = total_seconds(hours_1, minutes_1, seconds_1) + total_seconds(
    hours_2, minutes_2, seconds_2)

print(f"hours: {(total - total % 3600) / 3600}")
print(f"minutes: {(total - total % 60) / 60}")
print(f"seconds: {total}")

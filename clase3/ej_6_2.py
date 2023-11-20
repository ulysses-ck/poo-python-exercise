from ej_5 import sum, total_seconds

# Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

first_interval = []
second_interval = []

for i in range(3):
	first_interval.append(int(input(f"Write the number 1:")))
	second_interval.append(int(input(f"Write the number 2:")))

total_interval_1 = total_seconds(first_interval[0], first_interval[1],
                                 first_interval[2])

total_interval_2 = total_seconds(second_interval[0], second_interval[1],
                                 second_interval[2])

total_final = sum(total_interval_1, total_interval_2)

print(f"hours: {total_final / 3600}")
print(f"minutes: {total_final / 60}")
print(f"seconds: {total_final}")


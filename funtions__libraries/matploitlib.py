import matplotlib.pyplot as plt
import random
import math
estudiantes = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Eva"]
estudiantes_2 = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Eva"]
notas = [8, 7.5, 6.1, 9.2, 8.8, 1]

# estudiante = random.choice(estudiantes_2)
# print(estudiante)

# plt.bar(estudiantes, notas)
# plt.show()

recetas = 1000
unidades = 15

# print(f"La empresa vendio {math.ceil(recetas/unidades)} unidades")

#------ funcione lambda


# nota_1 = int(input("Ingrese la nota del primer examen: "))
# nota_2 = int(input("Ingrese la nota del segundo examen: "))
# nota_3 = int(input("Ingrese la nota del tercer examen: "))

promedio = lambda nota_1, nota_2, nota_3: (nota_1 + nota_2 + nota_3) / 3

# print(promedio(nota_1, nota_2, nota_3))


# nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Eva"]
# for i in range(len(nombres)):
#     print(f"lo que tiene i es: {i}, lo que tiene nombres es: {nombres[i]}")


alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
print(imc)



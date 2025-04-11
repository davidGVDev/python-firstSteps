import random as rnd
import math
# numeros = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
# print(rnd.choice(numeros))

#4 - Crea un programa que genere aleatoriamente un número entero menor que 100.
# print(rnd.randint(0, 99))


#5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros 
# y calcule la potencia del primer número elevado al segundo.

# numero_1 = int(input("Ingrese el primer número: "))
# numero_2 = int(input("Ingrese el segundo número: "))
# res = math.pow(numero_1, numero_2)
# print(res)

"""
7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. 
El token debe ser par y variar de 1000 a 9998. Escribe 
un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este token generado aleatoriamente.
"""

# nombre = input("Ingrese su nombre: ")
# token = rnd.randrange(1000, 9998,2)
# print(f"Hola {nombre}, su token es: {token}")

"""
8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado 
"ensalada de frutas sorpresa". En este ítem, se eligen aleatoriamente 3 frutas de una 
lista de 12 para componer la ensalada de frutas del cliente. 
Crea el código que realice esta selección aleatoria según la lista dada.
"""
# frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

# fruta_1 = rnd.choice(frutas)
# fruta_2 = rnd.choice(frutas)
# fruta_3 = rnd.choice(frutas)

# print(f"La ensalada de frutas sorpresa es: {fruta_1}, {fruta_2}, {fruta_3}")

"""
9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, 
identificando cuáles resultan en un número entero. La lista es la siguiente:
"""
# numeros = [2, 8, 15, 23, 91, 112, 256]

# for numero in numeros:
#     raiz = math.sqrt(numero)
#     if raiz.is_integer():
#         print(f"La raiz cuadrada de {numero} es: {raiz}")

# numeros = [2, 8, 15, 23, 91, 112, 256]
# raices_enteras = [num for num in numeros if math.sqrt(num) % 1 == 0]
# print("Números con raíces enteras:", raices_enteras)


"""
10 - Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con jardines circulares 
y el precio del metro cuadrado de césped es de R$ 25,00. 
Pide a la persona usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.
"""
precio_metro_cuadrado = 25.00
radio = float(input("Ingrese el radio del área circular: "))
area = math.pi * radio ** 2
precio = area * precio_metro_cuadrado
print(f"El precio del césped es: R$ {precio:.2f}")






import json


texto = "Hola Mundo"
# textoMayusculas = texto.upper()
# textoMinusculas = texto.lower()
# textoCapitalizado = texto.capitalize()
# textoTitulo = texto.title()
# textoSinEspacios = texto.strip()
# textoSinEspaciosDerecha = texto.rstrip()
# textoSinEspaciosIzquierda = texto.lstrip()

# ------------- Tipos de datos -------------

# int => numeros enteros
# float => numeros decimales
# str => cadenas de texto
# bool => True o False

# int = 10 # int
# float = 10.5 # float
# str = "Hola Mundo" # str
# bool = True # bool

# print(type(int), int)
# print(type(float), float)
# print(type(str), str)
# print(type(bool), bool)


# ------------- Variables -------------

# Variables => son espacios en memoria que guardan un valor

nombre = "Juan" # str
edad = 20 # int
altura = 1.75 # float
esMayorDeEdad = True # bool

persona = {
    "datos": {
        "nombre": nombre,
        "edad": edad,
        "altura": altura,
        "esMayorDeEdad": esMayorDeEdad
    }
}

persona2 = {
    "datos": {
        "nombre": nombre,
        "edad": edad,
        "altura": altura,
        "esMayorDeEdad": esMayorDeEdad
    },
    "tipos": {
        "nombre": type(nombre),
        "edad": type(edad),
        "altura": type(altura),
        "esMayorDeEdad": type(esMayorDeEdad)
    }
}

# print(persona)
# print(json.dumps(persona, indent=4))

# Imprimir tipos de datos de manera más clara
# print("\nTipos de datos de las variables:")
# for variable, valor in persona2["datos"].items():
#     print(f"{variable}: {type(valor).__name__}")


# ------------- Operadores -------------

# Operadores aritméticos

# + => suma
# - => resta
# * => multiplicación
# / => división (float)
# // => división (int)
# % => módulo (resto)
# ** => potencia    

# Operadores de comparación

# == => igual
# != => diferente
# > => mayor
# < => menor

# Operadores lógicos

# and => y
# or => o
# not => no

# Operadores de asignación

# = => asignación
# += => suma y asignación
# -= => resta y asignación
# *= => multiplicación y asignación
# /= => división y asignación

# Operadores de pertenencia

# in => está
# not in => no está

# Operadores de identidad

# is => es
# is not => no es

# Operadores de comparación

# == => igual
# != => diferente
# > => mayor
# < => menor
# >= => mayor o igual
# <= => menor o igual

# --------- Input => entrada de datos ---------

# input => entrada de datos

numero = int(input("Ingresa el numero de la tabla de multiplicar: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")




































# Listas: 
# - Ordenadas y mutables (se pueden modificar)
# - Permiten elementos duplicados
# - Se accede por índice numérico
# - Se crean con corchetes []
lista = [1, 2, 3, 4, 5]

# Diccionarios:
# - No ordenados y mutables
# - Clave-valor (key-value)
# - No permiten claves duplicadas
# - Se accede por clave
# - Se crean con llaves {}
diccionario = {
    "nombre": "Juan",
    "edad": 20,
    "ciudad": "Madrid"
}

# Tuplas:
# - Ordenadas e inmutables (no se pueden modificar)
# - Permiten elementos duplicados
# - Se accede por índice numérico
# - Se crean con paréntesis ()
tupla = (1, 2, 3, 4, 5)

# Conjuntos:
# - No ordenados e inmutables (pero se pueden agregar/eliminar elementos)
# - No permiten elementos duplicados
# - No se puede acceder por índice
# - Se crean con llaves {} pero sin pares clave-valor
conjunto = {1, 2, 3, 4, 5}


# ---- manipulacion de listas ----

# Agregar elementos al final de la lista
lista.append(6)
print(lista)

# Agregar elementos de otra lista al final de la lista
lista.extend([7, 8, 9])
print(lista)

# Insertar elementos en una posición específica
lista.insert(0, 0)  # Insertar al principio
print(lista)

# Eliminar elementos
lista.remove(6)  # Eliminar elemento específico
print(lista)

# Eliminar elemento por índice
lista.pop(0)  # Eliminar primer elemento
print(lista)

# Eliminar todos los elementos
lista.clear()
print(lista)

# Partir una lista en dos 
lista1 = lista[:3] # desde el 0 hasta el 3
lista2 = lista[3:] # desde el 3 hasta el final
print(lista1)
print(lista2)

# Ordenar una lista
lista.sort()
print(lista)

# Invertir una lista
lista.reverse()
print(lista)

# Tamaño de la lista
print(len(lista))

# Saber el indice de un elemento
print(lista.index(5))

# Eliminar la lista
del lista

# ---- manipulacion de diccionarios ----

# Agregar elementos
diccionario["apellido"] = "Perez"
print(diccionario)

# Eliminar elementos
del diccionario["edad"]
print(diccionario)

# Verificar si una clave existe
print("apellido" in diccionario)

# Tamaño del diccionario
print(len(diccionario))

# Eliminar el diccionario
del diccionario

# ---- manipulacion de tuplas ----

# Tamaño de la tupla
print(len(tupla))

# Eliminar la tupla
del tupla

# ---- manipulacion de conjuntos ----

# Tamaño del conjunto
print(len(conjunto))

# Eliminar el conjunto
del conjunto


# ---- ejemplo de lista con diccionarios ----

lista = [
    {"nombre": "Juan", "edad": 20},
    {"nombre": "Maria", "edad": 21},
    {"nombre": "Pedro", "edad": 22}
]

# Agregar un diccionario a la lista
lista.append({"nombre": "Ana", "edad": 23})
print(lista)

# Eliminar un diccionario de la lista
lista.remove({"nombre": "Maria", "edad": 21})
print(lista)

# ---- ejemplo de diccionario con listas ----

diccionario = {
    "nombre": ["Juan", "Maria", "Pedro"],
    "edad": [20, 21, 22]
}

# Agregar un diccionario a la lista
diccionario["nombre"].append("Ana")
diccionario["edad"].append(23)
print(diccionario)

# eliminar un diccionario de la lista
diccionario["nombre"].remove("Maria")
diccionario["edad"].remove(21)
print(diccionario)















# --------- Estructuras condicionales ---------

# if => si
# elif => sino si
# else => sino

# if => si
# elif => sino si
# else => sino

# --------- operadores logicos ---------
# and => y
# or => o
# not => no

# --------- operador ternario ---------

# variable = valor1 if condicion else valor2

# --------- Ejercicios ---------

# 1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.
# numero1 = int(input("Ingresa el primer numero: "))
# numero2 = int(input("Ingresa el segundo numero: "))

# if numero1 > numero2:
#     print(f"El numero {numero1} es mayor que {numero2}")
# else:
#     print(f"El numero {numero2} es mayor que {numero1}")

# 2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).
# porcentaje = int(input("Ingresa el porcentaje de crecimiento de producción de una empresa: "))

# if porcentaje > 0:
#     print("Hubo un crecimiento")
# else:
#     print("Hubo una disminución")

# 3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.
# letra = input("Ingresa una letra: ")

# if letra in "aeiou":
#     print("Es una vocal")
# else:
#     print("Es una consonante")

# 4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.
# precio1 = int(input("Ingresa el precio del primer año: "))
# precio2 = int(input("Ingresa el precio del segundo año: "))
# precio3 = int(input("Ingresa el precio del tercer año: "))

# if precio1 > precio2 and precio1 > precio3:
#     print("El precio más alto es el del primer año")
# elif precio2 > precio1 and precio2 > precio3:
#     print("El precio más alto es el del segundo año")
# elif precio3 > precio1 and precio3 > precio2:
#     print("El precio más alto es el del tercer año")


# 5 - Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.
# precio1 = int(input("Ingresa el precio del primer producto: "))
# precio2 = int(input("Ingresa el precio del segundo producto: "))
# precio3 = int(input("Ingresa el precio del tercer producto: "))

# if precio1 < precio2 and precio1 < precio3:
#     print("El producto más barato es el del primer producto")
# elif precio2 < precio1 and precio2 < precio3:
#     print("El producto más barato es el del segundo producto")
# else:
#     print("El producto más barato es el del tercer producto")


# 6 - Escribe un programa que lea tres números y los muestre en orden descendente.
# lista = []
# numero1 = int(input("Ingresa el primer numero: "))
# numero2 = int(input("Ingresa el segundo numero: "))
# numero3 = int(input("Ingresa el tercer numero: "))

# lista.append(numero1)
# lista.append(numero2)
# lista.append(numero3)

# lista.sort(reverse=True)

# print(lista)

# 7 -Escribe un programa que pregunte en qué turno estudia la persona usuaria ("mañana", "tarde" o "noche") y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.
# turno = input("Ingresa en qué turno estudia la persona usuaria: ")

# if turno == "mañana":
#     print("¡Buenos Días!")
# elif turno == "tarde":
#     print("¡Buenas Tardes!")
# elif turno == "noche":
#     print("¡Buenas Noches!")
# else:
#     print("Valor Inválido!")


# 8 - Escribe un programa que solicite un número entero a la persona usuaria y determine si es par o impar. Pista: Puedes usar el operador módulo (%).
# numero = int(input("Ingresa un numero: "))

# if numero % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

# 9 - Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.
# numero = float(input("Ingresa un numero: "))

# if numero.is_integer():
#     print("El numero es entero")
# else:
#     print("El numero es decimal")

# Momento de los proyectos

# 10 - Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué operación desea realizar. 
# El resultado de la operación debe incluir información sobre el número, si es par o impar, positivo o negativo, e entero o decimal.

# numero1 = float(input("Ingresa el primer numero: "))
# numero2 = float(input("Ingresa el segundo numero: "))
# print("""
#       [1] Suma
#       [2] Resta
#       [3] Multiplicación
#       [4] División
#       """)
# operacion = int(input("Ingresa la operación que desea realizar: /n "))

# def par_impar(numero):
#     if numero % 2 == 0:
#         return "El numero es par"
#     else:
#         return "El numero es impar"
    
# def positivo_negativo(numero):
#     if numero > 0:
#         return "El numero es positivo"
#     else:
#         return "El numero es negativo"

# def entero_decimal(numero):
#     if numero.is_integer():
#         return "El numero es entero"
#     else:
#         return "El numero es decimal"

# def opcion_menu(operacion):
#     match operacion:
#         case 1:
#             print(f"La suma de los numeros es: {numero1 + numero2}")
#             print(par_impar(numero1 + numero2))
#             print(positivo_negativo(numero1 + numero2))
#             print(entero_decimal(numero1 + numero2))
#             print("--------------------------------")
#         case 2:
#             print(f"La resta de los numeros es: {numero1 - numero2}")
#             print(par_impar(numero1 - numero2))
#             print(positivo_negativo(numero1 - numero2))
#             print(entero_decimal(numero1 - numero2))
#             print("--------------------------------")
#         case 3:
#             print(f"La multiplicacion de los numeros es: {numero1 * numero2}")
#             print(par_impar(numero1 * numero2))
#             print(positivo_negativo(numero1 * numero2))
#             print(entero_decimal(numero1 * numero2))
#             print("--------------------------------")

#         case 4:
#             print(f"La division de los numeros es: {numero1 / numero2}")
#             print(par_impar(numero1 / numero2))
#             print(positivo_negativo(numero1 / numero2))
#             print(entero_decimal(numero1 / numero2))
#             print("--------------------------------")
#         case _:
#             print("Opcion invalida")
    
# opcion_menu(operacion)

# 11 - Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo. El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias:

# Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
# Triángulo Equilátero: tres lados iguales;
# Triángulo Isósceles: dos lados iguales;
# Triángulo Escaleno: tres lados diferentes.
# 12 - Un establecimiento está vendiendo combustibles con descuentos variables. Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 15 litros, el descuento será del 3% por litro. En caso contrario, será del 5% por litro. El precio por litro de diésel es de R$ 2,00 y el precio por litro de etanol es de R$ 1,70. Escribe un programa que lea la cantidad de litros vendidos y el tipo de combustible (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. Ten en cuenta algunas sugerencias:

# El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor del descuento.
# El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro por la cantidad de litros menos el valor del descuento resultante del cálculo.
# 13 - En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas anuales para ayudar a la dirección en la toma de decisiones. El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual. A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:

# Para una variación superior al 20%: bonificación para el equipo de ventas.
# Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
# Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
# Para bonificaciones inferiores al -10%: recorte de gastos.












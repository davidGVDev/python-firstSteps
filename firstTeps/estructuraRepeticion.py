# contador = 1

# while contador <= 10:
#     print(contador)
#     contador += 1

# bucle for

# for i in range(1, 11):
#     print(i)


# Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y seguridad. Un número primo es aquel que es divisible solo por sí mismo y por 1. 
# Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.

numero = int(input("Ingresa un numero entero: "))

if numero <= 1:
    print("El numero no es primo")
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("El numero no es primo")
            break
    else:
        print("El numero es primo")


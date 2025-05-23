"""
1 - Crea un programa que tenga la siguiente lista con los gastos de una empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Con estos valores, crea un programa que calcule el promedio de gastos. Sugerencia: usa las funciones integradas sum() y len().

2 - Con los mismos datos de la pregunta anterior, determina cuántas compras se realizaron por encima de 3000 reales y calcula el porcentaje con respecto al total de compras.

3 - Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].

4 - Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado.

5 - Crea un programa que, al ingresar un número cualquiera, genere una lista que contenga todos los números primos entre 1 y el número ingresado.

6 - Escribe un programa que pida una fecha, especificando el día, mes y año, y determine si es válida para su análisis.

Momento para los proyectos

7 - Para un estudio sobre la multiplicación de bacterias en una colonia, se recopiló el número de bacterias multiplicadas por día y se puede observar a continuación: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Con estos valores, crea un código que genere una lista que contenga el porcentaje de crecimiento de bacterias por día, comparando el número de bacterias en cada día con el número de bacterias del día anterior. Sugerencia: para calcular el porcentaje de crecimiento, utiliza la siguiente ecuación: 100 * (muestra_actual - muestra_anterior) / muestra_anterior.

8 - Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados por números enteros, sabiendo que los productos con ID par son dulces y los que tienen ID impar son amargos. Crea un código que recoja 10 IDs. Luego, calcula y muestra la cantidad de productos dulces y amargos.

9 - Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas. Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide con el resultado. Cada pregunta vale un punto y hay opciones A, B, C o D.
Resultado del examen:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B

10 - Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año. Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista. Luego, calcula el promedio anual de las temperaturas y muestra todas las temperaturas por encima del promedio anual y en qué mes ocurrieron, mostrando los meses por su nombre (Enero, Febrero, etc.).

11 - Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos. Los datos de ventas se han almacenado en un diccionario:
{'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}
Escribe un código que calcule el total de ventas y el producto más vendido.

12 - Se realizó una encuesta de mercado para decidir cuál diseño de marca infantil es más atractivo para los niños. Los votos de la encuesta se pueden ver a continuación:
Tabla de votos de la marca
Diseño 1 - 1334 votos
Diseño 2 - 982 votos
Diseño 3 - 1751 votos
Diseño 4 - 210 votos
Diseño 5 - 1811 votos
Adapta los datos proporcionados a una estructura de diccionario. A partir de ello, informa el diseño ganador y el porcentaje de votos recibidos.

13 - Los empleados de un departamento de tu empresa recibirán una bonificación del 10% de su salario debido a un excelente rendimiento del equipo. El departamento de finanzas ha solicitado tu ayuda para verificar las consecuencias financieras de esta bonificación en los recursos. Se te ha enviado una lista con los salarios que recibirán la bonificación: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. La bonificación de cada empleado no puede ser inferior a 200. En el código, convierte cada uno de los salarios en claves de un diccionario y la bonificación de cada salario en el valor correspondiente. Luego, informa el gasto total en bonificaciones, cuántos empleados recibieron la bonificación mínima y cuál fue el valor más alto de la bonificación proporcionada.

14 - Un equipo de científicos de datos está estudiando la diversidad biológica en un bosque. El equipo recopiló información sobre el número de especies de plantas y animales en cada área del bosque y almacenó estos datos en un diccionario. En él, la clave describe el área de los datos y los valores en las listas corresponden a las especies de plantas y animales en esas áreas, respectivamente.
{'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}
Escribe un código para calcular el promedio de especies por área e identificar el área con la mayor diversidad biológica. Sugerencia: utiliza las funciones incorporadas sum() y len().

15 - El departamento de Recursos Humanos de tu empresa te pidió ayuda para analizar las edades de los colaboradores de 4 sectores de la empresa. Para ello, te proporcionaron los siguientes datos:
{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
Dado que cada sector tiene 10 colaboradores, construye un código que calcule la media de edad de cada sector, la edad media general entre todos los sectores y cuántas personas están por encima de la edad media general.
"""
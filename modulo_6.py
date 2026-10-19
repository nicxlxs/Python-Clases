
#Clase 7 - Matrices y listas de listas de python

#Una matris es una lista que contiene otras listas, 
# parecido a las tablas de excel

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]


# Se accede a un elemento de una matriz asi:
# matriz[fila][columna]

# print(matriz[0][0])


# Modificar un elemento
# matriz[1][1] = 500


# Recorrer matrices


#Usamos bucles anidados

# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

#Imprimir cada elemento de la matriz por filas
# for fila in matriz:
#     for elemento in fila:
#         print(elemento)


# Imprimir la matriz en formato tabla
# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")
#     print()


# Recorriendo matrices usando indices

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j])



# Modificar todos los elementos

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         matriz[i][j] = matriz[i][j] * 2






#Sumar todos los elementos

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# suma = 0

# for fila in matriz:
#     for numero in fila:
#         suma += numero

# print(suma)



#Buscar un elemento

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# buscado = 50
# encontrado = False


# for fila in matriz:
#     for numero in fila:
#         if numero == buscado:
#             encontrado = True
#             break

#     if encontrado:
#         break


# if encontrado:
#     print("Número encontrado")
# else:
#     print("Número no encontrado")




#Buscar la posicion

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# buscado = 50

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if matriz[i][j] == buscado:
#             print(f"Encontrado en fila {i}, columna {j}")




# Matrices + funciones

# def mostrar_matriz(matriz):
#     for fila in matriz:
#         for numero in fila:
#             print(numero, end = " ")
#         print()


# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# mostrar_matriz(matriz)



#Ejercicios de la clase 7


# Ejercicio 31 — Crear y acceder

# Crea esta matriz:

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# Muestra:

# 10
# 50
# 90
# 30
# 70

# Utiliza:

# matriz[fila][columna]

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# print(matriz[0][0])
# print(matriz[1][1])
# print(matriz[2][2])
# print(matriz[0][2])
# print(matriz[2][0])



# Ejercicio 32 — Modificar

# Usa:

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# Modifica:

# 10 → 100
# 50 → 500
# 90 → 900

# Después muestra la matriz.

# Resultado:

# 100 20  30
# 40  500 60
# 70  80  900

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]


# matriz[0][0]=100
# matriz[1][1]=500
# matriz[2][2]=900


# for fila in matriz:
#     for numero in fila:
#         print(numero , end= " ")
#     print()


# Ejercicio 33 — Recorrer matriz

# Crea:

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Utiliza dos for para mostrar:

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# for fila in matriz:
#     for numero in fila:
#         print(numero)


# Ejercicio 34 — Mostrar como tabla

# Utiliza la misma matriz.

# Debe mostrar:

# 1 2 3
# 4 5 6
# 7 8 9

# Utiliza:

# print(numero, end=" ")

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# for fila in matriz:
#     for numero in fila:
#         print(numero, end= " ")
#     print()




# Ejercicio 35 — Sumar matriz

# Crea:

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# Calcula manualmente la suma utilizando:

# acumulador
# +
# for
# +
# for

# No uses:

# sum()

# Resultado:

# 450


# def suma_matriz(matriz):
#     suma = 0
#     for fila in matriz:
#         for numero in fila:
#             suma += numero
#     return suma

# def mostrar(suma):
#     print(f'La suma total es: {suma}')


# def main():

#     matriz = [
#         [10, 20, 30],
#         [40, 50, 60],
#         [70, 80, 90]
#     ]

#     v_suma =suma_matriz(matriz)
#     mostrar(v_suma)


# main()



# Ejercicio 36 — Contar pares

# Usa:

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Calcula:

# Cantidad de pares
# Cantidad de impares

# Utiliza contadores.

# def contar_pares_impares(matriz):

#     count_pares = 0
#     count_impares = 0

#     for fila in matriz:
#         for numero in fila:
#             if numero % 2 == 0:
#                 count_pares += 1
#             else:
#                 count_impares += 1

#     return count_pares, count_impares

# def mostrar(pares, impares):
#     print(f'Hay un total de {pares} pares')
#     print(f'Hay un total de {impares} impares')




# def main():
#     matriz = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]

#     v_count_pares, v_count_impares = contar_pares_impares(matriz)
#     mostrar(v_count_pares, v_count_impares)


# main()



# Ejercicio 37 — Buscar número

# Usa:

# matriz = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# Pide un número al usuario.

# Sin utilizar:

# in

# determina si existe.

# Utiliza:

# for
# for
# if
# bandera
# break

# def pedir_numero():
#     while True:
#         try:
#             numero = int(input('Ingrese un numero: '))
#             break
#         except ValueError:
#             print('Numero no valido')
#             continue
#     return numero


# def buscar(matriz, numero):

#     estado = False

#     for fila in matriz:
#         for elemento in fila:
#             if elemento == numero:
#                 estado = True
#                 break

#         if estado:
#             break
#     return estado


# def mostrar(estado):

#     if estado:
#         print('Su numero fue encontrado')
#     else:
#         print('Su numero no fue encontrado')

# def main():

#     matriz = [
#         [10, 20, 30],
#         [40, 50, 60],
#         [70, 80, 90]
#     ]

#     v_numero = pedir_numero()
#     v_estado = buscar(matriz, v_numero)
#     mostrar(v_estado)

# main()


# Ejercicio 38 — Buscar posición

# Pide un número al usuario.

# Si existe, muestra:

# Número encontrado
# Fila: X
# Columna: Y

# Si no existe:

# Número no encontrado

# Utiliza:

# range(len())

# y:

# matriz[i][j]


# def pedir_numero():
#     while True:
#         try:
#             numero = int(input('Ingrese un numero: '))
#             break
#         except ValueError:
#             print('Numero no valido')
#             continue
#     return numero



# def buscar_posicion(matriz, numero):

#     encontrado = False
#     fila = None
#     columna = None


#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             if matriz[i][j] == numero:
#                 fila = i
#                 columna = j
#                 encontrado = True
#                 break
#         if encontrado:
#             break

#     return encontrado, fila , columna


# def mostrar(encontrado, fila, columna):
#     if encontrado:
#         print("Número encontrado")
#         print(f"Fila: {fila}")
#         print(f"Columna: {columna}")
#     else:
#         print("Número no encontrado")

# def main():

#     matriz = [
#         [10, 20, 30],
#         [40, 50, 60],
#         [70, 80, 90]
#     ]

#     v_numero = pedir_numero()
#     v_encontrado, v_fila, v_columna = buscar_posicion(matriz,v_numero)
#     mostrar(v_encontrado,v_fila, v_columna)

# main()


# Ejercicio 39 — Función mostrar_matriz()

# Crea:

# def mostrar_matriz(matriz):

# La función debe mostrar cualquier matriz que reciba.

# Por ejemplo:

# matriz1 = [
#     [1, 2],
#     [3, 4]
# ]

# matriz2 = [
#     [10, 20, 30],
#     [40, 50, 60]
# ]

# La misma función debe poder mostrar ambas.



# def mostrar_matriz(matriz):
#     for fila in matriz:
#         for elemento in fila:
#             print(elemento, end=" ")
#         print()


# def main():

#     matriz1 = [
#         [1, 2],
#         [3, 4]
#     ]

#     matriz2 = [
#     [10, 20, 30],
#     [40, 50, 60]
#     ]

#     mostrar_matriz(matriz1)
#     mostrar_matriz(matriz2)

# main()



# Ejercicio 40 — Mini sistema de matriz

# Este será el ejercicio final de la clase.

# Crea un programa con:

# crear_matriz()
# mostrar_matriz()
# sumar_matriz()
# contar_pares()
# buscar_numero()
# main()

# El programa debe trabajar con una matriz de:

# 3 filas × 3 columnas

# Y mostrar un menú:

# ===== MENÚ =====

# 1. Mostrar matriz
# 2. Sumar elementos
# 3. Contar pares
# 4. Buscar número
# 5. Salir

# Por ejemplo:

# Matriz:

# 10 20 30
# 40 50 60
# 70 80 90

# Elige una opción: 2

# La suma es: 450
# Condiciones

# No utilices todavía:

# sum()
# max()
# min()


def pedir_numero(mensaje):
    while True: 
        try:
            numero = int(input(mensaje))
            break
        except ValueError:
            print('Numero ingresado no valido')
            continue
    return numero


# Desconmentar para usar cuando pidamos al usuario que cree una matriz
# def pedir_filas_columnas():

#     filas = pedir_numero("¿Cuántas filas tendrá la matriz?: ")
#     columnas = pedir_numero("¿Cuántas columnas tendrá la matriz?: ")
#     return filas, columnas


# Funcion para crear una matriz de cualquier tamano
# def crear_matriz_tamano(matriz):
#     v_filas ,  v_columnas = pedir_filas_columnas()

#     for i in range(v_filas):
#         fila_actual = []

#         for j in range(v_columnas):
#             numero = pedir_numero(f'Ingrese el numero para la posicion [{i}][{j}]: ')
#             fila_actual.append(numero)
#         matriz.append(fila_actual)
#     return matriz


# def crear_matriz(matriz):
#     v_filas = 3  
#     v_columnas = 3
#     print(f"\n--- Creando una matriz de {v_filas}x{v_columnas} ---")

#     for i in range(v_filas):
#         fila_actual = []
#         for j in range(v_columnas):
#             numero = pedir_numero(f'Ingrese el numero para la posicion [{i}][{j}]: ')
#             fila_actual.append(numero)
#         matriz.append(fila_actual)
#     return matriz


# def mostrar_matriz(matriz):
#     print("\n--- Tu Matriz ---")
#     for fila in matriz:
#         for elemento in fila:
#             print(elemento, end=' ')
#         print('')

# def sumar_matriz(matriz):

#     suma = 0

#     for fila in matriz:
#         for elemento in fila:
#             suma += elemento
#     return suma

# def contar_pares(matriz):

#     count_pares = 0

#     for fila in matriz:
#         for numero in fila:
#             if numero % 2 == 0 :
#                 count_pares += 1
#     return count_pares

# def buscar_numero(matriz):
#     numero = pedir_numero('Ingrese el numero que quiere buscar en la matriz: ')
#     encontrado = False

#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             if matriz[i][j] == numero:
#                 print(f'¡Su número {numero} fue encontrado en la posición [{i}][{j}]!')
#                 encontrado = True

#     if not encontrado:
#         print(f'El número {numero} no se encuentra en la matriz.')

#     return encontrado


# def menu():
#     print('=====MENU=====')
#     print('1.- Mostrar matriz')
#     print('2.- Sumar elementos')
#     print('3.- Contar pares')
#     print('4.- Buscar numero')
#     print('5.- Salir')

# def main():

#     matriz = []

#     crear_matriz(matriz)

#     while True:
#         menu()
#         choice = pedir_numero('Ingrese una opcion: ')

#         if choice == 5:
#             print('Saliendo del programa...')
#             break

#         if choice in [1,2,3,4]:
#             match choice:
#                 case 1:
#                     mostrar_matriz(matriz)
                    
#                 case 2:
#                     v_suma=sumar_matriz(matriz)
#                     print(f'La suma es: {v_suma}')

#                 case 3:
#                     v_count_pares = contar_pares(matriz)
#                     print(f'La cantidad de pares es: {v_count_pares}')

#                 case 4:
#                     buscar_numero(matriz)

#         else:
#             print('Numero ingresado no es una opcion')

# main()








































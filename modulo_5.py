#Listas

# numeros = [10,20,30,40,50]

# frutas = ["manzana", "pera", "uva"]




#Para agregar elementos de la lista usamos append()
# numeros = []

# numeros.append(10)
# numeros.append(20)
# numeros.append(30)

# print(numeros)


#Para eliminar un elemento usando su contenido usamos remove()
# frutas.remove("pera")


# Para eliminar por posicion usamos pop()
# frutas.pop(1)

#len para saber cuantos elementos tiene la lista
# for i in range(len(frutas)):
#     print(f"Índice: {i}")
#     print(f"Fruta: {frutas[i]}")


# for i in range(len(numeros)): #---> esto es para usar los indices
#     print(f'Indice: {i}')
#     print(f'Numero: {numeros[i]}')


# in Para encontrar elementos en la lista
# if 'uva' in frutas:
#     print('Encontramos la uva')

# if "sandía" not in frutas:
#     print("La sandía no está")


# count() Contar elementos
# print(numeros.count(10))



#Para encontrar la posicion usamos index()
# posicion = frutas.index("pera")

# print(posicion)


#Para sumar numeros usamos sum()
# total = sum(numeros)

# print(total)


#Para encontrar maximo y minimo usamos max() min()

# print(max(numeros))
# print(min(numeros))


#Para hallar promedio

# promedio =  sum(numeros) / len(numeros)

# print(promedio)



# Listas + Input

# Le pedimos al usuario ingresar 5 numeros

# numeros = []


# for i in range(5):
#     numero = int(input('Ingrese un numero: '))
#     numeros.append(numero)


# print(numeros)



# Lista + funcion

# def calcular_promedio(numeros):
#     if not numeros:
#         return 0
#     return sum(numeros)/len(numeros)


# def agregar_numero(numeros,numero):
#     numeros.append(numero)

# def agregar_numero_input(numeros):
#     cantidad = int(input('Cuantos numeros quieres agregar?: '))

#     for i in range(cantidad):
#         try: 
#             numero = int(input('Ingrese un numero: '))
#             numeros.append(numero)

#         except ValueError:
#             print('Numero ingresado invalidp')
#     return numeros


# # --- Flujo del programa ---
# notas = [15, 18, 12, 17]

# # 1. Agregamos el número fijo (13)
# agregar_numero(notas, 13)

# # 2. Agregamos los números del usuario (Ej: agregamos un 10 y un 20)
# agregar_numero_input(notas)

# # 3. Calculamos el promedio AL FINAL, con todos los datos cargados
# promedio = calcular_promedio(notas)

# # 4. Mostramos los resultados
# print("Lista final de notas:", notas)
# print("Promedio final:", promedio)



#Ejercicios


#Ejercicios 1 Crear y acceder
# Crea una lista llamada:

# frutas

# con 5 frutas.

# Después muestra:

# La primera fruta.
# La tercera fruta.
# La última fruta.

# frutas = ['manzana', 'pera','uva','platano','naranja']


# print(frutas[0])
# print(frutas[2])
# print(frutas[-1])



#Ejercicio 2 - Modificar

# Crea:

# numeros = [10, 20, 30, 40, 50]

# Cambia:

# 10 → 100
# 30 → 300
# 50 → 500

# Después imprime la lista.


# numeros = [10, 20, 30, 40, 50]

# numeros[0] = 100
# numeros[2] = 300
# numeros[4] = 500


# print(numeros)


#Ejercicio 3 - Agregar

# Comienza con:

# numeros = []

# Utilizando append() agrega:

# 10
# 20
# 30
# 40
# 50

# Después imprime la lista.


# numeros = []

# numeros.append(10)
# numeros.append(20)
# numeros.append(30)
# numeros.append(40)
# numeros.append(50)


# print(numeros)



# Ejercicio 4 — Eliminar

# Utiliza:

# frutas = ["manzana", "pera", "uva", "plátano", "naranja"]

# Haz:

# Elimina "uva" utilizando remove().
# Elimina "naranja" utilizando pop().

# Después imprime la lista.


# frutas = ["manzana", "pera", "uva", "plátano", "naranja"]

# frutas.remove('uva')
# frutas.pop(-1)


# print(frutas)




# Ejercicio 5 — Recorrer

# Crea una lista:

# numeros = [5, 10, 15, 20, 25]

# Recórrela utilizando:

# for

# y muestra cada número.



# numeros = [5, 10, 15, 20, 25]

# for i in numeros:
#     print(f'{i}')


# Ejercicio 6 — Contar

# Crea:

# numeros = [2, 5, 2, 8, 2, 10, 5]

# Muestra:

# Cuántos elementos tiene la lista.
# Cuántas veces aparece 2.
# Cuántas veces aparece 5.


# numeros = [2, 5, 2, 8, 2, 10, 5]


# print(len(numeros))

# print(numeros.count(2))
# print(numeros.count(5))


# Ejercicio 7 — Estadísticas

# Crea:

# numeros = [15, 8, 23, 42, 11, 7, 30]

# Calcula:

# Suma
# Promedio
# Mayor
# Menor

# Utiliza:

# sum()
# len()
# max()
# min()


# numeros = [15, 8, 23, 42, 11, 7, 30]

# suma = sum(numeros)

# promedio = suma / len(numeros) 

# print(suma)
# print(round(promedio,2))
# print(max(numeros))
# print(min(numeros))



# Ejercicio 8 — Buscar

# Crea una lista de nombres:

# nombres = ["Omar", "Nicolas", "Juan", "Pedro", "Luis"]

# Pide al usuario un nombre y determina si está en la lista.

# Debes utilizar:

# in


# def pedir_numero():
#     new_nombre = input('Ingrese un nombre: ')
#     return new_nombre


# def verificar_nombre(lista_nombres):

#     nombre_a_buscar = pedir_numero()

#     if nombre_a_buscar in lista_nombres:
#         print('El nombre que usted ingreso esta en la lista') 
#     else:
#         print('El nombre que usted ingreso no esta en la lista') 



# nombres = ["Omar", "Nicolas", "Juan", "Pedro", "Luis"]


# verificar_nombre(nombres)




# Ejercicio 9 — Construir una lista

# Pide al usuario 5 números.

# Cada número debe guardarse en una lista utilizando:

# append()

# Al terminar muestra:

# Lista completa
# Suma
# Promedio
# Mayor
# Menor

# Aquí vas a combinar:

# input
# +
# for
# +
# append
# +
# lista
# +
# sum
# +
# len
# +
# max
# +
# min

# def pedir_numero(lista_numeros):
#     while len(lista_numeros) < 5:
#         try:
#             new_number = int(input(f'{len(lista_numeros) + 1}.- Ingrese un número: '))
#             lista_numeros.append(new_number)
#         except ValueError:
#             print('El valor ingresado no es válido. Intente de nuevo.')
#     return lista_numeros


# def calcular_promedio(lista_numeros):
#     suma_total = sum(lista_numeros)
#     promedio = suma_total/len(lista_numeros)

#     return suma_total, promedio

# def mostrar(lista_numeros):
#     print("\n--- RESULTADOS ---")
#     print(f'Lista completa: {lista_numeros}')

#     suma_total, promedio = calcular_promedio(lista_numeros)


#     print(f'La suma total es: {suma_total}')
#     print(f'El promedio es: {promedio:.2f}') 
#     print(f'El max numero es: {max(lista_numeros)}')
#     print(f'El minimo numero es: {min(lista_numeros)}')


# def main():

#     numeros = []

#     pedir_numero(numeros)
#     mostrar(numeros)

# main()



# Ejercicio 10 — Contar pares

# Crea una lista con 10 números.

# Recórrela utilizando un for y determina:

# Cantidad de pares
# Cantidad de impares

# Aquí quiero que vuelvas a utilizar los contadores que aprendiste en bucles.


# def calcular_pares_impares(lista_numeros):

#     cantidad_pares = 0
#     cantidad_impares = 0

#     for numero in lista_numeros:
#         if numero % 2 == 0:
#             cantidad_pares += 1
#         else:
#             cantidad_impares += 1    

#     return cantidad_pares , cantidad_impares

# def mostrar(lista_numeros):

#     cantidad_pares, cantidad_impares = calcular_pares_impares(lista_numeros)

#     print(f'Cantidad de numeros pares: {cantidad_pares}')
#     print(f'Cantidad de numeros impares: {cantidad_impares}')

# def main():

#     numeros = [1,2,3,4,5,6,7,8,9,10,11]

#     mostrar(numeros)


# main()


# Ejercicio 11 — Buscar manualmente

# Crea una lista de números:

# numeros = [10, 25, 30, 45, 50, 60]

# Pide un número al usuario.

# Sin utilizar:

# in

# determina si el número existe en la lista.

# Debes utilizar:

# for
# if
# bandera booleana
# break



# numeros = [10, 25, 30, 45, 50, 60]


# buscado = int(input('Ingrese un numero para buscarlo: '))

# estado = False

# for numero in numeros:
#     if numero == buscado:
#         estado = True
#         break   
    

# if estado:
#     print('Numero encontrado')
# else:
#     print('Numero no encontrado')


# Ejercicio 12 — Encontrar posición

# Usa:

# nombres = ["Omar", "Juan", "Pedro", "Luis", "Nicolas"]

# Pide un nombre al usuario.

# Sin utilizar:

# .index()

# muestra su posición.

# Si no existe, muestra:

# Nombre no encontrado

# Debes utilizar:

# range(len())
# índices



# nombres = ["Omar", "Juan", "Pedro", "Luis", "Nicolas"]


# buscado = input('Ingrese un nombre para encontrar su posicion: ')

# estado = False
# posicion = -1
# for i in range(len(nombres)):
#      if nombres[i] == buscado:
#         estado = True
#         posicion = i
#         break

# if estado:
#     print('Nombre encontrado')
#     print(f'Esta en la posicion: {posicion}')
# else:
#     print('Nombre no encontrado')



# Ejercicio 13 — Mayor manual

# Crea:

# numeros = [15, 8, 23, 42, 11, 50, 7]

# Sin utilizar:

# max()

# encuentra el número mayor.

# Utiliza:

# mayor = numeros[0]
# for
# if



# numeros = [15, 8, 23, 42, 11, 50, 7]

# mayor = numeros[0]



# for i in numeros[1:]:
#     if i > mayor:
#         mayor = i
    

# print(f'EL numero mayor es: {mayor}')





# Ejercicio 14 — Menor manual

# Usa la misma lista:

# numeros = [15, 8, 23, 42, 11, 50, 7]

# Sin utilizar:

# min()

# encuentra el número menor.


# numeros = [15, 8, 23, 42, 11, 50, 7]

# menor = numeros[0]



# for i in numeros[1:]:
#     if i < menor:
#         menor = i
    

# print(f'EL numero menor es: {menor}')




# Ejercicio 15 — Estadísticas manuales

# Crea una función:

# def calcular_estadisticas(lista):

# Debe calcular manualmente:

# Suma
# Promedio
# Mayor
# Menor

# No puedes utilizar:

# sum()
# max()
# min()

# Debe retornar los cuatro valores.






# def calcular_estadisticas(lista):


#     if not lista:
#          return 0 , 0 , None, None

#     suma = 0
#     cantidad = 0
#     mayor = lista[0]
#     menor = lista[0]


#     for elemento in lista:
#         suma += elemento
#         cantidad += 1

#         if elemento > mayor:
#             mayor = elemento


#         if elemento < menor:
#             menor = elemento


#     promedio = suma/cantidad

#     return suma, promedio, mayor,menor
        






# def main():

#     numeros = [1,2,3,4,5,6,7,8,9,10]

#     v_suma, v_promedio, v_mayor, v_menor = calcular_estadisticas(numeros)
    
#     print('Resultados totales')
#     print(f'La suma total es: {v_suma}')
#     print(f'El promedio total es: {v_promedio}')
#     print(f'El maximo numero es: {v_mayor}')
#     print(f'El minimo numero es: {v_menor}')

# main()



#Ejercicio 16 — Filtrar pares

# Crea:

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crea una nueva lista llamada:

# pares

# Recorre numeros.

# Solo agrega los números pares a pares.

# No modifiques la lista original.

# Resultado esperado:

# [2, 4, 6, 8, 10]



# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pares = []



# for numero in numeros:
#     if numero % 2 == 0 :
#         pares.append(numero)

# print(pares)




# Ejercicio 17 — Filtrar positivos

# Usa:

# numeros = [-10, 5, -3, 20, 0, 8, -1]

# Crea una nueva lista:

# positivos

# Agrega solamente los números mayores que 0.




# numeros = [-10, 5, -3, 20, 0, 8, -1]



# positivos = []



# for numero in numeros:
#     if numero > 0:
#         positivos.append(numero)


# print(positivos)




# Ejercicio 18 — Duplicar lista

# Usa:

# numeros = [2, 4, 6, 8, 10]

# Modifica cada elemento para que sea el doble.

# Resultado:

# [4, 8, 12, 16, 20]

# Aquí debes utilizar:

# range(len(numeros))

# porque necesitas modificar los elementos mediante sus índices.

# numeros = [2, 4, 6, 8, 10]

# for i in range(len(numeros)):
#     numeros[i] = numeros[i] *2 


# print(numeros)


# Ejercicio 19 — Copias de listas

# Crea:

# lista1 = [10, 20, 30]

# Crea una copia correcta llamada:

# lista2

# Después:

# Agrega 40 a lista2.
# Muestra ambas listas.

# El resultado debe demostrar que:

# lista1 no cambió
# lista2 sí cambió


# lista1 = [10, 20, 30]

# lista2 = lista1.copy()

# lista2.append(40)

# print(lista1)
# print(lista2)


# Ejercicio 20 — Mini analizador de números

# Crea un programa con estas funciones:

# pedir_numeros()
# calcular_estadisticas()
# obtener_pares()
# mostrar_resultado()
# main()

# El programa debe:

# Pedir 5 números al usuario.
# Guardarlos en una lista.
# Calcular manualmente:
# suma
# promedio
# mayor
# menor
# Crear una nueva lista solo con números pares.
# Mostrar todos los resultados.

# No utilices:

# sum()
# max()
# min()



# def pedir_numeros():

#     lista = []

#     for i in range(1,6):
#         numero = int(input(f'{i}.- Ingrese un numero: '))
#         lista.append(numero)

#     return lista


# def calcular_estadisticas(lista):

#     suma = 0
#     mayor = lista[0]
#     menor = lista[0]

#     for i in lista:
#         suma = suma + i

#         if i > mayor:
#             mayor = i

#         if i < menor:
#             menor = i



#     promedio = suma/len(lista)

#     return suma, promedio, mayor, menor
        
        



# def obtener_pares(lista):

#     new_lista = []

#     for i in lista:
#         if i % 2 == 0:
#             new_lista.append(i)

#     return new_lista


# def mostrar_resultado(suma , promedio , mayor , menor, pares):
    
#     print(':::::::Resultado::::::')
#     print(f'La suma total de los numeros es: {suma}')
#     print(f'El promedio total de los numeros es: {promedio} ')
#     print(f'EL numero mayor es: {mayor}')
#     print(f'EL numero menor es: {menor}')
#     print(f'Los numeros pares son : {pares}')
    





# def main():

#     numeros = pedir_numeros()
#     pares = obtener_pares(numeros)

#     v_suma , v_promedio , v_mayor , v_menor = calcular_estadisticas(numeros)

#     mostrar_resultado(v_suma , v_promedio , v_mayor , v_menor, pares)
    


# main()





# CONTRASENA = '12845'




# # Rango de todas las combinaciones posibles de 5 dígitos
# for combinacion in range(10000, 100000):
#     ingreso = str(combinacion)
    
#     if ingreso == CONTRASENA:
#         print(f'¡Contraseña rota por fuerza bruta! Era: {ingreso}')
#         break




# Para insertar un objeto en una posicion especifica usamos insert()

# numeros = [10, 20, 40]

# numeros.insert(2, 30)



# Para unir lista usamos extend()


# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]


# lista1.extend(lista2)


# print(lista1)



# append() agrega toda la lista como un solo elemento a la nueva lista
# extend() Agregó los elementos individualmente.



# Para ordenar una lista usamos sort()
# sort() modifica la lista original.

# numeros = [50, 10, 30, 20, 40]

# print(numeros)

# numeros.sort()

# print(numeros)


# #Ordenar de forma descendente

# numeros.sort(reverse=True)

# print(numeros)

#Para invertir una lista usamos reverse() 


# numeros = [1, 2, 3, 4, 5]

# numeros.reverse()

# print(numeros)


#Importante no significa necesariamente ordenar de mayor a menor.
# Simplemente invierte el orden actual.


#Slicing sirve para extraer partes de una lista


# numeros = [10, 20, 30, 40, 50]



# print(numeros[:4])


# enumerate() sirve para enumerar una lista con su indice - indeice + valor


# nombres = ['Nicolas', 'Omar', 'Nautilus']

# for i in range(len(nombres)):
#     print(i,nombres[i])


# for indice, nombre in enumerate(nombres):
#     print(indice, nombre)


#Introduccion a listas de listas


#Lista normal:

# numeros = [10, 20, 30]




#Una lista puede contener otras listas:

# numeros = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]





#Ejercicios


# Ejercicio 21 — Insertar elementos

# Crea:

# numeros = [10, 20, 40, 50]

# Utilizando insert():

# Inserta 30 entre 20 y 40.
# Inserta 5 al inicio.

# Resultado:

# [5, 10, 20, 30, 40, 50]


# def insertar_elemento(lista,indice, numero):
#     lista.insert(indice, numero)
#     return lista

# def mostrar(lista):
#     print(lista)

# def main():

#     numeros = [10, 20, 40, 50]

#     insertar_elemento(numeros,2,30)
#     insertar_elemento(numeros,0,5)
#     mostrar(numeros)


# main()


# Ejercicio 22 — Unir listas

# Crea:

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]

# Utiliza:

# extend()

# Une ambas listas.

# Después imprime:

# [1, 2, 3, 4, 5, 6]

# Luego responde con tu propio código:

# ¿Cuál es la diferencia entre append(lista2) y extend(lista2)?


# def unir_listas(lista1,lista2):
#     lista1.extend(lista2)
#     return lista1


# def mostrar(lista):
#     print(lista)

# def main():
#     lista1 = [1, 2, 3]
#     lista2 = [4, 5, 6]

#     unir_listas(lista1,lista2)
#     mostrar(lista1)

#     #La diferencia entre append(lista2) y extend(lista2) es que
#     #append(lista2) agrega toda la lista 2 como un elemento a la lista 1
#     #mientras que extend(lista2) agregas los elementos de la lista 2 a la lista 1

#     print("\n--- Demostración de la diferencia ---")
    
#     a = [1, 2, 3]
#     b = [4, 5, 6]
    
#     a.append(b)  # Agrega la lista completa como un solo elemento (sublista)
#     print("Resultado con append():")
#     mostrar(a)   # Imprime: [1, 2, 3, [4, 5, 6]]



# main()


# Ejercicio 23 — Ordenar

# Crea:

# numeros = [45, 10, 80, 25, 60]

# Muestra:

# La lista ordenada de menor a mayor.
# La lista ordenada de mayor a menor.

# Importante: recuerda que sort() modifica la lista.


# def ordenar_menor_a_mayor(lista):
#     copia = lista.copy()
#     copia.sort()
#     return copia


# def ordenar_mayor_a_menor(lista):
#     copia = lista.copy()
#     copia.sort(reverse = True)
#     return copia

# def mostrar(ascendente, descendente):
#     print(f'Lista ordenada de forma ascendete: {ascendente}')
#     print(f'Lista ordenada de forma descendete: {descendente}')



# def main():

#     numeros = [45, 10, 80, 25, 60]

#     ascendente = ordenar_menor_a_mayor(numeros)
#     descendente = ordenar_mayor_a_menor(numeros)


#     mostrar(ascendente,descendente)



# main()



# Ejercicio 24 — Invertir

# Crea:

# numeros = [1, 2, 3, 4, 5]

# Utiliza:

# reverse()

# Resultado esperado:

# [5, 4, 3, 2, 1]

# Después prueba con:

# numeros = [10, 50, 20, 30]

# e invierte la lista.

# Quiero que observes que reverse():

# NO ordena
# SOLO invierte


# def invertir(lista):
#     lista.reverse()
#     return lista


# def mostrar(lista):

#     print(f'Lista invertida: {lista}')

# def main():
    
#     numeros = [1, 2, 3, 4, 5]

#     numeros2 = [10, 50, 20, 30]

#     #Lista de numeros
#     invertir(numeros)
#     mostrar(numeros)


#     #Lista de numeros2
#     invertir(numeros2)
#     mostrar(numeros2)


# main()



# Ejercicio 25 — Vaciar lista

# Crea:

# frutas = ["manzana", "pera", "uva"]

# Muestra la lista.

# Después utiliza:

# clear()

# Vuelve a mostrarla.


# Ejercicio 25 — Vaciar lista

# Crea:

# frutas = ["manzana", "pera", "uva"]

# Muestra la lista.

# Después utiliza:

# clear()

# Vuelve a mostrarla.


# def vaciar_lista(lista):
#     lista.clear()
#     return lista

# def mostrar(lista):
#     print(f'Lista: {lista}')

# def main():
#     frutas = ["manzana", "pera", "uva"]

#     mostrar(frutas)
#     vaciar_lista(frutas)
#     mostrar(frutas)


# main()


# Ejercicio 26 — Buscar posición

# Crea:

# nombres = ["Omar", "Juan", "Pedro", "Luis", "Nicolas"]

# Pide un nombre.

# Utiliza:

# in
# index()

# Si existe:

# El nombre se encuentra en la posición X

# Si no existe:

# Nombre no encontrado

# def pedir_nombre():
#     nombre = input('Ingrese un nombre para buscar: ').strip()
#     return nombre

# def buscar_por_posicion(lista, nombre):
#     if nombre in lista:
#         return lista.index(nombre)
#     else:
#         return None

# def mostrar(posicion):

#     if posicion is not None:
#         print(f'El nombre se encuentra en la posicion {posicion}')
#     else:
#         print('Nombre no encontrado')

# def main():

#     nombres = ["Omar", "Juan", "Pedro", "Luis", "Nicolas"]

#     v_nombre = pedir_nombre()
#     v_posicion =buscar_por_posicion(nombres,v_nombre)
#     mostrar(v_posicion)

# main()
    

# Ejercicio 27 — Slicing básico

# Usa:

# numeros = [10, 20, 30, 40, 50, 60, 70]

# Muestra:

# Los primeros 3 números.
# Los últimos 3 números.
# Los números desde la posición 2 hasta la posición 5.
# Todos los números excepto el primero.
# Todos los números excepto el último.


# numeros = [10, 20, 30, 40, 50, 60, 70]

# # 1. Los primeros 3 números (índices 0, 1, 2)
# print("Primeros 3:", numeros[:3])  # Salida: [10, 20, 30]

# # 2. Los últimos 3 números (usando índice negativo)
# print("Últimos 3:", numeros[-3:])  # Salida: [50, 60, 70]

# # 3. Los números desde la posición 2 hasta la posición 5
# # Nota: Va del índice 2 al 5 de forma inclusiva, por eso el tope es 6
# print("De la 2 a la 5:", numeros[2:6])  # Salida: [30, 40, 50, 60]

# # 4. Todos los números excepto el primero
# print("Excepto el primero:", numeros[1:])  # Salida: [20, 30, 40, 50, 60, 70]

# # 5. Todos los números excepto el último
# print("Excepto el último:", numeros[:-1])  # Salida: [10, 20, 30, 40, 50, 60]




# Ejercicio 28 — Slicing con saltos

# Usa:

# numeros = [10, 20, 30, 40, 50, 60, 70, 80]

# Muestra:

# Un número sí y uno no.
# Los elementos que están en posiciones pares.
# Los elementos que están en posiciones impares.
# La lista invertida utilizando slicing.

# Para el último, intenta descubrir qué significa:

# numeros[::-1]

# numeros = [10, 20, 30, 40, 50, 60, 70, 80]

# # 1. Un número sí y uno no (avanza de 2 en 2 desde el principio)
# print("Uno sí y uno no:", numeros[::2])  # Salida: [10, 30, 50, 70]

# # 2. Los elementos que están en posiciones (índices) pares
# # Nota: En Python el índice 0 es par, por lo que coincide con el anterior
# print("Índices pares:", numeros[::2])    # Salida: [10, 30, 50, 70]

# # 3. Los elementos que están en posiciones (índices) impares
# # Empezamos explícitamente desde el índice 1 y saltamos de 2 en 2
# print("Índices impares:", numeros[1::2])  # Salida: [20, 40, 60, 80]

# # 4. La lista invertida utilizando slicing
# print("Lista invertida:", numeros[::-1]) # Salida: [80, 70, 60, 50, 40, 30, 20, 10]

# Ejercicio 29 — Enumerate

# Usa:

# frutas = ["manzana", "pera", "uva", "plátano"]

# Utiliza:

# enumerate()

# para mostrar:

# Posición 0: manzana
# Posición 1: pera
# Posición 2: uva
# Posición 3: plátano


# def mostrar(lista):
#     for indice, nombres in enumerate(lista):
#         print(f'Posicion {indice}: {nombres}')

# def main():

#     frutas = ["manzana", "pera", "uva", "plátano"]

#     mostrar(frutas)


# main()



# Ejercicio 30 — Mini gestor de lista

# Crea un programa con estas funciones:

# mostrar_lista()
# agregar_elemento()
# insertar_elemento()
# eliminar_elemento()
# ordenar_lista()
# main()

# El programa debe tener un menú:

# 1. Mostrar lista
# 2. Agregar elemento
# 3. Insertar elemento en posición
# 4. Eliminar elemento
# 5. Ordenar lista
# 6. Salir

# Utiliza una lista de números.

# La idea es que combines todo lo aprendido:

# Listas
# Funciones
# Menús
# Bucles
# Condicionales
# append()
# insert()
# remove()
# sort()


# def mostrar_lista(lista):
#     print(lista)

# def pedir_elemento():
#     try:
#         elemento = int(input('Ingrese un elemento a la lista: '))

#     except ValueError:
#         print('Error: La posición debe ser un número entero válido.')


#     return elemento

# def pedir_posicion():
#     try:
#         posicion = int(input('Ingrese en que posicion quiere agregar el nuevo elemento: '))

#     except ValueError:
#         print('Error: La posición debe ser un número entero válido.')
#     return posicion



# def agregar_elemento(lista, elemento):
#     lista.append(elemento)

# def insertar_elemento(lista,elemento, posicion):
#     lista.insert(posicion, elemento)
#     return lista

# def eliminar_elemento(lista):
#     elemento = int(input('Ingresa un elemento exacto que desea eliminar: '))

#     if elemento in lista:
#         lista.remove(elemento)
#         print(f"'{elemento}' ha sido eliminado.")
#     else:
#         print("El elemento no se encuentra en la lista.")
#     return lista

# def ordenar_lista(lista):
#     lista.sort()

# def menu():
#     print(':::::Menu:::::')
#     print('1.- Mostrar lista')
#     print('2.- Agregar elemento')
#     print('3.- Insertar elemento en posicion')
#     print('4.- Eliminar elemento')
#     print('5.- Ordenar lista')
#     print('6.- salir')


# def main():

#     numeros = []
#     while True:
#         menu()
#         try:
#             choice = int(input('Ingrse una opcion: '))

#         except ValueError:
#             print('Opción no válida. Ingrese un número.')
#             continue

#         if choice == 6:
#             print("Saliendo del programa...")
#             break

#         if choice in [1, 2, 3, 4,5]:

#             match choice:
#                 case 1: 
#                     mostrar_lista(numeros)

#                 case 2:
#                     v_elemento = pedir_elemento()
#                     agregar_elemento(numeros,v_elemento)

#                 case 3:
#                     v_elemento = pedir_elemento()
#                     v_posicion = pedir_posicion()
#                     insertar_elemento(numeros,v_elemento, v_posicion)

#                 case 4:
#                     eliminar_elemento(numeros)

#                 case 5:
#                     ordenar_lista(numeros)

#         else: 
#             print("Opción fuera de rango (1-6).")
            

# main()



















































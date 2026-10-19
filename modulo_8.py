

#Clase sobre Tuplas


# Una tupla es parecido a una liste, 
# pero no se puede modificar despues de ser creada


# Se representa con ()

# persona = ("Nicolas", 22, "Software")

# Para acceder a sus elementos

# print(persona[0])
# print(persona[1])
# print(persona[2])


# Para recorrerla

# for dato in persona:
#     print(dato)


# Para desempaquetar los datos de la tupla

# persona = ("Nicolas", 22, "Software")

# nombre, edad, carrera = persona

# print(nombre)
# print(edad)
# print(carrera)


# Tuplas y funciones

# def calcular(a, b):
#     suma = a + b
#     resta = a - b

#     return suma, resta

# resultado = calcular(10, 5)

# resultado sera un tupla: (15,5)


# Tambien podemos hacerlo asi:
# suma, resta = calcular(10, 5)
# Esto se llama desempaquetado.



# Que es un set?
# un set es un conjunto de elementos que no permite duplicados
# Se crea con {}

# Set sin duplicados
# numeros = {10, 20, 30, 40}
# print(numeros)
# Imprime {10,20,30,40}




# Set con duplicados
# numeros = {10, 20, 20, 30, 30, 30}
# print(numeros)
# Imprime {10, 20, 30} sin los duplicados


# Para que sirve un set?

# De esta lista obten los valores unicos y sin repeticion

# carreras = [
#     "Software",
#     "Sistemas",
#     "Software",
#     "Industrial",
#     "Sistemas",
#     "Software"
# ]

# Usamos el set para quitar los duplicados de la lista
# carreras_unicas = set(carreras)

# print(carreras_unicas)

# Obtendrás los valores sin repetición.

# Esto es muy útil para:

# eliminar duplicados
# obtener valores únicos
# comparar grupos
# encontrar elementos comunes
# encontrar diferencias



# Agregar elementos en el set usamos .add()
# numeros = {10, 20, 30}
# numeros.add(40)
# Si intentamos agregar algo que ya existe, este no se duplica


# Eliminar elementos de un set usamos .remove(), 
# pero si el elemento no existe puede producir un error
# numeros.remove(20)

# Tambien podemos usar discard() para eliminar un elemento de un set, 
# este no genera un error si el elemento no existe
# numeros.discard(100)


# Para buscar dentro de un set usamos in, igual que con las listas
# numeros = {10, 20, 30}

# if 20 in numeros:
#     print("El número existe")


# Operaciones entre conjuntos
# Tenemos:
# grupo_a = {"Python", "Java", "C#", "SQL"}
# grupo_b = {"Java", "Python", "JavaScript", "SQL"}


# Union
# elementos que estan en A o B:

# union = grupo_a.union(grupo_b)

# print(union)
# Me imprime los elementos que tienen ambos


# Tambien se puede utulizar:
# union = grupo_a | grupo_b



# Interseccion
# Elementos que estan en ambos conjuntos:
# comunes = grupo_a.intersection(grupo_b)
# print(comunes)
# Imprime los elementos que estan ambos

# Tambien se puede utilizar:
# comunes = grupo_a & grupo_b



# Diferencia
# Elementos que estan en A pero no estan en B:
# diferencia = grupo_a.difference(grupo_b)
# print(diferencia)
# Imprime los elementos que estan en A pero no en B

# Tambien podemos utilizar:
# diferencia = grupo_a - grupo_b

# y al contrario
# grupo_b - grupo_a


# Por ultimo, un set funciona como una lista para acceder por posicion
# Porque un set no esta pensado para trabajar mediante indices

# Si necesitas: 
# numeros[0]
# numeros[1]
# numeros[2]
# probablemente quieres una lista.


# Si necesitas:
# "Quiero saber que elementos unicos existen"
# probablemente quieres un set.



# Ejercicios -  Clase 10


# Ejercicio 61 — Crear y acceder a una tupla

# Crea una tupla llamada datos que contenga:

# nombre
# edad
# carrera

# Después muestra cada elemento individualmente.

# datos = ("Nicolas", 20 , "Ingenieria de Software")

# print(datos[0])
# print(datos[1])
# print(datos[2])


# Ejercicio 62 — Recorrer una tupla
# Crea una tupla con 5 números.

# Recórrela usando for y muestra cada número.

# numero = (10,20,30,40,50)

# for elemento in numero:
#     print(elemento)





# Ejercicio 63 — Desempaquetado

# Crea:

# persona = ("Carlos", 25, "Ingeniería")

# Desempaqueta la tupla en:

# nombre
# edad
# carrera

# Después muestra las tres variables.

# persona = ("Carlos", 25, "Ingeniería")

# nombre,edad,carrera = persona

# print(nombre)
# print(edad)
# print(carrera)




# Ejercicio 64 — Función que retorna una tupla

# Crea una función:

# calcular(a, b)

# Debe retornar:

# suma
# resta
# multiplicación

# Luego utiliza desempaquetado:

# suma, resta, multiplicacion = calcular(10, 5)

# Y muestra los resultados.


# def calcular(a,b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a*b
#     return suma, resta, multiplicacion

# def main():


#     suma, resta, multiplicacion = calcular(10, 5)    

#     # Mostramos los resultados individuales
#     print("Suma:", suma)
#     print("Resta:", resta)
#     print("Multiplicación:", multiplicacion)


# main()


# Ejercicio 65 — Eliminar duplicados

# Tienes:

# numeros = [10, 20, 20, 30, 10, 40, 30, 50]

# Utiliza un set para eliminar los números repetidos.

# El resultado debe contener solamente valores únicos.


# def eliminar_repetidos(lista):
#     numeros_unicos = set(lista)
#     return numeros_unicos

# def main():
#     numeros = [10, 20, 20, 30, 10, 40, 30, 50]

#     v_numeros_unicos = eliminar_repetidos(numeros)

#     print(v_numeros_unicos)


# main()


# Ejercicio 66 — Agregar, eliminar y buscar

# Crea:

# numeros = {10, 20, 30}

# Realiza:

# Agrega 40.
# Elimina 20.
# Busca si existe 30.
# Busca si existe 100.
# Muestra el conjunto final.


# def main():
#     numeros = {10, 20, 30}

#     numeros.add(40)
#     print(numeros)

#     numeros.discard(20)

#     if 30 in numeros:
#         print('El numero 30 existe en el set')
#     else:
#         print('El numero 30 no existe en el set')


#     if 100 in numeros:
#         print('El numero 100 existe en el set')
#     else:
#         print('El numero 100 no existe en el set')

#     print(numeros)

# main()





# Ejercicio 67 — Operaciones entre sets

# Crea:

# grupo_a = {"Python", "Java", "C#", "SQL"}
# grupo_b = {"Python", "JavaScript", "SQL", "PHP"}

# Obtén:

# Unión.
# Intersección.
# Elementos solamente de grupo_a.
# Elementos solamente de grupo_b.

# def calcular(grupo_a, grupo_b):
#     union = grupo_a.union(grupo_b)
#     interseccion = grupo_a.intersection(grupo_b)
#     diferencia_1 = grupo_a.difference(grupo_b)
#     diferencia_2 = grupo_b.difference(grupo_a)

#     return union,interseccion,diferencia_1,diferencia_2

# def mostrar(grupo_a, grupo_b):
#     v_union,v_interseccion,v_diferencia_1,v_diferencia_2 = calcular(grupo_a, grupo_b)
#     print('==================================================')
#     print('::: RESULTADOS DE LAS OPERACIONES ENTRE SETS :::')
#     print('==================================================')
#     print(f'1. Unión (Todos los lenguajes):\n   {v_union}\n')
#     print(f'2. Intersección (Lenguajes en ambos grupos):\n   {v_interseccion}\n')    
#     print(f'3. Solo en Grupo A (Java y C#):\n   {v_diferencia_1}\n')
#     print(f'4. Solo en Grupo B (JavaScript y PHP):\n   {v_diferencia_2}')
#     print('==================================================')


# def main():

#     grupo_a = {"Python", "Java", "C#", "SQL"}
#     grupo_b = {"Python", "JavaScript", "SQL", "PHP"}

#     mostrar(grupo_a,grupo_b)
# main()



# Ejercicio 68 — Carreras únicas

# Tienes:

# carreras = [
#     "Software",
#     "Sistemas",
#     "Software",
#     "Industrial",
#     "Sistemas",
#     "Software",
#     "Industrial"
# ]

# Crea una función:

# obtener_carreras_unicas(carreras)

# Debe retornar un set con las carreras sin repetir.

# def obtener_carreras_unicas(carreras):
#     carreras_unicas = set(carreras)
#     return carreras_unicas

# def mostrar(carreras, v_carreras_unicas):
#     print('==================================================')
#     print('::: REPORTE DE CARRERAS UNIVERSITARIAS :::')
#     print('==================================================')
#     print(f'Lista original (con repetidos):\n   {carreras}\n')
#     print(f'Carreras únicas encontradas (Set):\n   {v_carreras_unicas}')
#     print('==================================================')


# def main():
#     carreras = [
#         "Software",
#         "Sistemas",
#         "Software",
#         "Industrial",
#         "Sistemas",
#         "Software",
#         "Industrial"
#     ]

#     v_carreras_unicas = obtener_carreras_unicas(carreras)

#     mostrar(carreras, v_carreras_unicas)

# main()



# Ejercicio 69 — Comparar estudiantes

# Tenemos dos grupos:

# grupo_a = {"Carlos", "Maria", "Pedro", "Luis"}
# grupo_b = {"Maria", "Pedro", "Ana", "Jose"}

# Crea funciones para obtener:

# estudiantes que están en ambos grupos
# estudiantes solamente del grupo A
# estudiantes solamente del grupo B

# Intenta que cada operación esté dentro de una función diferente.


# def estudiantes_ambos_grupos(grupo_a,grupo_b):
#     estudiantes_comunes = grupo_a.intersection(grupo_b)
#     return estudiantes_comunes



# def estudiantes_en_a(grupo_a,grupo_b):
#     estudiantes_a = grupo_a.difference(grupo_b)
#     return estudiantes_a



# def estudiantes_en_b(grupo_a,grupo_b):
#     estudiantes_b = grupo_b.difference(grupo_a)
#     return estudiantes_b

# def mostrar(grupo_a, grupo_b):
#     v_estudiantes_comunes = estudiantes_ambos_grupos(grupo_a, grupo_b)
#     v_estudiantes_a = estudiantes_en_a(grupo_a, grupo_b)
#     v_estudiantes_b = estudiantes_en_b(grupo_a, grupo_b)

#     print('==================================================')
#     print('::: COMPARACIÓN DE GRUPOS DE ESTUDIANTES :::')
#     print('==================================================')
#     print(f'1. Están en ambos grupos (Intersección):\n   {v_estudiantes_comunes}\n')
#     print(f'2. Solamente pertenecen al Grupo A:\n   {v_estudiantes_a}\n')
#     print(f'3. Solamente pertenecen al Grupo B:\n   {v_estudiantes_b}')
#     print('==================================================')



# def main():

#     grupo_a = {"Carlos", "Maria", "Pedro", "Luis"}
#     grupo_b = {"Maria", "Pedro", "Ana", "Jose"}

#     mostrar(grupo_a,grupo_b)

# main()




# Ejercicio 70 — Mini sistema

# Vamos a combinar lo que ya sabes:

# listas + diccionarios + funciones + sets + tuplas.

# Crea un sistema de estudiantes.

# Cada estudiante debe tener:

# {
#     "nombre": "...",
#     "edad": 20,
#     "carrera": "Software"
# }

# El sistema debe permitir:

# 1. Agregar estudiante
# 2. Mostrar estudiantes
# 3. Buscar estudiante
# 4. Mostrar carreras únicas
# 5. Mostrar estudiantes de una carrera
# 6. Salir
# Requisitos

# Para agregar estudiantes, utiliza una lista de diccionarios.

# Ejemplo:

# estudiantes = [
#     {
#         "nombre": "Carlos",
#         "edad": 20,
#         "carrera": "Software"
#     },
#     {
#         "nombre": "Maria",
#         "edad": 22,
#         "carrera": "Industrial"
#     }
# ]

# Para la opción "carreras únicas", debes utilizar un set.

# Por ejemplo:

# Carreras disponibles:
# - Software
# - Industrial
# - Sistemas

# Y debes separar la lógica en funciones:

# agregar_estudiante()
# mostrar_estudiantes()
# buscar_estudiante()
# obtener_carreras_unicas()
# buscar_por_carrera()
# main()

# No necesitas hacer todavía un CRUD completo con actualizar/eliminar; eso ya lo hiciste en la clase anterior.


# def pedir_usuario(mensaje):
#     elemento = input(mensaje)
#     return elemento

# def agregar_estudiante(lista):
#     v_nombre = pedir_usuario('Digite el nombre del estudiante: ')
#     v_carrera = pedir_usuario('Digite la carrera del estudiante: ')
#     while True:
#         try:
#             v_edad = int(pedir_usuario('Ingrese la edad del alumno: '))
#             if v_edad < 0:
#                 print('La edad no puede ser un número negativo.')
#                 continue
#             break
#         except ValueError:
#             print('Edad ingresada incorrecta. Ingrese un número entero.')

#     lista.append({
#         "nombre": v_nombre,
#         "edad": v_edad,
#         "carrera": v_carrera
#     }
#     )

#     return lista

# def mostrar_estudiantes(lista):
#     if not lista:
#         print("No hay estudiantes registrados.\n")
#         return
    
#     for diccionario in lista:
#         print(f"::::Datos del alumnmo {diccionario['nombre']}::::")
#         print(f"Nombre del estudiante: {diccionario['nombre']}")
#         print(f"Edad del estudiante: {diccionario['edad']} ")
#         print(f"Carrera del estudiante: {diccionario['carrera']} ")
#         print(f" ")


# def buscar_estudiante(lista):
#     v_nombre = pedir_usuario('Ingrese el nombre del estudiante que desea buscar: ')
#     encontrado = False # Bandera para saber si existe

#     for diccionario in lista:
#         if v_nombre.lower() == diccionario['nombre'].lower():
#             print('\n=== Alumno Encontrado ===')
#             print(f"Nombre: {diccionario['nombre']}")
#             print(f"Edad: {diccionario['edad']}")
#             print(f"Carrera: {diccionario['carrera']}\n")
#             encontrado = True
#             break # Rompemos el ciclo si ya lo encontramos
            
#     if not encontrado:
#         print('Alumno no encontrado.\n')



# def obtener_carreras_unicas(lista):
#     # carreras_unicas = set(lista)
#     carreras = []
#     for diccionario in lista:
#         carreras.append(diccionario['carrera'])

#     carreras_unicas = set(carreras)
#     return carreras_unicas

# def mostrar_carreras_unicas(lista):
#     v_carreras_unicas = obtener_carreras_unicas(lista)

#     if not v_carreras_unicas:
#         print("No hay carreras registradas.\n")
#         return

#     print(f"\n::: Carreras disponibles en el sistema :::")
#     for carrera in v_carreras_unicas:
#         print(f"- {carrera}")
#     print(" ") 




# def buscar_por_carrera(lista):
#     v_carrera = pedir_usuario('Ingrese la carrera del estudiante que desea buscar: ')
#     alumnos_por_carrera = []

#     for diccionario in lista:
#         if v_carrera.lower() == diccionario['carrera'].lower():
#             alumnos_por_carrera.append(diccionario)

#     return alumnos_por_carrera

# def mostrar_estudiante_segun_carrera(lista):
#     v_alumnos_por_carrera = buscar_por_carrera(lista)

#     if not v_alumnos_por_carrera:
#         print("No se encontraron alumnos en esa carrera.\n")
#         return

#     print(f"\n::: Alumnos de la carrera :::")
#     for diccionario in v_alumnos_por_carrera:
#         print(f"::::Datos del alumno {diccionario['nombre']}::::")
#         print(f"Nombre del estudiante: {diccionario['nombre']}")
#         print(f"Edad del estudiante: {diccionario['edad']} ")
#         print(f"Carrera del estudiante: {diccionario['carrera']} ")
#         print(f" ")


# def menu():
#     print("::::Sistema Alumno::::")
#     print("1. Agregar estudiante")
#     print("2. Mostrar estudiantes")
#     print("3. Buscar estudiante")
#     print("4. Mostrar carreras únicas")
#     print("5. Mostrar estudiantes de una carrera")
#     print("6. Salir")
#     print(" ")




# def main():
#     estudiantes = [
#     {
#         "nombre": "Carlos",
#         "edad": 20,
#         "carrera": "Software"
#     },
#     {
#         "nombre": "Maria",
#         "edad": 22,
#         "carrera": "Industrial"
#     }
#     ]


#     while True:
#         menu()
#         try:
#             choice = int(pedir_usuario('Seleccione una opción: '))
#         except ValueError:
#             print("Error: Por favor, ingrese un número del 1 al 6.\n")
#             continue

#         match choice:
#             case 1:
#                 agregar_estudiante(estudiantes)
#             case 2:
#                 mostrar_estudiantes(estudiantes)
#             case 3:
#                 buscar_estudiante(estudiantes)
#             case 4:
#                 mostrar_carreras_unicas(estudiantes)
#             case 5:
#                 mostrar_estudiante_segun_carrera(estudiantes)
#             case 6:
#                 break
            

# main()






































































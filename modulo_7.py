# Listas

# persona = {
#     "nombre": "Nicolas", 
#     "edad": 22,
#     "carrera": "Ingeniería de Software"
# }

# print(persona["nombre"])


# Acceder a valores

# print(producto["nombre"])
# print(producto["precio"])
# print(producto["stock"])


# Modificar un valor

# producto["precio"] = 2300


#   Agregar nuevos datos

# producto["marca"] = "Lenovo"

# Eliminar datos
# Usamos del 
# del producto["stock"]

# También podemos utilizar .pop():
# producto.pop("marca")

#La diferencia importante es que pop() 
# puede devolver el valor eliminado:

# producto = {
#     "nombre": "Laptop",
#     "precio": 2300,
#     "stock": 10,
#     "marca": "Lenovo"
# }

# marca = producto.pop("marca")

# print(marca)


# Si la clave no existe podemos usar .get()
# para que devuelva None y no keyerror
# tambien .get() busca la clave, si no la encuentra devuelve el segundo texto
# resultado = alumno.get(v_clave, "El dato no existe")


# Para comprobar que existe una clave usamos in
# if "precio" in producto:
#     print("La clave existe")

# Recorrer un diccionario
# for clave in producto:
#     print(clave)
# También podemos utilizar:
# for clave in producto.keys():
#     print(clave)


# Recorrer los valores
# Para esto usamos .value()

# for valor in producto.values():
#     print(valor)


# Para recorrer claves y valores

# for clave, valor in producto.items():
#     print(clave, ":", valor)


# .items() piensa como dame cada clave junto con su valor


# Se puede guardar listas en el diccionario


# Podemos tener varios usuarios
# Usuario es una lista que contiene varios diccionarios
# usuarios = [
#     {
#         "nombre": "Carlos",
#         "edad": 21
#     },
#     {
#         "nombre": "Maria",
#         "edad": 23
#     },
#     {
#         "nombre": "Pedro",
#         "edad": 20
#     }
# ]

# for usuario in usuarios:
#     print(usuario["nombre"], usuario["edad"])

# print(usuarios[0]["nombre"])



# Tambien podemos usar funciones con diccionarios

# persona es el diccionario
# def mostrar_persona(persona):
#     print("Nombre:", persona["nombre"])
#     print("Edad:", persona["edad"])


# persona = {
#     "nombre": "Nicolas",
#     "edad": 22
# }

# mostrar_persona(persona)


# Importante la diferencia entre una lista y un diccionario
# Una lista se accede mediante posicion
# Un diccionario se accede mediante claves (keys)



# Ejercicio clase 8

# Ejercicio 41 — Crear diccionario

# Crea un diccionario llamado persona con:

# nombre
# edad
# carrera
# ciudad

# Luego imprime cada dato.


# persona = {
#     "nombre": "Nicolas" ,
#     "edad": 19,
#     "carrera": "Ingenieria de software",
#     "ciudad": "Lima" 


# }

# for clave, valor in persona.items():
#     print(f"{clave.capitalize()}: {valor}")


# Ejercicio 42 — Modificar

# Crea:

# producto = {
#     "nombre": "Mouse",
#     "precio": 50,
#     "stock": 20
# }

# Modifica:

# precio → 45
# stock → 15

# Luego muestra el diccionario.

# def modificar(producto):
#     producto['precio'] = 45
#     producto['stock'] = 15

# def mostrar(producto):
#     for clave, valor in producto.items():
#         print(f"{clave.capitalize()}: {valor}")




# def main():
#     producto = {
#         "nombre": "Mouse",
#         "precio": 50,
#         "stock": 20
#     }

#     modificar(producto)
#     mostrar(producto)


# main()



# Ejercicio 43 — Agregar

# Utilizando el diccionario anterior, agrega:

# marca → Logitech
# categoria → Accesorios

# def modificar(producto):
#     producto['precio'] = 45
#     producto['stock'] = 15
#     producto['marca'] = "Logitech"
#     producto['categoria'] = "Accesorios"



# def mostrar(producto):
#     for clave, valor in producto.items():
#         print(f"{clave.capitalize()}: {valor}")


# def main():
#     producto = {
#         "nombre": "Mouse",
#         "precio": 50,
#         "stock": 20
#     }

#     modificar(producto)
#     mostrar(producto)


# main()

# Ejercicio 44 — Eliminar

# Elimina la clave:

# stock

# Utiliza pop().

# def modificar(producto):
#     producto['precio'] = 45
#     producto['stock'] = 15
#     producto['marca'] = "Logitech"
#     producto['categoria'] = "Accesorios"



# def mostrar(producto):
#     for clave, valor in producto.items():
#         print(f"{clave.capitalize()}: {valor}")


# def eliminar(producto):
#     producto.pop("stock")


# def main():
#     producto = {
#         "nombre": "Mouse",
#         "precio": 50,
#         "stock": 20
#     }

#     modificar(producto)
#     eliminar(producto)
#     mostrar(producto)

# main()



# Ejercicio 45 — Buscar clave

# Crea un diccionario de un alumno:

# alumno = {
#     "nombre": "...",
#     "edad": ...,
#     "carrera": "...",
#     "promedio": ...
# }

# Pregunta al usuario qué dato quiere consultar.

# Ejemplo:

# Ingrese el dato que desea consultar: promedio

# Si existe, muestra el valor.

# Si no existe:

# El dato no existe

# Pista: utiliza .get().

# def pedir_usuario(mensaje):
#     clave = input(mensaje)
#     return clave

# def buscar_clave(alumno):
#     v_clave = pedir_usuario('Ingrese el dato que desea consultar: ')

#     if v_clave in alumno:
#         return v_clave
#     else:
#         return None


# def mostrar(alumno):
#     clave_encontrada = buscar_clave(alumno)        

#     if clave_encontrada: 
#         print(alumno.get(clave_encontrada))
#     else:
#         print("El dato no existe")




# def main():
#     alumno = {
#         "nombre": "Nicolas",
#         "edad": 22,
#         "carrera": "Ingenieria de software",
#         "promedio": 15
#     }

#     mostrar(alumno)

# main()




# Ejercicio 46 — Recorrer diccionario

# Crea un diccionario:

# notas = {
#     "Matematica": 15,
#     "Programacion": 18,
#     "Base de Datos": 16,
#     "Arquitectura": 17
# }

# Recorre el diccionario e imprime:

# Matematica : 15
# Programacion : 18
# ...

# Utiliza .items().

# def mostrar(diccionario):
#     for clave, valor in diccionario.items():
#         print(f"{clave}: {valor}")     



# def main():
#     notas = {
#         "Matematica": 15,
#         "Programacion": 18,
#         "Base de Datos": 16,
#         "Arquitectura": 17
#     }

#     mostrar(notas)

# main()



# Ejercicio 47 — Contar aprobados

# Utilizando el diccionario notas anterior:

# Recorre las notas.
# Cuenta cuántos cursos tienen nota >= 13.
# Cuenta cuántos tienen nota < 13.

# Resultado esperado:

# Cursos aprobados: 4
# Cursos desaprobados: 0


# def contar_aprobado_desaprobados(diccionario):
#     aprobados = 0
#     desaprobados = 0
#     for valor in diccionario.values():
#         if valor >= 13:
#             aprobados += 1
#         else: 
#             desaprobados += 1

#     return aprobados, desaprobados


# def mostrar(diccionario):
#     v_aprobados, v_desaprobados = contar_aprobado_desaprobados(diccionario) 

#     print(f'Cursos aprobados: {v_aprobados}')
#     print(f'Cursos desaprobados: {v_desaprobados}')



# def main():
#     notas = {
#         "Matematica": 15,
#         "Programacion": 18,
#         "Base de Datos": 16,
#         "Arquitectura": 17
#     }

    
#     mostrar(notas)

# main()


# Ejercicio 48 — Lista de personas

# Crea una lista de diccionarios:

# personas = [
#     {"nombre": "Ana", "edad": 20},
#     {"nombre": "Luis", "edad": 25},
#     {"nombre": "Pedro", "edad": 18},
#     {"nombre": "Maria", "edad": 30}
# ]

# Recorre la lista e imprime:

# Ana - 20
# Luis - 25
# Pedro - 18
# Maria - 30


# def mostrar(lista):
#     for elemento in lista:
#         print(f"{elemento['nombre']} - {elemento['edad']}")


# def main():
#     personas = [
#         {"nombre": "Ana", "edad": 20},
#         {"nombre": "Luis", "edad": 25},
#         {"nombre": "Pedro", "edad": 18},
#         {"nombre": "Maria", "edad": 30}
#     ]

#     mostrar(personas)

# main()



# Ejercicio 49 — Buscar persona

# Utilizando la lista anterior:

# Pregunta:

# Ingrese el nombre que desea buscar:

# Busca la persona.

# Si existe:

# Persona encontrada
# Nombre: Luis
# Edad: 25

# Si no:

# Persona no encontrada

# Pista: necesitarás combinar:

# for

# con:

# if

# y acceder a:

# persona["nombre"]


# def preguntar_usuario(mensaje):
#     valor = input(mensaje)
#     return valor


# def buscar_persona(lista):
#     nombre = preguntar_usuario('Ingrese el nombre que desea buscar: ')
#     nombre_formateado = nombre.capitalize()

#     for elemento in lista:
#         if nombre_formateado == elemento['nombre']:
#             return elemento['nombre'], elemento['edad'] 

#     return None, None
            

# def mostrar(lista):
#     v_nombre, v_edad = buscar_persona(lista)

#     if v_nombre:
#         print('Persona encontrada ')
#         print(f'Nombre: {v_nombre}')
#         print(f'Edad: {v_edad}')
#     else:
#         print('Persona no encontrada ')


# def main():
#     personas = [
#         {"nombre": "Ana", "edad": 20},
#         {"nombre": "Luis", "edad": 25},
#         {"nombre": "Pedro", "edad": 18},
#         {"nombre": "Maria", "edad": 30}
#     ]

#     mostrar(personas)

# main()


# 🚀 Ejercicio 50 — Mini sistema de alumnos

# Este será el ejercicio más importante de la clase.

# Crea un programa que maneje varios alumnos.

# Cada alumno tendrá:

# nombre
# edad
# carrera
# promedio

# La estructura será:

# alumnos = [
#     {
#         "nombre": "Carlos",
#         "edad": 21,
#         "carrera": "Software",
#         "promedio": 16
#     },
#     ...
# ]

# El programa debe tener funciones:

# 1. agregar_alumno()
# 2. mostrar_alumnos()
# 3. buscar_alumno()
# 4. calcular_promedio()
# 5. main()

# El menú podría ser:

# ===== SISTEMA DE ALUMNOS =====

# 1. Agregar alumno
# 2. Mostrar alumnos
# 3. Buscar alumno
# 4. Calcular promedio
# 5. Salir

# Seleccione una opción:
# Requisitos

# Agregar alumno

# Debe pedir los datos y agregar un nuevo diccionario a la lista.

# Mostrar alumnos

# Debe mostrar todos los alumnos.

# Buscar alumno

# Debe pedir un nombre y buscarlo.

# Calcular promedio

# Debe calcular el promedio de todos los alumnos.


# def pedir_usuario(mensaje):
#     elemento = input(mensaje)
#     return elemento

# def agregar_alumno(lista):

#     nombre = pedir_usuario('Ingrese el nombre del alumno: ')
#     carrera = pedir_usuario('Ingrese la carrera del alumno: ')
#     while True:
#         try:
#             edad = int(pedir_usuario('Ingrese la edad del alumno: '))
#             break
#         except ValueError:
#             print('Error: La edad debe ser un número entero. Intente de nuevo.')

#     while True:
#             try:
#                 promedio = int(pedir_usuario('Ingrese el promedio del alumno: '))
#                 break
#             except ValueError:
#                 print('Error: El promedio debe ser un número válido. Intente de nuevo.')

#     lista.append({
#     "nombre": nombre,
#     "edad": edad,
#     "carrera": carrera,
#     "promedio": promedio
#     })  
    
# def mostrar_alumnos(lista):
#     for diccionario in lista:
#         # CORRECCIÓN: Comillas dobles afuera y simples adentro
#         print(f"Información del alumno {diccionario['nombre']}")
#         print(f"Nombre: {diccionario['nombre']}")
#         print(f"Edad: {diccionario['edad']} ")
#         print(f"Carrera: {diccionario['carrera']}")
#         print(f"Promedio: {diccionario['promedio']} ")
#         print(' ')

# def buscar_alumno(lista):
#     v_nombre = pedir_usuario('Ingrese un nombre para buscar al alumno: ')
#     v_nombre_convertido = v_nombre.capitalize()
#     for diccionario in lista: 
#         if v_nombre_convertido == diccionario['nombre']:
#             return diccionario
#     return None

# def mostrar_alumno_encontrado(lista):
#     alumno = buscar_alumno(lista)

#     if alumno:
#         print(f"\nInformación del alumno {alumno['nombre']}")
#         print(f"Nombre: {alumno['nombre']}")
#         print(f"Edad: {alumno['edad']} ")
#         print(f"Carrera: {alumno['carrera']}")
#         print(f"Promedio: {alumno['promedio']} \n")
#     else: 
#         print('Alumno no encontrado en la base de datos\n')


# def calcular_promedio(lista):

#     if len(lista) == 0 :
#         return 0

#     # Promedio = suma de promedios/ len(lista)
#     suma_total = 0

#     for diccionario in lista:
#         suma_total += diccionario['promedio']

#     return suma_total/len(lista)

# def menu():

#     print('===== SISTEMA DE ALUMNOS =====')
#     print('1. Agregar alumno')
#     print('2. Mostrar alumnos')
#     print('3. Buscar alumno')
#     print('4. Calcular promedio')
#     print('5. Salir')

# def main():

#     alumnos = [
#         {
#             "nombre": "Carlos",
#             "edad": 21,
#             "carrera": "Software",
#             "promedio": 16
#         },

#         {
#             "nombre": "Nicolas",
#             "edad": 22,
#             "carrera": "Software",
#             "promedio": 18
#         },



#     ]



#     while True:
#         menu()

#         try:
#             choice = int(pedir_usuario('Seleccione una opción: '))
#         except ValueError:
#             print("Error: Por favor, ingrese un número del 1 al 5.\n")
#             continue

#         if choice == 5:
#             print('Saliendo del programa...')
#             break
#         if choice in [1,2,3,4]:
#             match choice:
#                 case 1:
#                     agregar_alumno(alumnos)
#                 case 2:
#                     mostrar_alumnos(alumnos)

#                 case 3:
#                     mostrar_alumno_encontrado(alumnos)

#                 case 4:
#                     print(f'El promedio general de todos los alumnos es: {calcular_promedio(alumnos)}')
#         else:
#             print("Error: Opción no válida. Intenta de nuevo.\n")

# main()

# Ejercicios de la clase 9}

# Ejercicio 51 — Mostrar alumnos

# Utiliza:

# alumnos = [
#     {"nombre": "Carlos", "edad": 21, "nota": 16},
#     {"nombre": "Maria", "edad": 22, "nota": 18},
#     {"nombre": "Pedro", "edad": 20, "nota": 12}
# ]

# Crea:

# mostrar_alumnos(alumnos)

# Debe mostrar:

# Carlos - 21 - 16
# Maria - 22 - 18
# Pedro - 20 - 12


# def mostrar_alumnos(alumnos):

#     for diccionario in alumnos:
#         print(f"{diccionario['nombre']} - {diccionario['edad']} - {diccionario['nota']}")
#         # print(f"Informacion del alumno {diccionario['nombre']} ")
#         # print(f"Nombre: {diccionario['nombre']} ")
#         # print(f"Edad: {diccionario['edad']} ")
#         # print(f"Nota: {diccionario['nota']} ")
#         # print(' ')


# def main():

#     alumnos = [
#         {"nombre": "Carlos", "edad": 21, "nota": 16},
#         {"nombre": "Maria", "edad": 22, "nota": 18},
#         {"nombre": "Pedro", "edad": 20, "nota": 12}
#     ]

#     mostrar_alumnos(alumnos)

# main()


# Ejercicio 52 — Buscar alumno

# Crea:

# buscar_alumno(alumnos, nombre)

# Debe devolver el diccionario completo.

# Ejemplo:

# alumno = buscar_alumno(alumnos, "Maria")

# Resultado:

# {
#     "nombre": "Maria",
#     "edad": 22,
#     "nota": 18
# }

# Si no existe:

# None



# def buscar_alumno(alumnos,nombre):

#     for alumno in alumnos:
#         if alumno['nombre'].lower() == nombre.lower():
#             return alumno
#     return None

# def mostrar(alumnos):
#     alumno = buscar_alumno(alumnos, "Maria")

#     if alumno is not None:
#         print(alumno)
#     else:
#         print('Estudiante no encontrado')





# def main():

#     alumnos = [
#         {"nombre": "Carlos", "edad": 21, "nota": 16},
#         {"nombre": "Maria", "edad": 22, "nota": 18},
#         {"nombre": "Pedro", "edad": 20, "nota": 12}
#     ]

#     mostrar(alumnos)
# main()


# Ejercicio 53 — Contar aprobados

# Crea:

# contar_aprobados(alumnos)

# Debe devolver la cantidad de alumnos con:

# nota >= 13


# def contar_aprobados(alumnos):

#     contador = 0

#     for alumno in alumnos:
#         if alumno['nota'] >= 13:
#             contador += 1

#     return contador

# def mostrar(alumnos):
#     v_contador = contar_aprobados(alumnos)

#     print(f'La cantidad de alumnos aprobado es: {v_contador}')




# def main():

#     alumnos = [
#         {"nombre": "Carlos", "edad": 21, "nota": 16},
#         {"nombre": "Maria", "edad": 22, "nota": 18},
#         {"nombre": "Pedro", "edad": 20, "nota": 12}
#     ]

#     mostrar(alumnos)
# main()




# Ejercicio 54 — Obtener aprobados

# Crea:

# obtener_aprobados(alumnos)

# Debe devolver una nueva lista solamente con los alumnos aprobados.


# def contar_aprobados(alumnos):

#     contador = 0

#     for alumno in alumnos:
#         if alumno['nota'] >= 13:
#             contador += 1

#     return contador

# def mostrar(alumnos):
#     v_contador = contar_aprobados(alumnos)

#     print(f'La cantidad de alumnos aprobado es: {v_contador}')




# def main():

#     alumnos = [
#         {"nombre": "Carlos", "edad": 21, "nota": 16},
#         {"nombre": "Maria", "edad": 22, "nota": 18},
#         {"nombre": "Pedro", "edad": 20, "nota": 12}
#     ]

#     mostrar(alumnos)
# main()



# Ejercicio 55 — Obtener mayor nota

# Crea:

# obtener_mejor_alumno(alumnos)

# Debe devolver el diccionario completo del alumno con mayor nota.

# def obtener_mejor_alumno(alumnos):

#     if len(alumnos) == 0:
#         return None

#     mejor = alumnos[0]


#     for alumno in alumnos:
#         if alumno['nota'] > mejor['nota']:
#             mejor = alumno

#     return mejor


# def mostrar(alumnos):
#     v_mejor = obtener_mejor_alumno(alumnos)

#     print('El alumno con mayor nota es: ')
#     print(f'{v_mejor}')




# def main():

#     alumnos = [
#         {"nombre": "Carlos", "edad": 21, "nota": 16},
#         {"nombre": "Maria", "edad": 22, "nota": 18},
#         {"nombre": "Pedro", "edad": 20, "nota": 12}
#     ]

#     mostrar(alumnos)
# main()



# Ejercicio 56 — Buscar por carrera

# Ahora los alumnos tendrán:

# alumnos = [
#     {"nombre": "Carlos", "edad": 21, "carrera": "Software"},
#     {"nombre": "Maria", "edad": 22, "carrera": "Software"},
#     {"nombre": "Pedro", "edad": 20, "carrera": "Sistemas"},
#     {"nombre": "Ana", "edad": 24, "carrera": "Industrial"}
# ]

# Crea:

# buscar_por_carrera(alumnos, carrera)

# Debe devolver una lista.

# Ejemplo:

# buscar_por_carrera(alumnos, "Software")

# debe devolver Carlos y Maria.


# def buscar_por_carrera(alumnos, carrera):

#     alumno_carrera = []
#     for alumno in alumnos:
#        if carrera.lower() == alumno['carrera'].lower():
#            alumno_carrera.append(alumno)
#     return alumno_carrera 

# def mostrar(alumnos):
#     v_alumnos = buscar_por_carrera(alumnos, "Software")

#     # Extraemos solo los nombres de los alumnos encontrados para mostrarlos bonito
#     nombres = [alumno['nombre'] for alumno in v_alumnos]
#     print(f"Los alumnos de esa carrera son: {', '.join(nombres)}")

# def main():

#     alumnos = [
#     {"nombre": "Carlos", "edad": 21, "carrera": "Software"},
#     {"nombre": "Maria", "edad": 22, "carrera": "Software"},
#     {"nombre": "Pedro", "edad": 20, "carrera": "Sistemas"},
#     {"nombre": "Ana", "edad": 24, "carrera": "Industrial"}
#     ]   

#     mostrar(alumnos)

# main()


# Ejercicio 57 — Actualizar alumno

# Crea:

# actualizar_edad(alumnos, nombre, nueva_edad)

# Debe modificar la edad del alumno.

# Debe devolver:

# True

# si encontró al alumno.

# Y:

# False

# si no lo encontró.


# def actualizar_edad(alumnos, nombre, nueva_edad):

#     for alumno in alumnos:
#         if alumno['nombre'].lower() == nombre.lower():
#             alumno['edad'] = nueva_edad
#             return True

#     return False


# def mostrar(alumnos):

#     resultado1 = actualizar_edad(alumnos, "Carlos", 30)
#     print(f"¿Se actualizó a Carlos?: {resultado1}")
    

#     resultado2 = actualizar_edad(alumnos, "Luis", 25)
#     print(f"¿Se actualizó a Luis?: {resultado2}")
    

#     print(f"\nLista de alumnos final:\n{alumnos}")

# def main():

#     alumnos = [
#     {"nombre": "Carlos", "edad": 21, "carrera": "Software"},
#     {"nombre": "Maria", "edad": 22, "carrera": "Software"},
#     {"nombre": "Pedro", "edad": 20, "carrera": "Sistemas"},
#     {"nombre": "Ana", "edad": 24, "carrera": "Industrial"}
#     ]   

#     mostrar(alumnos)
 
# main()


# Ejercicio 58 — Eliminar alumno

# Crea:

# eliminar_alumno(alumnos, nombre)

# Debe eliminar al alumno de la lista.

# También debe devolver:

# True

# o:

# False

# dependiendo de si encontró al alumno.

# def buscar_alumno_posicion(alumnos, nombre):

#     for i in range(len(alumnos)):
#         if alumnos[i]['nombre'].lower() == nombre.lower():
#             return i
#     return None    


# def eliminar_alumno(alumnos, nombre):

#     posicion = buscar_alumno_posicion(alumnos, nombre)

#     if posicion is not None :
#         alumnos.pop(posicion)
#         return True
    
#     return False

# def eliminar_alumno(alumnos, nombre):

#     for i in range(len(alumnos)):
#             if alumnos[i]['nombre'].lower() == nombre.lower():
#                 alumnos.pop(i)
#                 return True
#     return False    


# def mostrar(alumnos):

#     resultado1 = eliminar_alumno(alumnos, "Carlos")
#     print(f"¿Se eliminó a Carlos?: {resultado1}")
    
#     resultado2 = eliminar_alumno(alumnos, "Luis")
#     print(f"¿Se eliminó a Luis?: {resultado2}")
    
#     print(f"\nLista de alumnos final:\n{alumnos}")



# def main():

#     alumnos = [
#     {"nombre": "Carlos", "edad": 21, "carrera": "Software"},
#     {"nombre": "Maria", "edad": 22, "carrera": "Software"},
#     {"nombre": "Pedro", "edad": 20, "carrera": "Sistemas"},
#     {"nombre": "Ana", "edad": 24, "carrera": "Industrial"}
#     ]   

#     mostrar(alumnos)
 
# main()



# Ejercicio 59 — Estadísticas

# Crea:

# calcular_estadisticas(alumnos)

# Debe devolver:

# promedio
# mayor
# menor

# Por ejemplo:

# Promedio: 15.33
# Mayor: 18
# Menor: 12

# No utilices sum(), max() ni min().

# Hazlo manualmente como aprendiste en las clases anteriores.

# def calcular_estadisticas(alumnos):

#     if len(alumnos) == 0 :
#         return 0, 0 , 0

#     suma = 0
#     mayor = alumnos[0]['edad']
#     menor = alumnos[0]['edad']

#     for alumno in alumnos:

#         edad = alumno['edad']
#         suma += edad

#         if edad > mayor:
#             mayor = edad

#         if edad < menor:
#             menor = edad

#     promedio = suma/len(alumnos)

#     return promedio, mayor,menor
         

# def mostrar(alumnos):

#     v_promedio , v_mayor , v_menor = calcular_estadisticas(alumnos)

#     print("LAS ESTADISTICAS")
#     print(f"El promedio total de las edades es: {v_promedio:.2f}")
#     print(f"La edad mayor es: {v_mayor}")
#     print(f"La edad menor es: {v_menor}")





# def main():

#     alumnos = [
#     {"nombre": "Carlos", "edad": 21, "carrera": "Software"},
#     {"nombre": "Maria", "edad": 22, "carrera": "Software"},
#     {"nombre": "Pedro", "edad": 20, "carrera": "Sistemas"},
#     {"nombre": "Ana", "edad": 24, "carrera": "Industrial"}
#     ]   

#     mostrar(alumnos)
 
# main()


# 🚀 Ejercicio 60 — Mini sistema CRUD

# Este será el ejercicio principal de la clase.

# Crea un sistema:

# ===== SISTEMA DE ALUMNOS =====

# 1. Agregar alumno
# 2. Mostrar alumnos
# 3. Buscar alumno
# 4. Actualizar edad
# 5. Eliminar alumno
# 6. Mostrar aprobados
# 7. Mostrar estadísticas
# 8. Salir

# Cada alumno tendrá:

# nombre
# edad
# carrera
# nota

# Debes crear como mínimo:

# agregar_alumno()
# mostrar_alumnos()
# buscar_alumno()
# actualizar_edad()
# eliminar_alumno()
# obtener_aprobados()
# calcular_estadisticas()
# menu()
# main()
# La estructura debe ser:
# main()
#  │
#  ├── menu()
#  │
#  ├── agregar_alumno()
#  │
#  ├── mostrar_alumnos()
#  │
#  ├── buscar_alumno()
#  │
#  ├── actualizar_edad()
#  │
#  ├── eliminar_alumno()
#  │
#  ├── obtener_aprobados()
#  │
#  └── calcular_estadisticas()

# Aquí ya estarás construyendo un pequeño CRUD:

# C → Create → Crear
# R → Read   → Leer
# U → Update → Actualizar
# D → Delete → Eliminar

# Este concepto es fundamental en desarrollo de software y más adelante lo vamos a conectar directamente con bases de datos y APIs.


def pedir_usuario(mensaje):
    value = input(mensaje)
    return value


# def buscar_alumno_unificado(alumnos):
#     """
#     Función de búsqueda reutilizable para todo el CRUD.
#     Devuelve el ÍNDICE del alumno elegido o None si no hay resultados.
#     """
#     if len(alumnos) == 0:
#         print("No hay alumnos registrados.")
#         return None

#     print("\n--- CRITERIOS DE BÚSQUEDA ---")
#     print("1. Por Nombre")
#     print("2. Por Edad")
#     print("3. Por Carrera")
#     print("4. Por Nota")
    
#     opcion = pedir_usuario("Seleccione método de búsqueda (1-4): ")
#     coincidencias_indices = [] # Guardaremos los índices numéricos de los alumnos encontrados

#     # 1. Filtrar los índices según el criterio
#     match opcion:
#         case "1":
#             nombre_buscar = pedir_usuario("Ingrese el nombre: ").lower()
#             for i in range(len(alumnos)):
#                 if alumnos[i]['nombre'].lower() == nombre_buscar:
#                     coincidencias_indices.append(i)
#         case "2":
#             try:
#                 edad_buscar = int(pedir_usuario("Ingrese la edad: "))
#                 for i in range(len(alumnos)):
#                     if alumnos[i]['edad'] == edad_buscar:
#                         coincidencias_indices.append(i)
#             except ValueError:
#                 print("Error: Edad inválida.")
#                 return None
#         case "3":
#             carrera_buscar = pedir_usuario("Ingrese la carrera: ").lower()
#             for i in range(len(alumnos)):
#                 if alumnos[i]['carrera'].lower() == carrera_buscar:
#                     coincidencias_indices.append(i)
#         case "4":
#             try:
#                 nota_buscar = int(pedir_usuario("Ingrese la nota: "))
#                 for i in range(len(alumnos)):
#                     if alumnos[i]['nota'] == nota_buscar:
#                         coincidencias_indices.append(i)
#             except ValueError:
#                 print("Error: Nota inválida.")
#                 return None
#         case _:
#             print("Opción de búsqueda no válida.")
#             return None

#     # 2. Evaluar los resultados encontrados
#     if len(coincidencias_indices) == 0:
#         return None
        
#     # Si solo hay una coincidencia, la devolvemos directamente
#     if len(coincidencias_indices) == 1:
#         return coincidencias_indices[0]

#     # Si hay MÚLTIPLES coincidencias (ej. dos alumnos con la misma nota), el usuario desempata
#     print(f"\nSe encontraron {len(coincidencias_indices)} alumnos. Elija el número correcto:")
#     for opcion_num, idx in enumerate(coincidencias_indices, start=1):
#         al = alumnos[idx]
#         print(f"{opcion_num}. {al['nombre']} | Carrera: {al['carrera']} | Edad: {al['edad']} | Nota: {al['nota']}")
        
#     while True:
#         try:
#             seleccion = int(pedir_usuario("Seleccione el número de fila: "))
#             if 1 <= seleccion <= len(coincidencias_indices):
#                 # Devolvemos el índice real de la lista de alumnos
#                 return coincidencias_indices[seleccion - 1]
#             print("Número fuera de rango.")
#         except ValueError:
#             print("Ingrese un número entero.")


def agregar_alumno(alumnos):

    nombre = pedir_usuario('Ingrese el nombre del alumno: ')
    carrera = pedir_usuario('Ingrese la carrera del alumno: ')

    while True:
            try:
                edad = int(pedir_usuario('Ingrese la edad del alumno: '))
                if edad < 0:
                    print('La edad no puede ser un número negativo.')
                    continue
                break
            except ValueError:
             print('Edad ingresada incorrecta. Ingrese un número entero.')

    while True:
        try:
            nota = int(pedir_usuario('Ingrese la nota del alumno: '))
            if nota < 0:
                print('La nota no puede ser un número negativo.')
                continue
            break
        except ValueError:
            print('nota ingresada incorrecta. Ingrese un número entero.')


    alumnos.append({
                "nombre": nombre, 
                "edad": edad, 
                "carrera": carrera,
                "nota": nota
            })

    return alumnos


def mostrar_alumnos(alumnos):

    for alumno in alumnos:
        print(f"Datos del alumno {alumno['nombre']}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Carrera: {alumno['carrera']}")
        print(f"Nota: {alumno['nota']}")
        print("")

def mostrar_alumno(alumnos):
    posicion = buscar_alumno(alumnos)

    if posicion is not None:
        alumno = alumnos[posicion]
        print(f"\n--- Alumno Encontrado ---")
        print(f"Nombre: {alumno['nombre']} | Edad: {alumno['edad']} | Carrera: {alumno['carrera']} | Nota: {alumno['nota']}\n")
    else:
        print("Alumno no encontrado.\n")

def buscar_alumno(alumnos):

    nombre = pedir_usuario('Ingrese el nombre del alumno: ')

    for i in range(len(alumnos)):
        if alumnos[i]['nombre'].lower() == nombre.lower():
            return i
    return None



def actualizar_edad(alumnos):


    posicion = buscar_alumno(alumnos)

    if posicion is None:
        print("No se encontró al alumno para actualizar.")
        return False

    while True:
        try:
            edad = int(pedir_usuario('Ingrese la edad del alumno: '))
            if edad < 0:
                print('La edad no puede ser un número negativo.')
                continue
            break
        except ValueError:
            print('Edad ingresada incorrecta. Ingrese un número entero.')


    if posicion is not None :
        alumnos[posicion]['edad'] = edad
        return True
    
    return False


def eliminar_alumno(alumnos):

    posicion = buscar_alumno(alumnos)

    if posicion is not None :
        alumnos.pop(posicion)
        return True
    
    return False



def obtener_aprobados(alumnos):

    aprobado = []
    for alumno in alumnos:
        if alumno['nota'] >= 12.5:
            aprobado.append(alumno)

    return aprobado

def mostrar_aprobados(alumnos):

    lista_aprobados = obtener_aprobados(alumnos)
    
    print("=== ALUMNOS APROBADOS ===")
    
    if len(lista_aprobados) == 0:
        print("No hay ningún alumno aprobado.")
    else:
        for alumno in lista_aprobados:
            print(f"- {alumno['nombre']} (Nota: {alumno['nota']}, Carrera: {alumno['carrera']})")
            
    print()


def calcular_estadisticas(alumnos):

    if len(alumnos) == 0 :
        return 0, 0 , 0

    suma = 0
    mayor = alumnos[0]['edad']
    menor = alumnos[0]['edad']

    for alumno in alumnos:

        edad = alumno['edad']
        suma += edad

        if edad > mayor:
            mayor = edad

        if edad < menor:
            menor = edad

    promedio = suma/len(alumnos)

    return promedio, mayor,menor
         

def mostrar_estadisticas(alumnos):

    v_promedio , v_mayor , v_menor = calcular_estadisticas(alumnos)

    print("LAS ESTADISTICAS")
    print(f"El promedio total de las edades es: {v_promedio:.2f}")
    print(f"La edad mayor es: {v_mayor}")
    print(f"La edad menor es: {v_menor}")


def menu():
    print("===== SISTEMA DE ALUMNOS =====")
    print("1. Agregar alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno")
    print("4. Actualizar edad")
    print("5. Eliminar alumno")
    print("6. Mostrar aprobados")
    print("7. Mostrar estadísticas")
    print("8. Salir")


def main():

    alumnos = [
    {"nombre": "Carlos", "edad": 21, "carrera": "Software" , "nota": 14},
    {"nombre": "Maria", "edad": 22, "carrera": "Software" , "nota": 18},
    {"nombre": "Pedro", "edad": 20, "carrera": "Sistemas" , "nota": 12},
    {"nombre": "Ana", "edad": 24, "carrera": "Industrial" , "nota": 11}
    ]   


    while True:

        menu()

        try:
            choice = int(pedir_usuario('Seleccione una opción: '))
        except ValueError:
            print("Error: Por favor, ingrese un número del 1 al 5.\n")
            continue

        match choice:
            case 1:
                agregar_alumno(alumnos)
            case 2:
                mostrar_alumnos(alumnos)
            case 3:
                mostrar_alumno(alumnos)
            case 4:
                actualizar_edad(alumnos)
            case 5:
                eliminar_alumno(alumnos)
            case 6:
                mostrar_aprobados(alumnos)
            case 7:
                mostrar_estadisticas(alumnos)
            case 8:
                    print("Saliendo del programa... ¡Hasta luego!")
                    break
            case _:
                print("Error: Opción no válida. Intente con números del 1 al 8.\n")


main()





















































































































































# Clase 11 - Manejo de archivos en python

# En esta clase aprenderás a guardar y leer 
# información desde archivos, empezando por archivos .txt.




# Crear y escribir un archivo

# Python permite trabajar con archivos mediante open().

# La forma básica:

# archivo = open("datos.txt", "w")

# El segundo parámetro indica el modo.

# Los principales que aprenderemos son:

# | Modo  | Significado      |
# | ----- | ---------------- |
# | `"r"` | Read → leer      |
# | `"w"` | Write → escribir |
# | `"a"` | Append → agregar |


# 3. Escribir con "w"

# archivo = open("datos.txt", "w")

# archivo.write("Nicolas")

# archivo.close()

# 4. Agregar contenido con "a"

# Si queremos conservar lo existente y agregar información:

# archivo = open("datos.txt", "a")
# archivo.write("Python \n")
# archivo.close()

# "\n" significa salto de linea

# 6. Leer un archivo

# Ahora vamos a utilizar "r":


# archivo = open("datos.txt", "r")

# contenido = archivo.read()

# print(contenido)

# archivo.close()

# Hay distintas formas de leer el archivo
# Para leer una linea usamos readline()
# Para obtener todas las líneas en una lista usamos readlines():
# nombres_limpios = []

# for nombre in nombres:
#     nombres_limpios.append(nombre.strip())

# [
#     "Carlos\n",
#     "Maria\n",
#     "Pedro\n"
# ]



# La forma recomendada para abrir archivos es con with open
# Asi python se encarga de cerrar el archivo x si solo

# with open("datos.txt", "r") as archivo:
#     contenido = archivo.read()

# print(contenido)



# 9. Escribir utilizando with
# with open("datos.txt", "w") as archivo:
#     archivo.write("Carlos\n")
#     archivo.write("Maria\n")
#     archivo.write("Pedro\n")


# 10. Leer utilizando with
# with open("datos.txt", "r") as archivo:
#     contenido = archivo.read()

# print(contenido)


# 11. Guardar una lista

# nombres = ["Carlos", "Maria", "Pedro"]

# with open("datos.txt","w") as archivo:
#     for nombre in nombres:
#         archivo.write(nombre + "\n")

# 12. Leer el archivo y convertirlo nuevamente en una lista
# with open("datos.txt", "r") as archivo:
#     nombres = archivo.readlines()

# Podemos limpiarlo (\n) utilizando .strip():

# nombres_limpios = []

# for nombre in nombres:
#     nombres_limpios.append(nombre.strip())

# print(nombres_limpios)

# strip() elimina espacios y saltos 
# de línea innecesarios al principio y al final.

# 13. Manejo de errores

# try:
#     with open("datos.txt", "r") as archivo:
#         contenido = archivo.read()

#     print(contenido)

# except FileNotFoundError:
#     print("El archivo no existe.")

# 14. Crear una función para guardar
# def guardar_datos(datos):
#     with open("datos.txt", "w") as archivo:
#         archivo.write(datos)

# def main():
#     guardar_datos("Hola Python")

# main()

# 15. El siguiente nivel: guardar diccionarios
# estudiante = {
#     "nombre": "Carlos",
#     "edad": 20,
#     "carrera": "Software"
# }

# with open("estudiante.txt", "w") as archivo:
#     archivo.write(estudiante["nombre"] + "\n")
#     archivo.write(str(estudiante["edad"]) + "\n")
#     archivo.write(estudiante["carrera"] + "\n")



# Ejercicios clase 11

# Continuamos con la numeración.

# Ejercicio 71 — Crear y escribir

# Crea un archivo:

# datos.txt

# y escribe:

# Hola Python
# Estoy aprendiendo archivos
# Clase 11

# Utiliza:

# with open(...)


# def guardar_datos(datos):
#     try:
#         with open ("datos.txt", "w") as archivo:
#             archivo.write(datos + "\n")
#     except FileNotFoundError:
#         print("El archivo no existe.")

# def anadir_datos(datos):
#     try:
#         with open ("datos.txt", "a") as archivo:
#             archivo.write(datos + "\n")
#     except FileNotFoundError:
#         print("El archivo no existe.")


# def main():
#     guardar_datos("Hola Python")
#     anadir_datos("Estoy aprendiendo archivos")
#     anadir_datos("Clase 11")


# main()


# Ejercicio 72 — Escribir varios datos

# Crea una lista:

# nombres = ["Carlos", "Maria", "Pedro", "Ana"]

# Guarda todos los nombres en:

# nombres.txt

# Cada nombre debe estar en una línea diferente.


# def guardar_datos(datos):
#     with open("nombres.txt","w") as archivo:
#         for dato in datos:
#             archivo.write(dato + "\n")


# def main():
#     nombres = ["Carlos", "Maria", "Pedro", "Ana"]

#     guardar_datos(nombres)



# main()



# Ejercicio 73 — Leer archivo

# Utiliza el archivo nombres.txt del ejercicio anterior.

# Léelo utilizando:

# read()

# y muestra todo su contenido.


# def guardar_datos(datos):
#     try:
#         with open("nombres.txt","w") as archivo:
#             for dato in datos:
#                 archivo.write(dato + "\n")
#     except FileNotFoundError:
#         print("El archivo no existe.")

# def leer_y_mostrar_datos():
#     try:
#         with open("nombres.txt","r") as archivo:
#             # read() toma todo el contenido como un solo texto gigante
#             contenido = archivo.read()
#             print(contenido)
#     except FileNotFoundError:
#         print("El archivo no existe.")


# def main():
#     nombres = ["Carlos", "Maria", "Pedro", "Ana"]

#     guardar_datos(nombres)
#     leer_y_mostrar_datos()

# main()


# Ejercicio 74 — Leer línea por línea

# Utiliza:

# readlines()

# Obtén todas las líneas y recórrelas con:

# for

# Pero antes de mostrar cada nombre, utiliza:

# strip()

# para eliminar el salto de línea.

# Resultado esperado:

# Carlos
# Maria
# Pedro
# Ana


# def guardar_datos(datos):
#     try:
#         with open("nombres.txt","w") as archivo:
#             for dato in datos:
#                 archivo.write(dato + "\n")
#     except FileNotFoundError:
#         print("El archivo no existe.")

# def leer_y_mostrar_datos():
#     try:
#         with open("nombres.txt","r") as archivo:
#             contenido = archivo.readlines()
#             for elemento in contenido:
#                 print(elemento.strip())
#     except FileNotFoundError:
#         print("El archivo no existe.")


# def main():
#     nombres = ["Carlos", "Maria", "Pedro", "Ana"]

#     guardar_datos(nombres)
#     leer_y_mostrar_datos()

# main()


# Ejercicio 75 — Contar líneas

# Crea una función:

# contar_lineas(nombre_archivo)

# Debe abrir el archivo y retornar la cantidad de líneas.

# Por ejemplo:

# Carlos
# Maria
# Pedro
# Ana

# debe retornar:

# 4


# def guardar_datos(datos):
#     try:
#         with open("nombres.txt","w") as archivo:
#             for dato in datos:
#                 archivo.write(dato + "\n")
#     except FileNotFoundError:
#         print("El archivo no existe.")

# def leer_y_mostrar_datos():
#     try:
#         with open("nombres.txt", "r") as archivo:
#             contenido = archivo.readlines()
#             for elemento in contenido:
#                 print(elemento.strip())
#     except FileNotFoundError:
#         print("El archivo no existe.")


# def contar_lineas(nombre_archivo):
#     try:
#         with open(nombre_archivo,"r") as archivo:
#             contenido = archivo.readlines()
#             return len(contenido)
#     except FileNotFoundError:
#         print("El archivo no existe.")
#         return 0


    
# def main():
#     nombres = ["Carlos", "Maria", "Pedro", "Ana"]

#     guardar_datos(nombres)
#     print("--- Contenido del archivo ---")
#     leer_y_mostrar_datos()


#     print("--- Contando líneas ---")
#     # Guardamos el resultado de la función en una variable (pasando el nombre con comillas)
#     total = contar_lineas("nombres.txt")
#     print(f"El archivo tiene: {total} líneas.")

# main()



# Ejercicio 76 — Buscar en un archivo

# Crea:

# buscar_nombre(nombre_archivo, nombre)

# Debe buscar si un nombre existe dentro del archivo.

# Ejemplo:

# buscar_nombre("nombres.txt", "Carlos")

# Debe indicar:

# El nombre existe

# Si buscas:

# buscar_nombre("nombres.txt", "Luis")

# debe indicar:

# El nombre no existe

# Utiliza strip() y recuerda que puedes utilizar .lower() para que la búsqueda no dependa de mayúsculas.


# def guardar_datos(datos):
#     try:
#         with open("nombres.txt","w") as archivo:
#             for dato in datos:
#                 archivo.write(dato + "\n")
#     except FileNotFoundError:
#         print("El archivo no existe.")

# def leer_datos(nombre_archivo):
#     contenido = []
#     try:
#         with open(nombre_archivo, "r") as archivo:
#             contenido = archivo.readlines()
        
#     except FileNotFoundError:
#         print("El archivo no existe.")
#     return contenido

# def buscar_nombres(nombre_archivo, nombre):
#     v_contenido = leer_datos(nombre_archivo)
#     encontrado = False

#     for linea in v_contenido:
#         nombre_limpio = linea.strip().lower()
#         if nombre_limpio == nombre.lower():
#             encontrado = True
#             break # Si lo encontramos, salimos del bucle
                    
#     # Mostramos el resultado final
#     if encontrado:
#         print("El nombre existe")
#     else:
#         print("El nombre no existe")



# def contar_lineas(nombre_archivo):
#     try:
#         with open(nombre_archivo,"r") as archivo:
#             contenido = archivo.readlines()
#             return len(contenido)
#     except FileNotFoundError:
#         print("El archivo no existe.")
#         return 0


    
# def main():
#     nombres = ["Carlos", "Maria", "Pedro", "Ana"]

#     guardar_datos(nombres)
#     print("--- Buscar Nombre ---")
#     buscar_nombres("nombres.txt", "Carlos")


#     print("--- Contando líneas ---")
#     # Guardamos el resultado de la función en una variable (pasando el nombre con comillas)
#     total = contar_lineas("nombres.txt")
#     print(f"El archivo tiene: {total} líneas.")

# main()



# Ejercicio 77 — Agregar información

# Crea una función:

# agregar_nombre(nombre_archivo, nombre)

# Debe utilizar "a" para agregar un nuevo nombre sin borrar los anteriores.

# Por ejemplo:

# Carlos
# Maria
# Pedro

# Después de:

# agregar_nombre("nombres.txt", "Luis")

# debe quedar:

# Carlos
# Maria
# Pedro
# Luis


# def guardar_datos(datos):
#     try:
#         with open("nombres.txt","w") as archivo:
#             for dato in datos:
#                 archivo.write(dato + "\n")
#     except FileNotFoundError:
#         print("El archivo no existe.")


# def agregar_nombre(nombre_archivo, nombre):
#     try:
#         with open(nombre_archivo,"a") as archivo:
#             archivo.write(nombre + "\n")
#     except FileNotFoundError:
#         print("El archivo no existe.")


# def leer_datos(nombre_archivo):
#     contenido = []
#     try:
#         with open(nombre_archivo, "r") as archivo:
#             contenido = archivo.readlines()
        
#     except FileNotFoundError:
#         print("El archivo no existe.")
#     return contenido

# def buscar_nombres(nombre_archivo, nombre):
#     v_contenido = leer_datos(nombre_archivo)
#     encontrado = False

#     for linea in v_contenido:
#         nombre_limpio = linea.strip().lower()
#         if nombre_limpio == nombre.lower():
#             encontrado = True
#             break # Si lo encontramos, salimos del bucle
                    
#     # Mostramos el resultado final
#     if encontrado:
#         print("El nombre existe")
#     else:
#         print("El nombre no existe")



# def contar_lineas(nombre_archivo):
#     try:
#         with open(nombre_archivo,"r") as archivo:
#             contenido = archivo.readlines()
#             return len(contenido)
#     except FileNotFoundError:
#         print("El archivo no existe.")
#         return 0


    
# def main():
#     nombres = ["Carlos", "Maria", "Pedro", "Ana"]

#     guardar_datos(nombres)
#     print("--- Buscar Nombre ---")
#     buscar_nombres("nombres.txt", "Carlos")
#     agregar_nombre("nombres.txt", "Nicolas")



#     print("--- Contando líneas ---")
#     # Guardamos el resultado de la función en una variable (pasando el nombre con comillas)
#     total = contar_lineas("nombres.txt")
#     print(f"El archivo tiene: {total} líneas.")

# main()



# Ejercicio 78 — Copiar archivo

# Crea una función:

# copiar_archivo(origen, destino)

# Debe:

# Abrir el archivo origen.
# Leer su contenido.
# Crear/escribir el archivo destino.
# Copiar todo el contenido.

# Por ejemplo:

# copiar_archivo("nombres.txt", "backup.txt")


# def copiar_archivo(origen, destino):
#     try:
#         with open(origen, "r") as archivo_origen:
#             contenido = archivo_origen.read()

#         with open(destino, "w") as archivo_destino:
#             archivo_destino.write(contenido)


#         print(f"¡Archivo copiado con éxito de '{origen}' a '{destino}'!")

#     except FileNotFoundError:
#         print(f"Error: El archivo de origen '{origen}' no existe.")
    



# def main():
#     nombres = ["Carlos", "Maria", "Pedro", "Ana"]

#     copiar_archivo('nombres.txt', 'destino.txt')


# main()




# Ejercicio 79 — Registro de estudiantes

# Crea:

# estudiantes = [
#     {"nombre": "Carlos", "edad": 20},
#     {"nombre": "Maria", "edad": 22},
#     {"nombre": "Pedro", "edad": 21}
# ]

# Crea una función:

# guardar_estudiantes(estudiantes)

# Debe guardar la información en:

# estudiantes.txt

# Puedes decidir un formato sencillo, por ejemplo:

# Carlos | 20
# Maria | 22
# Pedro | 21

# Después crea:

# mostrar_archivo(nombre_archivo)

# que lea y muestre el contenido.



# def guardar_estudiantes(estudiantes):
#     try:
#         with open("estudiantes.txt", "w") as archivo_destino:
#             for estudiante in estudiantes:
#                 archivo_destino.write(f"{estudiante['nombre']} | {estudiante['edad']} \n")

#     except FileNotFoundError:
#         print(f"Error: El archivo no existe.")
    


# def mostrar_archivo(nombre_archivo):
#     try:
#         with open(nombre_archivo,"r") as archivo:
#             contenido = archivo.read()
#             print(contenido)
#     except FileNotFoundError:
#         print(f"Error: El archivo no existe.")

# def main():

#     estudiantes = [
#         {"nombre": "Carlos", "edad": 20},
#         {"nombre": "Maria", "edad": 22},
#         {"nombre": "Pedro", "edad": 21}
#     ]


#     guardar_estudiantes(estudiantes)
#     mostrar_archivo("estudiantes.txt")

# main()



# Ejercicio 80 — Mini sistema de notas

# Este será el ejercicio más importante de la clase.

# Crea un programa que permita:

# ===== SISTEMA DE NOTAS =====

# 1. Registrar estudiante
# 2. Mostrar estudiantes
# 3. Buscar estudiante
# 4. Agregar estudiante al archivo
# 5. Salir

# Cada estudiante tendrá:

# {
#     "nombre": "...",
#     "nota": 0
# }
# Requisitos

# 1. Registrar estudiante

# Solicita:

# Nombre:
# Nota:

# Y agrega el estudiante a una lista.

# 2. Mostrar estudiantes

# Muestra los estudiantes actualmente registrados.

# 3. Buscar estudiante

# Solicita un nombre y busca utilizando la lista.

# 4. Agregar estudiante al archivo

# Utiliza "a" para guardar el estudiante al final de:

# notas.txt

# Por ejemplo:

# Carlos | 15
# Maria | 18
# Pedro | 12

# 5. Salir

# Termina el programa.

# Estructura recomendada

# No quiero que hagas todo dentro de main().

# Utiliza algo parecido a:

# pedir_nombre()
# pedir_nota()
# registrar_estudiante()
# mostrar_estudiantes()
# buscar_estudiante()
# guardar_estudiante_archivo()
# mostrar_menu()
# main()

# No te preocupes todavía por convertir automáticamente el archivo nuevamente en diccionarios. Eso lo haremos cuando aprendamos JSON.

# def pedir_usuario(mensaje):
#     elemento = input(mensaje)
#     return elemento

# def pedir_nombre():
#     nombre = pedir_usuario('Ingrese el nombre del alumno: ')
#     return nombre


# def pedir_nota():

#     while True:
#         try:
#             nota = int(pedir_usuario('Ingrese la nota del alumno: '))
#             if nota < 0:
#                 print('La nota no puede ser un número negativo.')
#                 continue
#             if nota > 20:
#                 print('La nota debe de estar en un rango entre 0 - 20')
#                 continue
#             break
#         except ValueError:
#             print('Nota ingresada incorrecta. Ingrese un número entero.')
#     return nota

# def registrar_estudiante(lista):

#     v_nombre = pedir_nombre()
#     v_nota = pedir_nota()

#     lista.append({
#             "nombre": v_nombre,
#             "nota": v_nota,
#             })

#     return lista

# def mostrar_estudiantes(lista):
#     for elemento in lista:
#         print(f":::Datos del alumno {elemento['nombre']}:::")
#         print(f"Nombre: {elemento['nombre']}")
#         print(f"Nota: {elemento['nota']} \n")
        

        
# def buscar_estudiante(lista):

#     v_nombre = pedir_nombre()
#     estado =  False
#     if not lista:
#         print('No hay estudiante') 
    
#     for elemento in lista:
#         if v_nombre.lower() in elemento['nombre'].lower():
#             estado = True
#             break
    
#     if estado:
#         print('El usuario existe') 
#     else:
#         print('El usuario no existe') 



# def guardar_estudiante_archivo(lista):
#     if not lista:
#         print("No hay estudiantes nuevos para guardar.\n")
#         return
        
#     try:
#         with open("notas.txt", "a") as archivo:
#             for elemento in lista:
#                 archivo.write(f"{elemento['nombre']} | {elemento['nota']}\n")
        
#         print("¡Estudiantes guardados exitosamente en el archivo!")
#         lista.clear()  # Vaciamos la lista para que no se dupliquen la próxima vez
#         print("Lista temporal limpiada.\n")

#     except Exception as e:
#         print(f"Error al guardar: {e}")



# def mostrar_menu():
#     print("===== SISTEMA DE NOTAS =====")
#     print("1. Registrar estudiante")
#     print("2. Mostrar estudiantes")
#     print("3. Buscar estudiante")
#     print("4. Agregar estudiante al archivo")
#     print("5. Salir")


# def main():

#     estudiantes = [
#     {
#         "nombre": "Carlos",
#         "nota": 20,
#     },
#     {
#         "nombre": "Maria",
#         "nota": 10,
#     }
#     ]



#     while True:
#         mostrar_menu()
#         try:
#             choice = int(pedir_usuario('Seleccione una opción: '))
#         except ValueError:
#             print("Error: Por favor, ingrese un número del 1 al 6.\n")
#             continue

#         match choice:
#             case 1:
#                 registrar_estudiante(estudiantes)
#             case 2:
#                 mostrar_estudiantes(estudiantes)
#             case 3:
#                 buscar_estudiante(estudiantes)
#             case 4:
#                 guardar_estudiante_archivo(estudiantes)
#             case 5:
#                 print("Saliendo del programa...")
#                 break
            



# main()






# Opción 1: Guardar solo los nuevos (Vaciando la lista temporal)
# Si quieres seguir usando el modo "a" para añadir datos al final del archivo 
# poco a poco, lo correcto es que tras escribir la lista actual en el archivo, 
# vacíes la lista en memoria. De este modo, la próxima vez que registres a alguien, 
# la lista solo tendrá a los alumnos nuevos.Para lograrlo, limpia la lista al final 
# del bloque con lista.clear():pythondef guardar_estudiante_archivo(lista):

#     if not lista:
#         print("No hay estudiantes nuevos para guardar.\n")
#         return
        
#     try:
#         with open("notas.txt", "a") as archivo:
#             for elemento in lista:
#                 archivo.write(f"{elemento['nombre']} | {elemento['nota']}\n")
        
#         print("¡Estudiantes guardados exitosamente en el archivo!")
#         lista.clear()  # OJO: Vaciamos la lista para que no se dupliquen la próxima vez
#         print("Lista temporal limpiada.\n")

#     except Exception as e:
#         print(f"Error al guardar: {e}")

# Usa el código con precaución.Opción 2: Sobrescribir el archivo completo 
# (Cambiando a modo "w")Si prefieres que la lista en memoria (estudiantes) 
# se mantenga intacta durante toda la ejecución del programa para poder seguir 
# usándola en la opción 2 (mostrar_estudiantes), la solución es cambiar el modo de 
# apertura de "a" a "w". De esta forma, cada vez que des guardar, 
# se reescribirá el archivo completo con el estado actual exacto de tu lista.pythondef 
# guardar_estudiante_archivo(lista):

#     try:
#         Al usar "w", el archivo se limpia y se escribe la lista actualizada sin duplicar nada
#         with open("notas.txt", "w") as archivo:
#             for elemento in lista:
#                 archivo.write(f"{elemento['nombre']} | {elemento['nota']}\n")
#         print("¡Archivo actualizado con éxito!\n")

#     except Exception as e:
#         print(f"Error al guardar: {e}")
# Usa el código con precaución.🔍 Un par de correcciones extra para tu código:Aparte del problema del archivo, hay dos detalles en tus otras funciones que te conviene corregir para que el programa sea 100% robusto:En buscar_estudiante: Tu bucle busca bien, pero si el primer estudiante coincide (estado = True) y el segundo no, el bucle sigue corriendo. Te sugiero añadir un break apenas lo encuentre.En main: Inicializas estudiantes con Carlos y María adentro. Si usas la Opción 1, ten en cuenta que la primera vez que guardes se escribirán ellos dos y luego la lista quedará limpia para los nuevos que registres mediante consola.¿Cuál de las dos opciones prefieres implementar para la lógica de tu programa: vaciar la lista para guardar solo novedades o cambiar el modo a "w" para conservar siempre toda la lista en memoria?
























































































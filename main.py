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
    variable = input(mensaje)
    return variable


def agregar_alumno(alumnos):

    nombre = pedir_usuario('Ingrese el nombre del alumno:')
    carrera = pedir_usuario('Ingrese la carrera del alumno:')

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


    alumnos.append(
            {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera,
            "nota": nota
            }
        )
    return alumnos


def mostrar_alumnos(lista):
    for alumno in lista:
        print(f"Datos del alumno {alumno['nombre']}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Carrera: {alumno['carrera']}")
        print(f"Nota: {alumno['nota']}" )
        print(" ")

def mostrar_alumno_posicion(lista):
    posicion = buscar_alumno(lista)

    if posicion is not None:
        alumno = lista[posicion]
        print(f"\n--- Alumno Encontrado ---")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Carrera: {alumno['carrera']}")
        print(f"Nota: {alumno['nota']}" )
        print(" ")

    else:
        print("Alumno no encontrado.\n")


def buscar_alumno(alumnos):

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


# eliminar_alumno()
# obtener_aprobados()
# calcular_estadisticas()


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


# ===== SISTEMA DE ALUMNOS =====

# 1. Agregar alumno
# 2. Mostrar alumnos
# 3. Buscar alumno
# 4. Actualizar edad
# 5. Eliminar alumno
# 6. Mostrar aprobados
# 7. Mostrar estadísticas
# 8. Salir


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
            print("Error: Por favor, ingrese un número del 1 al 6.\n")
            continue

        match choice:
            case 1:
                agregar_alumno(alumnos)
            case 2:
                mostrar_alumnos(alumnos)
            case 3:
                mostrar_alumno_posicion(alumnos)
            case 4:
                break
            case 5:
                break
            case 6:
                break
            case 7:
                break
            case 8: 
                print("Saliendo del programa...")
                break

main()










































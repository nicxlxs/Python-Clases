#Ejercicio 1

# def moestrar_mensaje():
#     print('Bienvenido al programa')


# moestrar_mensaje()
# moestrar_mensaje()
# moestrar_mensaje()



#Ejercicio 2

# def saludar(nombre):
#     print(f'Hola {nombre}')


# saludar("Omar")
# saludar("Nicolas")
# saludar("Juan")


#Ejercicio 3

# def sumar(num1,num2):
#     return num1 + num2

# resultado = sumar(10, 5)

# print(resultado)


#Ejercicio 4

# def es_par(numero):

#     if numero % 2 == 0:
#         return True
#     else:
#         return False


# while True:
#     try:
#         numero = int(input('Ingresa un numero: '))
#         break
#     except ValueError:
#         print("Numero ingresado no valido")

# print(es_par(numero))



#Ejercicio 5

# def calcular_promedio(num1,num2,num3):
#     return (num1 + num2 + num3) / 3


# print(calcular_promedio(12,12,13))




# def pedir_numero(mensaje):
#     while True:
#         try:
#             return int(input(mensaje))
#         except ValueError:
#             print("Número inválido")


# def sumar(num1, num2):
#     return num1 + num2


# def main():
#     num1 = pedir_numero("Ingresa el primer número: ")
#     num2 = pedir_numero("Ingresa el segundo número: ")

#     resultado = sumar(num1, num2)

#     print(f"El resultado es: {resultado}")


# main()


#Ejercicios parte 2

#Ejercicio 6

# def pedir_numero(mensaje):
#     while True:
#         try:
#             return int(input(mensaje))
#         except ValueError:
#             print("Número inválido")


# def main():
#     num1 = pedir_numero('Ingresa el primer numero: ')
#     num2 = pedir_numero('Ingresa el segundo numero: ')
#     num3 = pedir_numero('Ingresa el tercer numero: ')

# main()


# def pedir_numero(mensaje):
#     while True:
#         try:
#             return int(input(mensaje))
#         except ValueError:
#             print('Numero invalido')


# def obtener_mayor(numero1,numero2):
#    if numero1 > numero2:
#        return numero1
#    else:
#        return numero2


# def mostrar_resultado(resultado):
#     print(f'El numero mayor es {resultado}')



# def main():
#     num1 = pedir_numero('Ingrese el valor del primer numero: ')
#     num2 = pedir_numero('Ingrese el valor del segundo numero: ')

#     resultado = obtener_mayor(num1,num2)

#     mostrar_resultado(resultado)


# main()



#Ejercicio 8 - Calculadora organizada

# Crea una calculadora con estas funciones:
# pedir_numero()
# sumar()
# restar()
# multiplicar()
# dividir()
# mostrar_menu()
# main()

# def pedir_numero(mensaje):
#     while True:
#         try:
#             return int(input(mensaje))
#         except ValueError:
#             print('Numero no valido')

# def suma(num1,num2):
#     return num1 + num2

# def resta(num1,num2):
#     return num1 - num2

# def multiplicacion(num1,num2):
#     return num1 * num2

# def division(num1,num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         return "Error: No se puede dividir entre cero."
#     except ValueError:
#         return "Error: Entrada no válida. Por favor, ingresa números válidos."


# def mostrar_menu():
#     print("\n:::::: CALCULADORA ::::::")
#     print("1. Sumar")
#     print("2. Restar") 
#     print("3. Multiplicar") 
#     print("4. Dividir")
#     print("5. Salir")
#     try:
#         return int(input("Elige una opción: "))
#     except ValueError:
#         return -1  # Retornamos un número inválido si no introducen un entero
    
    


# def main():
#         while True:
#             choice = mostrar_menu()

#             if choice == 5:
#                 print("Saliendo de la calculadora... ¡Hasta luego!")
#                 break
                
#             if choice in [1, 2, 3, 4]:
#                 num1 = pedir_numero('Ingresa el primer número: ')
#                 num2 = pedir_numero('Ingresa el segundo número: ')
                
#                 match choice:
#                     case 1:
#                         print(f"El resultado de la suma es: {suma(num1, num2)}")
#                     case 2:
#                         print(f"El resultado de la resta es: {resta(num1, num2)}")
#                     case 3:
#                         print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
#                     case 4:
#                         print(f"El resultado de la división es: {division(num1, num2)}")
#             else:
#                 print("Error: Opción no válida. Por favor, ingresa un número del 1 al 5.")

# # Punto de entrada del programa
# if __name__ == "__main__":
#     main()
            

#Ejercicio 9 - Sistema de notas

# def pedir_nota(mensaje):
#     while True:
#         try:
#             return float(input(mensaje))

#         except ValueError:
#             print('Numero invalido')
            

# def calcular_promedio(nota1,nota2,nota3):
#     return (nota1 + nota2 + nota3) / 3



# def determinar_estado(promedio):
#     if promedio >= 12.5:
#         return 'Usted ha aprobado'
#     else: 
#         return 'Usted ha desaprobado'


# def mostrar_resultado(nota1,nota2,nota3, promedio,estado):

#     print('::::Notas::::')
#     print(f'Nota 1: {nota1}')
#     print(f'Nota 2: {nota2}')
#     print(f'Nota 3: {nota3}')
#     print(f'Promedio: {promedio}')
#     print(f'Estado: {estado}')


# def main():

#     nota1 = pedir_nota("Ingrese la nota 1: ")
#     nota2 = pedir_nota("Ingrese la nota 2: ")
#     nota3 = pedir_nota("Ingrese la nota 3: ")

#     promedio = calcular_promedio(nota1,nota2,nota3)
#     estado = determinar_estado(promedio)

#     mostrar_resultado(nota1,nota2,nota3,promedio,estado)



# # Ejecución del programa (sin espacios al inicio)
# if __name__ == "__main__":
#     main()



#Ejercicio 10 - Adivinar el numero

# Crea un programa con:
# generar_numero()
# pedir_intento()
# verificar_numero()
# main()

# Puedes importar:
# import random

# Y generar un número así:
# random.randint(1, 10)

# import random

# def generar_numero():
#     return random.randint(1,10)


# def pedir_intento(mensaje):
#     while True:
#         try:
#             intento = int(input(mensaje))
#             if 1 <= intento <= 10:
#                 return intento
#             else:
#                 print('Por favor, ingresa un número entre 1 y 10.')
#         except ValueError:
#             print('Intento no válido. Debe ser un número entero.')

# def verificar_numero(intento, numero_secreto):
#     if intento == numero_secreto:
#         print('¡Felicidades! Adivinaste el número secreto.')
#         return True  # Retornamos True para avisar que ya ganó
#     elif intento < numero_secreto:
#         print('El número secreto es MAYOR. ¡Sigue intentando!')
#         return False
#     else:
#         print('El número secreto es MENOR. ¡Sigue intentando!')
#         return False


# def main():
#     print("::::::::: JUEGO: ADIVINA EL NÚMERO :::::::::")
#     print("He pensado un número entre 1 y 10. ¿Puedes adivinarlo?")
    
#     numero_secreto = generar_numero()
#     # print(f"(Chito/Prueba: {numero_secreto})") # Puedes borrar el comentario para probar
    
#     # Bucle para permitir intentos infinitos hasta acertar
#     while True:
#         intento = pedir_intento('\nIngrese su número: ')
        
#         # Guardamos el resultado de la verificación
#         ha_ganado = verificar_numero(intento, numero_secreto)
        
#         if ha_ganado:
#             break  # Detiene el juego si adivinó

# if __name__ == "__main__":
#     main()


# Ejericio 11 - Parametros por defecto

# def calcular_precio(precio, descuento=0):
#     descontado = (precio * descuento) / 100
#     nuevo_precio = precio - descontado
#     return nuevo_precio



# # Impresión con formato de moneda y 2 decimales
# precio_final_1 = calcular_precio(100)
# precio_final_2 = calcular_precio(100, 20)

# print(f"Precio sin descuento: ${precio_final_1:.2f}") # Salida: $100.00
# print(f"Precio con descuento: ${precio_final_2:.2f}") # Salida: $80.00



#Ejercicio 12 - Argumentos por nombre 
# def mostrar_persona(*, nombre, edad, ciudad):
#     print(':::Datos:::')
#     print(f'nombre: {nombre}')
#     print(f'edad: {edad}')
#     print(f'ciudad: {ciudad}')




# mostrar_persona(nombre = 'Omar', edad = 22, ciudad = 'Lima')




#Ejercicio 13 - Multiples retornos

# def operaciones(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     try:
#         division = a / b
#     except ZeroDivisionError:
#         # Asignamos un mensaje de error a la variable para que la función pueda retornar con éxito
#         division = "Error: No se puede dividir entre 0"

#     return suma,resta,multiplicacion,division



# # Guardamos los cuatro resultados en cuatro variables diferentes
# res_suma, res_resta, res_mult, res_div = operaciones(12, 3) # Probamos con 0 para comprobar la seguridad

# # Mostramos los resultados de forma ordenada
# print(":::: RESULTADOS ::::")
# print(f"Suma:           {res_suma}")
# print(f"Resta:          {res_resta}")
# print(f"Multiplicación: {res_mult}")
# print(f"División:       {res_div}")


#Ejercicio 14 - Funciones booleanas

# def es_par(numero):
#     return numero % 2 == 0



# def es_positivo(numero):
#     return numero > 0
    

# def es_mayor_de_edad(edad):
#     return edad >= 18



# print(es_par(2))
# print(es_positivo(2))
# print(es_mayor_de_edad(19))



#Ejercicio 15 — Mini sistema


# def pedir_numero(mensaje):
#     while True:
#         try:
#             return int(input(mensaje))
        
#         except ValueError:
#             print('Numero ingresado invalido')
            



# def es_par(numero):
#     return numero % 2 == 0

# def es_positivo(numero):
#     return numero > 0

# def obtener_mayor(num1, num2):
#     # Comparamos los dos números recibidos y retornamos el más grande
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# def main():
#     print("::::::::: MINI SISTEMA DE ANÁLISIS :::::::::\n")
    
#     # 1. Pedir dos números
#     num1 = pedir_numero('Ingresa el primer número: ')
#     num2 = pedir_numero('Ingresa el segundo número: ')
    
#     # 2. Mostrar cuál es el mayor
#     mayor = obtener_mayor(num1, num2)
#     if num1 == num2:
#         print(f'\n Ambos números son iguales ({num1}).')
#     else:
#         print(f'\n El número mayor es: {mayor}')
    
#     # 3. Analizar el primer número
#     print(f'\nAnálisis del número {num1}:')
#     if es_positivo(num1):
#         print('  - Es positivo')
#     else:
#         print('  - Es negativo')
        
#     if es_par(num1):
#         print('  - Es par')
#     else:
#         print('  - Es impar')

#     # 4. Analizar el segundo número
#     print(f'\nAnálisis del número {num2}:')
#     if es_positivo(num2):
#         print('  - Es positivo')
#     else:
#         print('  - Es negativo')
        
#     if es_par(num2):
#         print('  - Es par')
#     else:
#         print('  - Es impar')

# if __name__ == "__main__":
#     main()














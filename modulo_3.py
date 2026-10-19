#Nivel 1


#1.- Imprimir los numeros del 1 al 10

# for i in range(1,11):
#     print(i)


#2.- Imprimir los numeros del 10 al 1

# for i in range(10,0,-1):
#     print(i)



#3.- Imprimir los números pares del 1 al 20.

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)




#4.- Imprimir los números impares del 1 al 20.
# for i in range(1,21):
#     if i % 2 != 0:
#         print(i)




#5.- Imprimir la tabla de multiplicar de un
# número introducido por el usuario.
# while True:

#     try:
#         num = int(input('Ingrese un numero:'))
#         break

#     except ValueError:
#         print("Error: Entrada no válida. Por favor, ingresa un número válido.")



# for i in range (1,13):
#     resultado = i * num
#     print(f'{i} x {num} = {resultado}')





#Nivel 2


#6.- Sumar los numeros del 1 al 100

# suma = 0

# for i in range(1,101):
#     suma += i

# print(suma)




#7.- Calcular el factorial de un numero

# while True:

#     try :

#         num = int(input('Ingrese un numero:'))
#         break

#     except ValueError:
#         print("Error: Entrada no válida. Por favor, ingresa un número válido.")

#Acumulador
# factorial = 1

# for i in range(num,0,-1):
#     factorial *= i

# print(f'{num}! = {factorial}')



#8.- Contar cuántos números pares existen entre 1 y 100.

# contador = 0

# for  i in range (1,101):
#     if i % 2 == 0:
#         contador += 1

# print(f'Hay un total de {contador} numero pares existentes entre 1 y 100')


#9.- Pedir numeros al usuario hasta que
# introduzca 0 y mostrar la suma.

# suma = 0


# while True:

#     try:
#         num = int(input('Ingrese un número (0 para salir): '))

#         if num == 0:
#             break

#         suma += num

#     except ValueError:
#         print("Error: Entrada no válida. Por favor, ingresa un número válido.")

# print(f'La suma total de los números ingresados es: {suma}')


#10.- Pedir una contraseña hasta que sea correcta.

# USER_PASSWORD = '1234'


# while True:

#     password = input('Ingresa su constrasena:')

#     if password == USER_PASSWORD:
#         print('Acceso concedido')
#         break
#     else:
#         print('Contrasena incorrecta, vuelva a intentar')



# Nivel 3


#11.- Crear un programa que pida 10 números
# y determine cuál es el mayor.


# mayor = None
# i = 1
# while(i <=10):
#     try:
#         num = int(input(f'Ingrese el valor para el numero {i}: '))

#         if mayor is None or num > mayor:
#             mayor = num

#         i += 1

#     except ValueError:
#         print("Error: Entrada no válida. Por favor, ingresa un número válido.")

# print(f'El numero mayor de los 10 numeros que ingreso es {mayor}')


#12.- Crear un programa que pida números hasta que el usuario 
# introduzca 0 y muestre:
# cantidad de números introducidos
# suma
# promedio
# mayor
# menor


# cantidad = 0
# suma = 0
# promedio = 0
# mayor = None
# menor = None

# while True:

#     try:
#         num = int(input('Ingresa un numero:'))

#         if num == 0 :
#             break

#         #Calculamos la cantidad de numeros
#         cantidad += 1
#         #Calculamos la suma de los numeros
#         suma += num
        

#         if mayor is None or num > mayor:
#             mayor = num


#         if menor is None or num < menor:
#             menor = num
        



#     except ValueError:
#         print("Error: Entrada no válida. Por favor, ingresa un número válido.")


# if cantidad > 0:
#     promedio = suma / cantidad
#     print(f'Cantidad de numeros introducidos: {cantidad}')
#     print(f'La suma de todos los numeros es: {suma}')
#     print(f'El promedio de todos los numeros es: {promedio}')
#     print(f'El numero mayor es: {mayor}')
#     print(f'El numero menor es: {menor}')


#13.- Crear un programa que determine si un numero es primo
# while True:
#     try:
#         num = int(input('Ingrese un número para verificar si es primo: '))
#         break  # Si la conversión fue exitosa, salimos del bucle de captura
#     except ValueError:
#         print('Error: Por favor, ingrese un número entero válido.')

# # A partir de aquí, 'num' está garantizado que existe y es un entero
# if num <= 1:
#     es_primo = False
# else:
#     es_primo = True
#     # Probamos a dividir desde el 2 hasta la raíz cuadrada de num (muy eficiente)
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             es_primo = False  # Encontró otro divisor, ya no es primo
#             break  # Rompemos el ciclo porque no hace falta seguir buscando

# # Resultado final
# if es_primo:
#     print(f'El número {num} es primo.')
# else:
#     print(f'El número {num} no es primo.')



#14.-Crear un patrón con bucles:
# *
# **
# ***
# ****
# *****


# for i in range (1,6):
#     for j in range(i):
#         print('*', end="")
#     print()


#15.- Crear una tabla de multiplicar del 1 al 10 utilizando bucles anidados.

# for i in range(1,11):
#     for j in range(1,11):
#         resultado = i * j
#         print(f'{i} x {j} = {resultado}')










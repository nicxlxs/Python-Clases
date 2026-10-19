
# Nivel 1
# Pedir un número e indicar si es positivo o negativo.
# Pedir un número e indicar si es par o impar.
# Pedir la edad e indicar si es mayor de edad.
# Pedir dos números y mostrar el mayor.


# def es_positivo_o_negativo(num):
#     if num > 0:
#         return "El numero es positivo."
#     elif num == 0:
#         return "El numero es cero."
#     else: 
#         return "El numero es negativo."


# def es_par_o_impar(num):
#     if num % 2 == 0:
#         return "El numero es par."
#     else:
#         return "El numero es impar."


# def es_mayor_de_edad(edad):
#     if edad >= 18:
#         return "Eres mayor de edad."
#     else:
#         return "Eres menor de edad."

# def mayor_de_dos_numeros(num1,num2):
#     if num1 > num2:
#         return f"El numero mayor es: {num1}"
#     elif num2 > num1:
#         return f"El numero mayor es: {num2}"
#     else:
#         return "Ambos numeros son iguales."

# try:
#     num = float(input("Ingresa un numero:"))

#     edad = int(input("Ingresa tu edad:"))

#     num1 = float(input("Ingresa el primer numero:"))
#     num2 = float(input("Ingresa el segundo numero:"))

# except ValueError:
#     print("Error: Entrada no válida. Por favor, ingresa un número válido.")
#     exit()


# print(es_positivo_o_negativo(num))
# print(es_par_o_impar(num))
# print(es_mayor_de_edad(edad))
# print(mayor_de_dos_numeros(num1,num2))



# Nivel 2
# Pedir tres números y mostrar el mayor.
# Pedir una nota (0–20) y mostrar:
# Excelente (18–20)
# Aprobado (14–17)
# Desaprobado (0–13)
# Pedir una contraseña y verificar si es "python123".
# Pedir un usuario y una contraseña. Solo permitir el acceso si:
# Usuario: "admin"
# Contraseña: "1234"

#Credenciales en environments
# USUARIO = "admin"
# CONTRASENA = "1234"
# CONTRASENA2 = "python123"

# def mayor_de_tres_numeros(num1,num2,num3):

#     if num1 > num2 and num1 > num3:
#         return f"El numero mayor es: {num1}"
#     elif num2 > num1 and num2 > num3:
#         return f"El numero mayor es: {num2}"
#     else:
#         return f"El numero mayor es: {num3}"

# def verificar_nota(nota):
#     if nota >= 18 and nota <=20:
#         return "Excelente"
#     elif nota >=14 and nota <=17:
#         return "Aprobado"
#     elif nota >=0 and nota <=13:
#         return "Desaprobado"

# def verificar_contrasena(contrasena):
#     if contrasena == CONTRASENA2:
#         return "Contraseña correcta."
#     else:
#         return "Contraseña incorrecta."

# def verificar_credenciales(usuario, contrasena):
#     if usuario == USUARIO  and contrasena == CONTRASENA:
#         return "Acceso concedido."
#     else:
#         return "Acceso denegado. Usuario o contraseña incorrectos."

# try:
#     num1 = float(input("Ingresa el primer numero:"))
#     num2 = float(input("Ingresa el segundo numero:"))
#     num3 = float(input("Ingresa el tercer numero:"))
#     nota = float(input("Ingresa una nota (0-20):"))
# except ValueError:
#     print("Error: Entrada no válida. Por favor, ingresa un número válido.")
#     exit()

# usuario = input("Ingresa tu usuario:")
# contrasena = input("Ingresa tu contraseña:")
# contrasena2 = input("Ingresa una contraseña para verificar en el sistema:")


# print(mayor_de_tres_numeros(num1,num2,num3))
# print("Resultado de la verificación de nota:", verificar_nota(nota))
# print("Resultado de la verificación de credenciales:", verificar_credenciales(usuario, contrasena))
# print("Resultado de la verificación de contraseña:", verificar_contrasena(contrasena2))




# Nivel 3
# Calcular el descuento:
# Compra mayor o igual a S/500 → 20%
# Compra mayor o igual a S/200 → 10%
# Caso contrario → 0%
# Pedir un año y determinar si es bisiesto.

# Pista: un año es bisiesto si es divisible entre 4, 
# excepto los divisibles entre 100, salvo que también sean divisibles entre 400.


# def calcular_descuento(compra):
#     if compra >= 500:
#         descuento = compra * 0.20
#         precio_final = compra - descuento
#         return f"Descuento aplicado: S/{descuento:.2f}. Precio final: S/{precio_final:.2f}."
#     elif compra >= 200:
#         descuento = compra * 0.10
#         precio_final = compra - descuento
#         return f"Descuento aplicado: S/{descuento:.2f}. Precio final: S/{precio_final:.2f}."
#     else:
#         return "No se aplica descuento. Precio final: S/{:.2f}.".format(compra)

# def es_bisiesto(anio):
#     if (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0):
#         return "Es ano bisiesto."
#     else:
#         return "No es ano bisiesto."
    

# try:
#     compra = float(input("Ingresa el monto de la compra:"))
#     anio = int(input("Ingresa un año:"))

# except ValueError:
#     print("Error: Entrada no válida. Por favor, ingresa un número válido.")
#     exit()

# print(calcular_descuento(compra))
# print(es_bisiesto(anio))


# Nivel 4 (reto)
# Crea un sistema de inicio de sesión con máximo tres intentos.

# Por ahora no uses bucles. Hazlo con condicionales anidados.

# Reglas:

# Usuario correcto: "omar"
# Contraseña correcta: "java123"
# Si falla, vuelve a pedir usuario y contraseña.

# Si falla tres veces, muestra:

# Cuenta bloqueada.

# Si acierta antes del tercer intento, muestra:

# Bienvenido al sistema.


#Credenciales en environments
# USUARIO = "omar"
# CONTRASENA = "java123"


# def verificar_credenciales(usuario, contrasena):
#     # Devuelve True si es correcto, False si es incorrecto
#     return usuario == USUARIO and contrasena == CONTRASENA

# print("--- INTENTO 1 ---")
# usuario = input("Ingresa tu usuario: ")
# contrasena = input("Ingresa tu contraseña: ")

# if verificar_credenciales(usuario, contrasena):
#     print("Bienvenido al sistema.")
# else:
#     print("Usuario o contraseña incorrectos.")
    
#     print("\n--- INTENTO 2 ---")
#     usuario = input("Ingresa tu usuario: ")
#     contrasena = input("Ingresa tu contraseña: ")
    
#     if verificar_credenciales(usuario, contrasena):
#         print("Bienvenido al sistema.")
#     else:
#         print("Usuario o contraseña incorrectos.")
        
#         print("\n--- INTENTO 3 ---")
#         usuario = input("Ingresa tu usuario: ")
#         contrasena = input("Ingresa tu contraseña: ")
        
#         if verificar_credenciales(usuario, contrasena):
#             print("Bienvenido al sistema.")
#         else:
#             print("\n Cuenta bloqueada.")
















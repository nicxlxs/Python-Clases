
# Ejercicio 2  y 3: área de un rectángulo y perímetro de un rectángulo
# Solicita la base y la altura.

# def area_rectangulo(base,altura):
#     try:
#         return base * altura

#     except ValueError:
#         return "Error: Entrada no válida. Por favor, ingresa números vdwdwálidos."


# def perimetro_rectangulo(base,altura):
#     try:
#         return 2 * (base + altura)

#     except ValueError:
#         return "Error: Entrada no válida. Por favor, ingresa números válidos."

# try:
#     base = float(input("Ingresa la base del rectangulo:"))
#     altura = float(input("Ingresa la altura del rectangulo:"))

# except ValueError: 
#     print("Error: Entrada no válida. Por favor, ingresa un número válido.")
#     exit()    

# print("El area del rectangulo es:", area_rectangulo(base,altura))
# print("El perimetro del rectangulo es:", perimetro_rectangulo(base,altura))



#Ejercicio 4: edad futura
# Solicita la edad actual y calcula cuántos años tendrá la persona dentro de 5 años.

# Ejemplo:

# Edad actual: 22
# Dentro de 5 años tendrás 27 años.

# def edad_futura(edad_actual):
#     try:
#         return edad_actual + 5

#     except ValueError:
#         return "Error: Entrada no válida. Por favor, ingresa un número válido."    


# edad_actual = int(input("Ingresa tu edad actual:"))
# print("Dentro de 5 años tendrás:", edad_futura(edad_actual), "años.")


# Ejercicio 5: promedio de cuatro notas

# Solicita cuatro notas y muestra el promedio con dos decimales.
    


# def promedio_notas(nota1,nota2,nota3,nota4):
#     try:
#         promedio = (nota1 + nota2 + nota3 + nota4) / 4
#         return round(promedio,2)

#     except ValueError:
#         return "Error: Entrada no válida. Por favor, ingresa números válidos."

# try:
#     nota1 = float(input("Ingresa la primera nota:"))
#     nota2 = float(input("Ingresa la segunda nota:"))
#     nota3 = float(input("Ingresa la tercera nota:"))
#     nota4 = float(input("Ingresa la cuarta nota:"))
    
# except ValueError:
#     print("Error: Entrada no válida. Por favor, ingresa un número válido.")
#     exit()    

# print("El promedio de las notas es:" , promedio_notas(nota1,nota2,nota3,nota4))






# Ejercicio 6: conversor de dólares a soles
# Utiliza una constante:
# TIPO_CAMBIO = 3.75
# Solicita una cantidad en dólares y conviértela a soles.
# Fórmula:
# soles = dólares × tipo de cambio


# TIPO_CAMBIO = 3.75

# def convertir_dolares_a_soles(dolares):
#     try:
#         soles = dolares * TIPO_CAMBIO
#         return round(soles,2) 

#     except ValueError:
#         return "Error: Entrada no válida. Por favor, ingresa un número válido."


# dolares = float(input("Ingresa la cantidad en dólares:"))
# print("La cantidad en soles es:", convertir_dolares_a_soles(dolares))




# Ejercicio 7: salario semanal

# Solicita:

# Horas trabajadas
# Pago por hora

# Calcula:

# salario = horas trabajadas × pago por hora

# def calcular_salario_semanal(horas_trabajadas, pago_por_hora):
#     try:
#         salario = horas_trabajadas * pago_por_hora
#         return round(salario,2)
#     except ValueError:
#         return "Error: Entrada no válida. Por favor, ingresa un número válido."



# horas_trabajadas = float(input("Ingresa las horas trabajadas:"))
# pago_por_hora = float(input("Ingresa el pago por hora:"))

# print("El salario semanal es:", calcular_salario_semanal(horas_trabajadas, pago_por_hora))




# Ejercicio 8: precio con descuento

# Solicita el precio y el porcentaje de descuento. Muestra:

# Precio original
# Cantidad descontada
# Precio final


# def calcular_precio_con_descuento(precio, porcentaje_descuento):

#     try:
#         cantidad_descontada = precio * (porcentaje_descuento / 100)
#         precio_final = precio - cantidad_descontada
#         return round(precio_final,2)
#     except ValueError:
#         return "Error: Entrada no válida. Por favor, ingresa un número válido."


# precio = float(input("Ingresa el precio original:"))
# porcentaje_descuento = float(input("Ingresa el porcentaje de descuento:"))

# print("El precio original es:", calcular_precio_con_descuento(precio, porcentaje_descuento))




# Reto de la clase

# Crea un programa que calcule el costo de una compra.

# El programa debe solicitar:

# Nombre del producto
# Precio unitario
# Cantidad comprada
# Porcentaje de descuento

# Debe mostrar:

# Producto
# Subtotal
# Descuento
# Total a pagar

# Utiliza estas fórmulas:

# subtotal = precio unitario × cantidad
# descuento = subtotal × porcentaje / 100
# total = subtotal - descuento




producto = input("Nombre del producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = float(input("Descuento: "))

subtotal = precio_unitario * cantidad

descuento = subtotal * (porcentaje_descuento / 100)

total = subtotal - descuento

print(f"Producto: {producto}")
print(f"Subtotal: S/ {subtotal:.2f}")
print(f"Descuento: S/ {descuento:.2f}")
print(f"Total: S/ {total:.2f}")

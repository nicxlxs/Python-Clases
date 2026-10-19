def suma(n,n2):
    return n + n2

def resta(n,n2):
    return n - n2

def multiplicacion(n,n2):
    return n * n2

def division(n,n2):
    try:
        return n / n2
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except ValueError:
        return "Error: Entrada no válida. Por favor, ingresa números válidos."


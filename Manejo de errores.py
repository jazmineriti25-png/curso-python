class EdadInvalidaError(Exception):
    """Excepción lanzada cuando la edad es menor a 0."""
    pass

def verificar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser negativa.")
    return f"Edad registrada: {edad}"

try:
    numero = int(input("Ingresa un entero positivo: "))
    print(verificar_edad(numero))
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
except EdadInvalidaError as e:
    print(f"Error de validación: {e}")
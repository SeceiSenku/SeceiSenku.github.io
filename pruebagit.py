def es_par_o_impar(numero):
    """
    Función que determina si un número es par o impar.

    Args:
    numero (int): El número a verificar.

    Returns:
    str: "par" si el número es par, "impar" si es impar.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Ejemplo de uso
if __name__ == "__main__":
    try:
        num = int(input("Ingresa un número: "))
        resultado = es_par_o_impar(num)
        print(f"El número {num} es {resultado}.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

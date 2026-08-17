def dividir(dividendo, divisor):
    try:
        # Intentamos hacer la división normal
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        # Si el divisor es 0, Python lanza ZeroDivisionError y lo capturamos acá
        print("¡Error detectado! No se puede dividir por cero.")
        return None

# --- Pruebas de la función ---

# Prueba 1: Una división que sí funciona
print("Probando dividir(27, 3):")
print(f"Resultado: {dividir(27, 3)}")
print("-" * 30)

# Prueba 2: La prueba de fuego con el cero
print("Probando dividir(27, 0):")
print(f"Resultado: {dividir(27, 0)}")
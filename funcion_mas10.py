def mas_10(valor):
    try:
        # Intentamos sumarle 10 al valor que nos pasen
        resultado = valor + 10
        print(f"¡Éxito! {valor} + 10 es igual a: {resultado}")
    except TypeError:
        # Si nos pasan un texto como "cinco", saltará este error y lo capturamos
        print(f"Error: No puedo sumar un número con el texto '{valor}'. ¡Debes pasar un número!")

# --- Pruebas de la función ---

# Prueba 1: Pasando un número real (Funciona perfecto)
print("Probando mas_10(5):")
mas_10(5)
print("-" * 30)

# Prueba 2: Pasando el texto "cinco" (Dispara el TypeError)
print("Probando mas_10('cinco'):")
mas_10("cinco")
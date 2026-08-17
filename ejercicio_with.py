# ==========================================
# EJERCICIO 8.1: Abrir, crear si no existe y añadir la frase
# ==========================================
# Al usar "with open(...) as fichero:", Python sabe que adentro de este bloque
# el archivo está abierto, y apenas salgamos de la sangría (indentación), lo cierra solo.

with open("aprendizaje_with.txt", "a+") as fichero:
    fichero.write("Estoy aprendiendo Python con la estructura WITH\n")
    print("--- Ejercicio 8.1: Frase guardada con éxito ---")

# Acá afuera del bloque, el archivo ya se cerró automáticamente.


# ==========================================
# EJERCICIO 8.2: Abrir y mostrar sus propiedades (metadatos)
# ==========================================
print("\n--- Ejercicio 8.2: Propiedades del fichero ---")

with open("aprendizaje_with.txt", "r") as fichero:
    print(f"Nombre del archivo: {fichero.name}")
    print(f"Modo de apertura:   {fichero.mode}")
    print(f"Codificación:       {fichero.encoding}")
    print(f"¿El archivo está cerrado adentro del bloque?: {fichero.closed}")

# Salimos del bloque... ¡Python ya lo cerró!
print("-" * 46)
print(f"¿El archivo está cerrado afuera del bloque?: {fichero.closed}")
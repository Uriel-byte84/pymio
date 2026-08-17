# ==========================================
# PASO 1: Crear y escribir en el archivo ('w')
# ==========================================
archivo = open("mi_agenda.txt", "w")
archivo.write("Primer contacto: Uriel\n")
archivo.write("Segundo contacto: Alicia\n")
archivo.write("Tercer contacto: Bob\n")
archivo.close()  # ¡Siempre cerrar!

# ==========================================
# PASO 2: Leer el archivo usando los métodos
# ==========================================
archivo = open("mi_agenda.txt", "r")

# --- Usando readline() ---
print("--- Probando readline() ---")
linea1 = archivo.readline()
print(f"Línea 1: {linea1.strip()}") # .strip() saca el salto de línea sobrante

# --- Usando seek(0) para rebobinar ---
print("\n... Rebobinando al principio con seek(0) ...")
archivo.seek(0)

# --- Usando readlines() ---
print("\n--- Probando readlines() ---")
todas_las_lineas = archivo.readlines()
print(f"Lista generada por readlines: {todas_las_lineas}")

# Como es una lista, podemos recorrerla con un for:
print("\nRecorriendo la lista con un for:")
for linea in todas_las_lineas:
    print(f"-> {linea.strip()}")

archivo.close()  # ¡Cerramos al terminar todo!
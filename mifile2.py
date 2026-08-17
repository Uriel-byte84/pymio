# ==========================================
# 1. CREAMOS UN ARCHIVO CON TRES LÍNEAS
# ==========================================
archivo = open("prueba_lectura.txt", "w")
archivo.write("Línea número UNO\n")
archivo.write("Línea número DOS\n")
archivo.write("Línea número TRES\n")
archivo.close()

# ==========================================
# 2. PROBAMOS LAS FUNCIONES DE LECTURA
# ==========================================
archivo = open("prueba_lectura.txt", "r")

# --- readline() lee de a una sola línea ---
print("--- Probando readline() ---")
primera_linea = archivo.readline()
print(f"Leído con readline: {primera_linea.strip()}")

# --- seek(0) vuelve el puntero al principio ---
print("\n... Usando seek(0) para volver al inicio ...")
archivo.seek(0)

# --- readlines() lee todo y lo hace una lista ---
print("\n--- Probando readlines() ---")
lista_de_lineas = archivo.readlines()
print(f"Leído con readlines (mira los corchetes): {lista_de_lineas}")

archivo.close()
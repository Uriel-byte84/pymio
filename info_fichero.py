# 1. Abrimos el fichero que creamos antes en modo lectura ('r')
fichero = open("aprendizaje.txt", "r")

# 2. Mostramos los datos que nos pide el ejercicio
print("--- DATOS DEL FICHERO ---")
print(f"Nombre del archivo: {fichero.name}")
print(f"Modo de apertura:   {fichero.mode}")
print(f"Codificación:       {fichero.encoding}")

# Verificamos el estado ANTES de cerrarlo
print(f"¿El archivo está cerrado?: {fichero.closed}")

print("-" * 30)

# 3. Cerramos el fichero
fichero.close()

# Verificamos el estado DESPUÉS de cerrarlo
print("... Cerrando archivo ...")
print(f"¿El archivo está cerrado ahora?: {fichero.closed}")
# 1. Abrimos en modo 'a+' (agrega texto y permite leer, si no existe lo crea)
fichero = open("aprendizaje.txt", "a+")

# 2. ESCRIBIMOS la frase adentro del archivo (con un \n al final para el salto de línea)
fichero.write("Estoy aprendiendo Python\n")

# 3. REBOBINAMOS el cursor al principio (posición 0) para poder leer lo que escribimos
fichero.seek(0)

# 4. Leemos el contenido completo del archivo
contenido = fichero.read()

# 5. AHORA SÍ usamos print para mostrar en consola lo que había adentro del archivo
print("--- Contenido del archivo .txt ---")
print(contenido)

# 6. Cerramos el archivo para salvar los cambios
fichero.close()
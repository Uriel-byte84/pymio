# 1. Pedimos el número al usuario y lo convertimos a entero
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# 2. Creamos la lista vacía para almacenar los resultados
tabla = []

# 3. Calculamos la tabla del 1 al 10 usando un bucle
for i in range(1, 11):
    tabla.append(numero * i)

# 4. Mostramos el resultado final en pantalla
print(f"Tabla del {numero}: {tabla}")
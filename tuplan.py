tupla = (2, 8, 3, 10, 5, 7)

# Filtramos primero y luego contamos la longitud
mayores_a_5 = list(filter(lambda x: x > 5, tupla))
cantidad = len(mayores_a_5) 

print(f"Cantidad de elementos > 5: {cantidad}")
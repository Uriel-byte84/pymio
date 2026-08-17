from functools import reduce

tupla = (2, 8, 3, 10, 5, 7)

# El acumulador 'cont' empieza en 0
cantidad = reduce(lambda cont, x: cont + 1 if x > 5 else cont, tupla, 0)

print(f"Cantidad usando reduce: {cantidad}")
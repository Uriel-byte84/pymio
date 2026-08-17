cantidad = int(input("¿Cuántas palabras tendrá la lista?: "))
lista_palabras = []

for i in range(cantidad):
    palabra = input(f"Introduce la palabra {i + 1}: ")
    lista_palabras.append(palabra)

print(f"\nLa lista creada es: {lista_palabras}")

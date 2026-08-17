num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

inicio = min(num1, num2)
fin = max(num1, num2)

# Creamos la lista y la imprimimos
lista_consecutivos = list(range(inicio, fin + 1))
print(f"Números entre {inicio} y {fin}: {lista_consecutivos}")


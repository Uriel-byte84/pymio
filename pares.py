num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Aseguramos el orden de menor a mayor
inicio, fin = min(num1, num2), max(num1, num2)

for i in range(inicio, fin + 1):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
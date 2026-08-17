num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número (debe ser mayor al primero): "))

while num2 <= num1:
    print("Error: El segundo número debe ser mayor que el primero.")
    num2 = int(input("Introduce el segundo número nuevamente: "))

print(f"Los números finales son: {num1} y {num2}")

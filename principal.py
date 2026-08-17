# Script de nivel superior: principal.py

# Importamos las funciones desde nuestro paquete 'operaciones' y el módulo 'calculos'
from operaciones import calculos as calc

print("--- Ejecutando el Script de Nivel Superior ---")

n1 = 10
n2 = 5

# Usamos las funciones gracias al alias 'calc'
resultado_suma = calc.sumar(n1, n2)
resultado_resta = calc.restar(n1, n2)

print(f"El resultado de la suma es: {resultado_suma}")
print(f"El resultado de la resta es: {resultado_resta}")
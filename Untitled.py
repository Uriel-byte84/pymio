meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

try:
    num = int(input(f"Introduce un número entre 1 y {len(meses)}: "))
    if 1 <= num <= len(meses):
        print(f"El mes es: {meses[num - 1]}")
    else:
        print("Error: Número fuera de rango.")
except ValueError:
    print("Error: Debes introducir un número válido.")

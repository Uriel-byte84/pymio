anio = int(input("Introduce un año: "))

# Regla: Múltiplo de 400 O (múltiplo de 4 Y NO múltiplo de 100)
if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")


from functools import reduce

personas = [
    {'Nombre': 'Alicia', 'Edad': 22, 'Sexo': 'F'},
    {'Nombre': 'Bob', 'Edad': 25, 'Sexo': 'M'},
    {'Nombre': 'Charlie', 'Edad': 33, 'Sexo': 'M'},
    {'Nombre': 'Diana', 'Edad': 15, 'Sexo': 'F'},
    {'Nombre': 'Esteban', 'Edad': 30, 'Sexo': 'M'},
    {'Nombre': 'Federico', 'Edad': 44, 'Sexo': 'M'},
]

# 1. Tu código del promedio (que ya funciona genial)
hombres = list(filter(lambda x: x['Sexo'] == 'M', personas))
suma_edades = reduce(lambda suma, p: suma + p['Edad'], hombres, 0)
media_edad = suma_edades / len(hombres)
print(f"El promedio de edad de los hombres es: {media_edad}")
print("-" * 40)

# 2. EL DESAFÍO DEL KEYERROR:
# Agarramos a la primera persona (Alicia)
alicia = personas[0]

try:
    # Intentamos buscar una clave que NO existe en su diccionario
    print(alicia['Telefono']) 
except KeyError:
    # Si Python no encuentra la clave, salta directo acá:
    print("¡Error capturado! KeyError: La clave 'Telefono' no existe en el diccionario.")
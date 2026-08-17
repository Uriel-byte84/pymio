anchura = int(input("Introduce la anchura del rectángulo: "))
altura = int(input("Introduce la altura del rectángulo: "))
caracter = input("Introduce el carácter a utilizar: ")

for i in range(altura):
    print(caracter * anchura)

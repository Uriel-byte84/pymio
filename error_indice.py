# Creamos la lista con los números separados por comas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0  # Empezamos en la posición 0

try:
    # El while va a seguir para siempre...
    while True:
        # Mostramos por pantalla el número en la posición 'i'
        print(f"Posición {i}: El número es {lista[i]}")
        i = i + 1  # Pasamos a la siguiente posición
        
except IndexError:
    # Cuando 'i' valga 9, esa posición no existe y saltará acá
    print(f"\n¡Se cortó el bucle! Capturamos IndexError: La posición {i} está fuera del límite.")
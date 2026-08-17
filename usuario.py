while True:
    numero = int(input("Introduce un número positivo: "))
    
    if numero > 0:
        print(f"¡Correcto! Has introducido el {numero}.")
        break  # Ahora sí, este break frena el bucle 'while'
    else:
        print("Error: El número debe ser positivo. Inténtalo de nuevo.")
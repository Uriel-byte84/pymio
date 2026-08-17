from tkinter import Tk, Label

# Creamos la ventana principal
ventana = Tk()
ventana.title("Mi Primer Menú")
ventana.geometry("300x200")

# Agregamos un texto de bienvenida
etiqueta = Label(ventana, text="¡Hola! Si ves esto, funciona.")
etiqueta.pack(pady=50)

# Iniciamos la aplicación
ventana.mainloop()
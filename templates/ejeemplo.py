import tkinter as tk

def seleccionar_opcion(opcion):
    if opcion == 'Opción 1':
        print("Ejecutando acción 1.")
    elif opcion == 'Opción 2':
        print("Ejecutando acción 2.")
    elif opcion == 'Opción 3':
        print("Ejecutando acción 3.")

# Crear la ventana principal
root = tk.Tk()
root.title("Menú Desplegable")

# Crear una variable Tkinter para mantener la selección
seleccionada = tk.StringVar()

# Crear el menú desplegable
opciones_menu = ['Opción 1', 'Opción 2', 'Opción 3']
menu = tk.OptionMenu(root, seleccionada, *opciones_menu, command=seleccionar_opcion)
menu.pack()

# Iniciar el bucle de eventos
root.mainloop()


# fsgfsg
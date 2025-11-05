import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 

def obtener_entero():
    texto_obtenido = preguntar_opcion.get() # Obtener el texto del Entry
    try:
        # Convertir el texto a entero
        valor_entero = int(texto_obtenido)
        messagebox.showinfo("Resultado", f"El número es: {valor_entero}")
    except ValueError:
        # Manejar el error si el texto no es un número válido
        messagebox.showerror("Error", "Por favor, introduce un número entero válido.")
    if valor_entero == 250:
        accion.configure(text='el precio es de 16000')
    elif valor_entero == 100:
        accion.configure(text='el precio es de 11000')
    elif valor_entero == 80:
        accion.configure(text='el precio es de 8000')
    elif valor_entero == 50:
        accion.configure(text='el precio es de 4500')
    else:
        accion.configure(text='cuaderno no encontrado')

ventana = tk. Tk()
ventana.title ('Lista de cuadernos')
ventana.geometry('500x100')

etiqueta = tk.Label(ventana, text="Ingresa el valor del cuaderno ue deseas consultar", font=('Arial', 10, 'bold'))
etiqueta.pack(pady=20)
etiqueta.grid(column=1,  row=0)


opcion = tk.IntVar()
preguntar_opcion= tk.Entry(ventana, width=20, textvariable=opcion)
preguntar_opcion.grid(column=1, row=1)

boton = tk.Button(ventana, text="Obtener Número", command=obtener_entero)
boton.grid(column=2, row=1)

accion = ttk.Button(ventana, text='Consultar precio', command= obtener_entero)
accion.grid(column=1, row=2)

ventana.mainloop()
import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        estatura = float(entry_estatura.get())

        if peso <= 0 or estatura <= 0:
            messagebox.showerror("Error", "El peso y la estatura deben ser valores positivos.")
            return

        imc = peso / (estatura ** 2)

        if imc < 18.5:
            resultado = "Bajo peso"
        elif 18.5 <= imc < 25:
            resultado = "Peso ideal"
        elif 25 <= imc < 30:
            resultado = "Sobrepeso"
        else:
            resultado = "Obesidad"

        label_resultado.config(text=f"Tu IMC es {imc:.2f}. Clasificación: {resultado}")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Ventana principal
ventana = tk.Tk()

ventana.title("Control de Peso Saludable")
etiqueta = tk.Label(ventana, text="Indice de IMC para una vida saludable", font=("Courier New", 12))
etiqueta.pack(pady=20)
etiqueta.grid(column=1,  row=0)

ventana.configure(bg='#90EE90')
ventana.geometry("500x200")

# Etiquetas y entradas
tk.Label(ventana, text="Peso (kg):").grid(row=1, column=0)
entry_peso = tk.Entry(ventana)
entry_peso.grid(row=1, column=1)

tk.Label(ventana, text="Estatura (m):").grid(row=2, column=0)
entry_estatura = tk.Entry(ventana)
entry_estatura.grid(row=2, column=1)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular IMC", command=calcular_imc)
boton_calcular.grid(row=3, column=1)

# Resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=4, column=0)

ventana.mainloop()
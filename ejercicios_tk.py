#Crear una ventana simple:

import tkinter as tk

ventana = tk.Tk()
ventana.mainloop()
#Este es el ejemplo más básico. Creamos una ventana vacía.
#------------------------------------------------------------------------------

#Crear una ventana con título:
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.mainloop()
#Aquí hemos agregado un título a la ventana.
#------------------------------------------------------------------------------

#Crear una etiqueta:
import tkinter as tk

ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Hola, tkinter!")
etiqueta.pack()
ventana.mainloop()
#Creamos una etiqueta y la agregamos a la ventana.
#------------------------------------------------------------------------------

#Crear un botón:
import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Hola desde tkinter!")

ventana = tk.Tk()
boton = tk.Button(ventana, text="Presionar", command=mostrar_mensaje)
boton.pack()
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()
ventana.mainloop()
#Agregamos un botón que actualiza una etiqueta cuando se presiona.
#------------------------------------------------------------------------------

#Crear una entrada de texto:
import tkinter as tk

def mostrar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto)

ventana = tk.Tk()
entrada = tk.Entry(ventana)
entrada.pack()
boton = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto)
boton.pack()
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()
ventana.mainloop()
#Creamos una entrada de texto y un botón para mostrar el texto ingresado.

#------------------------------------------------------------------------------

#Crear un cuadro de lista (Listbox):
import tkinter as tk

def mostrar_elemento():
    seleccion = lista.curselection()
    etiqueta.config(text=f"Seleccionaste: {lista.get(seleccion)}")

ventana = tk.Tk()
lista = tk.Listbox(ventana)
lista.insert(1, "Elemento 1")
lista.insert(2, "Elemento 2")
lista.pack()
boton = tk.Button(ventana, text="Mostrar Elemento", command=mostrar_elemento)
boton.pack()
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()
ventana.mainloop()
#Creamos un cuadro de lista y un botón para mostrar el elemento seleccionado.

#------------------------------------------------------------------------------

#Crear una ventana emergente (Toplevel):
import tkinter as tk

def abrir_ventana_emergente():
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Ventana Emergente")
    etiqueta_emergente = tk.Label(ventana_emergente, text="¡Esta es una ventana emergente!")
    etiqueta_emergente.pack()

ventana = tk.Tk()
boton = tk.Button(ventana, text="Abrir Ventana Emergente", command=abrir_ventana_emergente)
boton.pack()
ventana.mainloop()
#Creamos una ventana emergente al hacer clic en un botón.

#------------------------------------------------------------------------------

#Crear una ventana modal (messagebox):
import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "Hola, soy un messagebox!")

ventana = tk.Tk()
boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack()
ventana.mainloop()
#Mostramos un cuadro de diálogo modal (messagebox).

#------------------------------------------------------------------------------

#Crear una barra de desplazamiento (Scrollbar):
import tkinter as tk

ventana = tk.Tk()
scrollbar = tk.Scrollbar(ventana)
scrollbar.pack(side="right", fill="y")
lista = tk.Listbox(ventana, yscrollcommand=scrollbar.set)
for i in range(100):
    lista.insert("end", f"Elemento {i}")
lista.pack(side="left")
scrollbar.config(command=lista.yview)
ventana.mainloop()
#Creamos una barra de desplazamiento para una lista larga.

#------------------------------------------------------------------------------
#Diseño de una calculadora básica:
import tkinter as tk

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        resultado.set(num1 + num2)
    except ValueError:
        resultado.set("Error")

ventana = tk.Tk()
ventana.title("Calculadora")

entrada_num1 = tk.Entry(ventana)
entrada_num1.pack()
entrada_num2 = tk.Entry(ventana)
entrada_num2.pack()

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack()

resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack()

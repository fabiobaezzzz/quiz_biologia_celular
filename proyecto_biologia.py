import tkinter as tk
import random
import json
from tkinter import messagebox
preguntas_juego = []
indice = 0
puntaje = 0
variables =[]
frame_juego = None
def cargar_preguntas():
    try:
        with open("preguntas.JSON","r",encoding="utf-8") as archivo:
            preguntas = json.load(archivo)
    except FileNotFoundError:
        messagebox.showerror("error ", "archivo no encontrado")
        return None
    except json.JSONDecodeError:
        messagebox.showerror("error","de formato del archivo" )
        return None
    return random.sample(preguntas, 5)
def calcular_puntos (seleccionadas, correctas):
    if seleccionadas == sorted(correctas):
        return 15
    else: return -5
def validar():
    global indice, puntaje, aciertos, fallos
    seleccionadas = []
    for i in range(len(variables)):
        if variables[i].get() == 1:
            seleccionadas.append(i)

    correctas = preguntas_juego[indice]["correctas"]
    puntos = calcular_puntos(seleccionadas, correctas)
    puntaje = puntaje + puntos
    if puntos == 15:
        aciertos = aciertos + 1
    else:
        fallos = fallos + 1

    indice = indice + 1
    if indice < 5:
        mostrar_preguntas()
    else:
        messagebox.showinfo("Fin", f"Puntaje final: {puntaje}")
def mostrar_preguntas():
    global variables, frame_juego
    if frame_juego is not None:
        frame_juego.destroy()
    frame_juego = tk.Frame(ventana)
    frame_juego.pack()
    pregunta = preguntas_juego[indice]
    tk.Label(frame_juego, text=f"pregunta {indice + 1} de 5  Puntaje : {puntaje}") .grid(row=0,column=0, columnspan=2)
    tk.Label(frame_juego, text= pregunta["pregunta"], font=('Times New Roman', 14), fg="#0a0a0a").grid(row=1, column=0, columnspan=2)
    variables = []
    for i, opcion in enumerate(pregunta["opciones"]):
        var= tk.IntVar()
        variables.append(var)
        tk.Checkbutton(frame_juego, text=opcion, variable=var ) .grid(row=2 + i // 2, column= i % 2)
    tk.Button(frame_juego, text="Validar", command=validar).grid(row=4, column=0, columnspan=2)
def iniciar ():
    global preguntas_juego, indice, puntaje, aciertos, fallos
    nombre = entrada_nombre.get()
    preguntas = cargar_preguntas()
    if preguntas is None:
        return
    preguntas_juego = preguntas
    indice = 0
    puntaje = 0 
    aciertos = 0
    fallos = 0
    frame_inicio.destroy()
    mostrar_preguntas()

ventana = tk.Tk()
ventana .title("inicio")
ventana .geometry('500x500')
frame_inicio = tk.Frame(ventana)
frame_inicio.pack()
label = tk.Label(frame_inicio, text='listo para jugar?')
label.pack()
label = tk.Label(frame_inicio, text='primero ingresa tu nombre')
label.pack()
entrada_nombre = tk.Entry(frame_inicio)
entrada_nombre.pack()
boton = tk.Button(frame_inicio, text= 'iniciar', command=iniciar) 
boton.pack()
ventana.mainloop()
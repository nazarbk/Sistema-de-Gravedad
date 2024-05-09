import tkinter as tk
import time
from cuerpo import Cuerpo
import math
aux = True

def actualizardatos(label, cuerpo2, cuerpo3):
    texto = "Cuerpo 1: "
    texto += "\n    Masa: {}".format(cuerpo2.masa)
    texto += "\n    Velocidad en X: {:.2f}".format(int(cuerpo2.velocidad_x * 100) / 100)
    texto += "\n    Velocidad en Y: {:.2f}".format(int(cuerpo2.velocidad_y * 100) / 100)
    texto += "\n    Posición (X, Y): ({:.2f}".format(cuerpo2.x)
    texto += ", {:.2f}".format(cuerpo2.y)
    texto += ")"
    texto += "\n    Aceleración en X: {:.2f}".format(int(cuerpo2.aceleracion_x * 100) / 100)
    texto += "\n    Aceleración en Y: {:.2f}".format(int(cuerpo2.aceleracion_y * 100) / 100)
    texto += "\n    Distancia respecto al Cuerpo 0: {:.2f}".format(cuerpo2.distancia)
    texto += "\n    Fuerza de atracción: {:.2f}".format(cuerpo2.fuerza)

    texto += "\n\nCuerpo 2: "
    texto += "\n    Masa: {}".format(cuerpo3.masa)
    texto += "\n    Velocidad en X: {:.2f}".format(int(cuerpo3.velocidad_x * 100) / 100)
    texto += "\n    Velocidad en Y: {:.2f}".format(int(cuerpo3.velocidad_y * 100) / 100)
    texto += "\n    Posición (X, Y): ({:.2f}".format(cuerpo3.x)
    texto += ", {:.2f}".format(cuerpo3.y)
    texto += ")"
    texto += "\n    Aceleración en X: {:.2f}".format(int(cuerpo3.aceleracion_x * 100) / 100)
    texto += "\n    Aceleración en Y: {:.2f}".format(int(cuerpo3.aceleracion_y * 100) / 100)
    texto += "\n    Distancia respecto al Cuerpo 0: {:.2f}".format(cuerpo3.distancia)
    texto += "\n    Fuerza de atracción: {:.2f}".format(cuerpo3.fuerza)
    
    label.config(text = texto)

def pausarSimulacion(event):
    global aux
    if aux == True and event.keysym == "d":
        aux = False
        print("Tecla presionada:", event.keysym)
    else:
        aux = True
        print("Tecla presionada:", event.keysym)

def dibujarCuadricula(ventana, lienzo, ancho, alto):
    for x in range(0, ancho, 10):
        lienzo.create_line(x, 0, x, alto, fill="gray")

    for y in range(0, alto, 10):
        lienzo.create_line(0, y, ancho, y, fill="gray")

def main():
    ventana = tk.Tk()
    ventana.title("Simulación de partícula")
    ancho = 700
    alto = 900
    lienzo = tk.Canvas(ventana, width=ancho, height=alto)
    label = tk.Label(ventana, text='Datos:', justify="left")
    label.pack(side="top", anchor="nw", padx=10, pady=10)
    lienzo.pack()

    #dibujarCuadricula(ventana, lienzo, ancho, alto)

    cuerpo = Cuerpo(
        lienzo, 
        351, 
        451, 
        masa = 60,
        velocidad_x=0, 
        velocidad_y=0, 
        aceleracion_x=0, 
        aceleracion_y=0,
        distancia=0, 
        fuerza=0  
    )

    cuerpo2 = Cuerpo(
        lienzo, 
        270, 
        245, 
        masa = 10,
        velocidad_x=3, 
        velocidad_y=1, 
        aceleracion_x=0, 
        aceleracion_y=0,
        distancia=0, 
        fuerza=0   
    )

    cuerpo3 = Cuerpo(
        lienzo, 
        270, 
        245, 
        masa = 70,
        velocidad_x=4, 
        velocidad_y=1, 
        aceleracion_x=0, 
        aceleracion_y=0,
        distancia=0, 
        fuerza=0     
    )

    ventana.bind("<Key>", pausarSimulacion)

    while True:
        if aux:
            cuerpo2.update_position(cuerpo)
            cuerpo3.update_position(cuerpo)
        ventana.update()
        actualizardatos(label, cuerpo2, cuerpo3)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
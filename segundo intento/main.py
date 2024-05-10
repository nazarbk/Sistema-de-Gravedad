import tkinter as tk
import time
from cuerpo import Cuerpo
import math
aux = True

def actualizardatos(label, cuerpo):
    texto =  "   Masa: {}".format(cuerpo.masa)
    texto += "\n    Velocidad en X: {:.2f}".format(int(cuerpo.velocidad_x * 100) / 100)
    texto += "\n    Velocidad en Y: {:.2f}".format(int(cuerpo.velocidad_y * 100) / 100)
    texto += "\n    Posición (X, Y): ({:.2f}".format(cuerpo.x)
    texto += ", {:.2f}".format(cuerpo.y)
    texto += ")"
    texto += "\n    Aceleración en X: {:.2f}".format(int(cuerpo.aceleracion_x * 100) / 100)
    texto += "\n    Aceleración en Y: {:.2f}".format(int(cuerpo.aceleracion_y * 100) / 100)
    texto += "\n    Distancia respecto al Cuerpo 0: {:.2f}".format(cuerpo.distancia)
    texto += "\n    Fuerza de atracción: {:.2f}".format(cuerpo.fuerza)
    
    label.config(text = texto)

def obtenerParametros():
    ventana_parametros = tk.Toplevel()
    ventana_parametros.title("Ingrese los siguientes parametros:")

    def almacenarParametros():
        masa = float(entry_masa.get())
        velocidad_x = float(entry_vel_x.get())
        velocidad_y = float(entry_vel_y.get())

        cuerpo = {
            "masa": masa,
            "velocidad_x": velocidad_x,
            "velocidad_y": velocidad_y
        }

        print("Parámetros guardados:", cuerpo)

        tk.Label(ventana_parametros, text="Masa:").grid(row=0, column=0, padx=5, pady=5)
        entry_masa = tk.Entry(ventana_parametros)
        entry_masa.grid(row=0, column=0, padx=5, pady=5)

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
    info_frame = tk.Frame(ventana)
    label_cuerpo2 = tk.Label(info_frame, text='Cuerpo 2:', justify="left")
    label_cuerpo3 = tk.Label(info_frame, text='Cuerpo 3:', justify="left")
    label_info_cuerpo2 = tk.Label(info_frame, text='', justify="left")
    label_info_cuerpo3 = tk.Label(info_frame, text='', justify="left")
    
    label_cuerpo2.grid(row=0, column=0, sticky="w")
    label_info_cuerpo2.grid(row=1, column=0, sticky="w")
    label_cuerpo3.grid(row=0, column=1, sticky="w")
    label_info_cuerpo3.grid(row=1, column=1, sticky="w")

    info_frame.pack(side="top", anchor="nw", padx=10, pady=10)
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
        velocidad_y=2, 
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
        actualizardatos(label_info_cuerpo2, cuerpo2)
        actualizardatos(label_info_cuerpo3, cuerpo3)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
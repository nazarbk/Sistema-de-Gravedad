import tkinter as tk
import time
from cuerpo import Cuerpo

def actualizardatos(label, cuerpo2, cuerpo3):
    datos = 0

def main():
    ventana = tk.Tk()
    ventana.title("Simulación de partícula")
    lienzo = tk.Canvas(ventana, width=900, height=700)
    label = tk.Label(ventana, text='Datos:')
    label.pack(side="top", anchor="nw", padx=10, pady=10)
    lienzo.pack()

    cuerpo = Cuerpo(
        lienzo, 
        351, 
        451, 
        masa = 60,
        velocidad_x=0, 
        velocidad_y=0, 
        aceleracion_x=0, 
        aceleracion_y=0
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
    )

    while True:
        cuerpo2.update_position(cuerpo)
        cuerpo3.update_position(cuerpo)
        ventana.update()
        actualizardatos(label, cuerpo2, cuerpo3)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
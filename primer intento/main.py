import tkinter as tk
import time
from cuerpos import Cuerpo

def main():
    ventana = tk.Tk()
    ventana.title("Simulación de partícula")
    lienzo = tk.Canvas(ventana, width=900, height=700)
    lienzo.pack()

    cuerpo = Cuerpo(
        lienzo, 
        345, 
        345, 
        velocidad_x=0, 
        velocidad_y=0, 
        aceleracion_x=0, 
        aceleracion_y=0, 
        masa = 80
    )

    cuerpo2 = Cuerpo(
        lienzo, 
        300, 
        100, 
        velocidad_x=2, 
        velocidad_y=1, 
        aceleracion_x=0, 
        aceleracion_y=0, 
        masa = 10
    )

    while True:
        cuerpo2.actualizar_posicion(cuerpo)
        ventana.update()
        time.sleep(0.05)

if __name__ == "__main__":
    main()
G = 6.67e-11
import math

class Cuerpo:

    def __init__(self, canvas, x, y, velocidad_x, velocidad_y, aceleracion_x, aceleracion_y, masa):
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x+10, y+10, fill="black")
        self.x = x
        self.y = y
        self.velocidad_x = velocidad_x 
        self.velocidad_y = velocidad_y 
        self.aceleracion_x = aceleracion_x
        self.aceleracion_y = aceleracion_y
        self.masa = masa

    def actualizar_posicion(self, cuerpo):
        #Controlar posiciones de la particula
        self.x = self.canvas.coords(self.id)[0]
        self.y = self.canvas.coords(self.id)[1]
        self.x2 = self.canvas.coords(self.id)[2]
        self.y2 = self.canvas.coords(self.id)[3]
        
        #Actualizar velocidad v = v + a
        aceleracionx, aceleraciony = self.fuerzag(cuerpo)

        self.velocidad_x += aceleracionx
        self.velocidad_y += aceleraciony

        self.canvas.move(self.id, self.velocidad_x, self.velocidad_y)

        print(self.x, self.y)

    def fuerzag(self, cuerpo):
        dx = cuerpo.x - self.x
        dy = cuerpo.y - self.y
        radio = math.sqrt(pow(dx,2) + pow(dy,2))

        #Normalizar vector dirección

        fuerza = (G * self.masa * cuerpo.masa) / pow(radio, 2)
        aceleracion = (fuerza/self.masa) * 10e10 
        
        if dx > 0:
            if dy > 0:
                return aceleracion, aceleracion
            else:
                return aceleracion, -aceleracion
        else:
            if dy > 0:
                return -aceleracion, aceleracion
            else:
                return -aceleracion, -aceleracion



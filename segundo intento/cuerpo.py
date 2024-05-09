G = 6.67e-11
import math

class Cuerpo:
    def __init__(self, canvas, x, y, masa, velocidad_x, velocidad_y, aceleracion_x, aceleracion_y, distancia, fuerza):
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x+masa/10, y+masa/10, fill="black")
        self.masa = masa
        self.x = x
        self.y = y
        self.velocidad_x = velocidad_x
        self.velocidad_y = velocidad_y
        self.aceleracion_x = aceleracion_x
        self.aceleracion_y = aceleracion_y
        self.distancia = 0
        self.fuerza = 0
    
    def update_position(self, cuerpo):
        self.aceleracion_x, self.aceleracion_y = self.gravityforce(cuerpo)

        self.velocidad_x += self.aceleracion_x
        self.velocidad_y += self.aceleracion_y

        self.x += self.velocidad_x
        self.y += self.velocidad_y

        self.body1 = self.canvas.create_line(self.x, self.y, self.x-self.velocidad_x, self.y-self.velocidad_y, fill='blue')

        #print("vel_x:", self.velocidad_x)
        #print("vel_y:", self.velocidad_y)
        #print("pos_x:", self.x)
        #print("pos_y:", self.y)

        self.canvas.move(self.id, self.velocidad_x, self.velocidad_y)

    def gravityforce(self, cuerpo):
        d1 = cuerpo.x - self.x 
        d2 = cuerpo.y - self.y
        r = math.sqrt(pow(d1, 2) + pow(d2, 2))
        self.distancia = r

        force = G * self.masa *  cuerpo.masa/ pow(r, 2) * pow(10,12.1)
        self.fuerza = force
        #print("fuerza:", self.fuerza)
        #print("masa:", self.masa)
        aceleracion = force / self.masa
        
        
        angulo = math.atan2(d2, d1)
        aceleracion_x = aceleracion * math.cos(angulo)
        aceleracion_y = aceleracion * math.sin(angulo)
        #print("acel:",aceleracion_x)
        #print("acel:",aceleracion_y)

        return aceleracion_x, aceleracion_y
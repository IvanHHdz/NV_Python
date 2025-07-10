from math import sin, cos, pi

g = 9.8

class Punto:
    def __init__(self, velocidad_inicial):
        self.velocidad = velocidad_inicial
        self.tiempo = 0
    
    def posicion_en(self, t):
        vx, vy = self.velocidad
        x, y = (vx*t, vy*t - .5 * g * (t ** 2))
        print(f"Coordenadas en t = {t}:  ({x:.2f}, {y:.2f})")
    
    def tabla(self, tf, intervalo, ti = 0):
        t = ti
        while t <= tf:
            self.posicion_en(t)
            t += intervalo

def vector(magnitud, angulo):
    x, y = magnitud * cos(angulo), magnitud * sin(angulo)
    return [x, y]

def grado_a_radianes(grados):
    return grados * (pi / 180)

def dato(str):
    while True:
        try:
            dato = float(input(str))
            return dato
        except:
            print("Ingrese un valor válido\n")
            continue

def main():
    magnitud = dato("Magnitud de la velocidad inicial v0 (m/s): ")
    angulo = dato("Ángulo de lanzamiento θ (grados): ")
    objeto = Punto(vector(magnitud, angulo))
    i = dato("Intervalo de tiempo (s): ")
    tf = dato("Tiempo total de simulación (s): ")
    objeto.tabla(tf, i)

if __name__ == "__main__":
    main()
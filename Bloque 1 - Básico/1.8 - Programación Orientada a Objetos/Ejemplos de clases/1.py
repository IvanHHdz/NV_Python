class Carro:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca
    
    def cambiar_de_color(self, nuevo_color):
        self.color = nuevo_color

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau guau!")

def main():
    mi_perro = Perro("Firulais")
    mi_perro.ladrar()
    

if __name__ == "__main__":
    main()
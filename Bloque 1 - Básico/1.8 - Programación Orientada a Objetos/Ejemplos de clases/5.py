class Caja:
    # Constructor, se ejecuta al crear el objeto y necesita del color
    def __init__(self, color):
        self.color = color
        self.contenido = []
    
    def agregar(self, item):
        self.contenido.append(item)
    
    # Esta es la forma en que se representa el objeto como una str
    def __str__(self):
        return f'Esta es una caja {self.color}\nContenido: {self.contenido}'

    # Con esto podemos ver su tamaño
    def __len__(self):
        return len(self.contenido)

    # Obtenemos un item del objeto
    def __getitem__(self, i):
        return self.contenido[i]

    # Asignamos items al objeto
    def __setitem__(self, i, value):
        self.contenido[i] = value
    
    # Definimos la suma del objeto
    def __add__(self, other):
        nueva_caja = Caja(self.color)
        nueva_caja.contenido = self.contenido + other.contenido
        return nueva_caja
    
    # Definimos la igualdad de objetos
    def __eq__(self, other):
        if self.color != other.color:
            return False
        elif self.contenido != other.contenido:
            return False
        else:
            return True
        
def main():
    caja1 = Caja("roja")
    caja1.agregar("juguete")
    caja1.agregar("libro")
    print(caja1)

    caja2 = Caja("azul")
    caja2.agregar("ropa")
    caja2.agregar("zapatos")
    print(caja2)

    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b   # [1, 2, 3, 4, 5, 6]
    caja3 = caja1 + caja2
    print(caja3)

    print(caja1 == caja2)
    print(caja1 == caja3)

if __name__ == "__main__":
    main()
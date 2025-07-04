class Botella:
    def __init__(self, contenido, precio):
        self.contenido = contenido
        self.precio = precio
        
    def __str__(self):
        return f"Botella: {self.contenido} - {self.precio}€"
    
def main():
    mi_botella = Botella("Agua", 1.50)
    print(mi_botella)
    
if __name__ == "__main__":
    main()
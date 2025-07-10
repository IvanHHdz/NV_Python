class Tablero:
    def __init__(self):
        self.filas = 3
        self.columnas = 3
        self.tablero = [["   " for _ in range(self.columnas)] for _ in range(self.filas)]
        self.coordenadas = {
            '1' : (0, 0), 
            '2' : (0, 1), 
            '3' : (0, 2),
            '4' : (1, 0), 
            '5' : (1, 1), 
            '6' : (1, 2),
            '7' : (2, 0), 
            '8' : (2, 1), 
            '9' : (2, 2)
        }

    def mostrar(self):
        print("Tablero:")
        for i in range(self.filas):
            for j in range(self.columnas):
                print(self.tablero[i][j], end="")
                if j < self.columnas - 1:
                    print("|", end="")
            if i < self.filas - 1:
                print("\n" + "-" * (self.columnas * 4 - 1))
            else:
                print("\n")

    def actualizar(self, simbolo):
        while True:
            posicion = input(f"Jugador {simbolo}, elige una posición (1-9): ")
            if posicion in self.coordenadas:
                fila, columna = self.coordenadas[posicion]
                if self.tablero[fila][columna] == "   ":
                    self.tablero[fila][columna] = f" {simbolo} "
                    break
                else:
                    print("Posición ya ocupada. Elige otra.")
            else:
                print("Posición inválida. Elige un número del 1 al 9.")

    def verificar(self):
        for fila in self.tablero:
            if fila.count(fila[0]) == self.columnas and fila[0] != "   ":
                return True
        
        for j in range(self.columnas):
            if all(self.tablero[i][j] == self.tablero[0][j] and self.tablero[0][j] != "   " for i in range(self.filas)):
                return True
        
        if all(self.tablero[i][i] == self.tablero[0][0] and self.tablero[0][0] != "   " for i in range(self.filas)):
            return True
        if all(self.tablero[i][self.columnas - 1 - i] == self.tablero[0][self.columnas - 1] and self.tablero[0][self.columnas - 1] != "   " for i in range(self.filas)):
            return True
        
        return False

def main():
    tablero = Tablero()
    x = True
    while True:
        tablero.mostrar()
        tablero.actualizar("X" if x else "O")
        x = not x
        if tablero.verificar():
            tablero.mostrar()
            print(f"¡{'X' if not x else 'O'} ha ganado!")
            break

if __name__ == "__main__":
    main()
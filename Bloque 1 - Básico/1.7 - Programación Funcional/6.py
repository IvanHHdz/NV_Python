def multiplicador(n):
    def multiplicar(x):
        return n * x
    return multiplicar

def main():
    doble = multiplicador(2)
    print(f"Doble de 10: {doble(10)}")
    triple = multiplicador(3)
    print(f"Triple de 10: {triple(10)}")
    cuadrado = multiplicador(4)
    print(f"Cuadrado de 10: {cuadrado(10)}")

if __name__ == "__main__":
    main()
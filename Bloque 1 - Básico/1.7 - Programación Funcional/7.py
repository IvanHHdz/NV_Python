def sume(n):
    def sumar(x):
        return n + x
    return sumar

def main():
    subir = sume(1)
    print(f"Subir 10: {subir(10)}")
    bajar = sume(-1)
    print(f"Bajar 10: {bajar(10)}")

if __name__ == "__main__":
    main()
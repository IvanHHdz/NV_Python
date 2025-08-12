def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def operar(a, b, operacion):
    return operacion(a, b)

def main():
    operaciones = [sumar, restar, multiplicar, sumar, sumar, sumar]
    for operacion in operaciones:
        resultado = operar(5, 3, operacion)
        print(f"{resultado}")

if __name__ == "__main__":
    main()
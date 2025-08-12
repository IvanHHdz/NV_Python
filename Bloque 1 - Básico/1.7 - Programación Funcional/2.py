def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def operar(a, b, operacion):
    return operacion(a, b)

def main():
    resultado = operar(5, 3, multiplicar)
    print(resultado)

if __name__ == "__main__":
    main()
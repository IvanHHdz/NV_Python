def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def operar(a, b, operacion):
    return operacion(a, b)

def main():
    operaciones = {
        "+": sumar,
        "-": restar,
        "*": multiplicar
    }
    operacion = input("Ingrese la operación (+, -, *): ")
    resultado = operaciones[operacion](5, 3)
    print(f"Resultado de la operación '{operacion}': {resultado}")

if __name__ == "__main__":
    main()
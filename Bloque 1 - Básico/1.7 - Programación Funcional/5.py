def main():
    operaciones = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b
    }

    operacion = input("Ingrese la operación (+, -, *): ")
    resultado = operaciones[operacion](5, 3)
    print(f"Resultado de la operación '{operacion}': {resultado}")

if __name__ == "__main__":
    main()
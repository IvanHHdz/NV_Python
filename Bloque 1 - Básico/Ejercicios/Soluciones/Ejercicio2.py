operaciones ={
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error: División por cero"
}

def option():
    while True:
        usr = input("Elige la operación (+, -, *, /): ")
        if usr in ['+', '-', '*', '/']:
            return usr
        print("Operación inválida. Inténtalo de nuevo.")

def main():
    while True:
        usr = option()
        if usr is None:
            continue
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = operaciones[usr](num1, num2)
        print(f"El resultado: {resultado}")

if __name__ == "__main__":
    main()
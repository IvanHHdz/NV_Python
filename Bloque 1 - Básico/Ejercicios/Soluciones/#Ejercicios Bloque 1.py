#Ejercicios Bloque 1

#Ejercicio 1

#Ejercicio 2
def calculadora():
    print("Calculadora básica")
    print("Operaciones disponibles: +, -, *, /")

    operacion = input("Elige la operación (+, -, *, /): ")

    if operacion not in ["+", "-", "*", "/"]:
        print("Operación no válida.")
        return

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Debes ingresar números.")
        return

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        try:
            resultado = num1/num2
        except ZeroDivisionError:
            print("Division entre 0 no se puede")
            return

    print(f"Resultado: {resultado}")

# Ejecutar la calculadora
calculadora()

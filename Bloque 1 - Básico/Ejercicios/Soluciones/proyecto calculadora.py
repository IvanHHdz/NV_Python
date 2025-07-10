
# Calculadora  en Python

# Mostramos las opciones al usuario
print("Elige la operación (+, -, *, /):")
operacion = input()

# Pedimos los dos números
# Usamos float para que acepte decimales también
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Verificamos qué operación quiere hacer el usuario
if operacion == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacion == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacion == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacion == "/":
    # Validamos que no se divida entre cero
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print("Resultado:", resultado)

else:
    # Si el usuario escribe algo incorrecto
    print("Operación no válida. Por favor elige +, -, * o /.")

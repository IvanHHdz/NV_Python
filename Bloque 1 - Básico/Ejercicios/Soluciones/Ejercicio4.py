def fibonacci(k):
    if k <= 2:
        return 1
    else:
        return fibonacci(k - 1) + fibonacci(k - 2)

def cuadrados(k):
    return k ** 2

def triangulos(k):
    return k * (k + 1) // 2

def padovan(k):
    if k <= 3:
        return 1
    else:
        return padovan(k - 2) + padovan(k - 3)

def catalan(k):
    return factorial(2 * k) // (factorial(k + 1) * factorial(k))

sucesiones = {
    '1' :   fibonacci,
    '2' :   cuadrados,
    '3' :   triangulos,
    '4' :   padovan,
    '5' :   catalan
}

def mostrar(sucesion, valor):
    P = sucesiones[sucesion]
    for i in range(1, valor + 1):
        print(P(i), end=", ")
    print()

def main():
    while True:
        print("Seleccione una sucesión: ")
        print("\t[1] - Sucesión de Fibonacci")
        print("\t[2] - Sucesión de cuadrados")
        print("\t[3] - Sucesión de triángulos")
        print("\t[4] - Sucesión de Padovan")
        print("\t[5] - Sucesión de Catalan")
        sucesion = input()
        if not sucesion in sucesiones.keys():
            input("Seleccione una sucesión válida\n")
            continue
        valores = input("Seleccione cuantos números desea ver: ")
        if not valores.isdigit() or int(valores) <= 0:
            input("Ingese un valor válido\n")
            continue
        valor = int(valores)
        
        mostrar(sucesion,valor)

def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

if __name__ == "__main__":
    main()
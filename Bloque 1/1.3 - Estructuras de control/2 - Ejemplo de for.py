for i in range(-1, 3):
    edad = int(input("¿Cuál es tu edad? "))
    if edad < 18:
        print("Eres menor de edad")
    elif edad < 65:
        print("Eres mayor de edad")
    else:
        print("Eres un adulto mayor")
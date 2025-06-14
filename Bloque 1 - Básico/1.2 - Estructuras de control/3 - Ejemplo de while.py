edad = 0

while edad >= 0:
    edad = int(input("¿Cuál es tu edad? "))
    if edad < 18:
        print("Eres menor de edad")
    elif edad < 65:
        print("Eres mayor de edad")
    else:
        print("Eres un adulto mayor")
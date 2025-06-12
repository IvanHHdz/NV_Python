# Define una variable global
valor = 10

# Ejemplo de función que saluda a un usuario
def saludar(nombre):
    print("Hola " + nombre)

# Función principal que utiliza la función saludar y una variable global
def main():
    usuario = "Pablo"
    saludar(usuario)
    # Accede a la variable global y la modifica
    global valor
    valor = 12
    print(valor)

# Bloque de código que se ejecuta al correr el script
if __name__ == "__main__":
    main()
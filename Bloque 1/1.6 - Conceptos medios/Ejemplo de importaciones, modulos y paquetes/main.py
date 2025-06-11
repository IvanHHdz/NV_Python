import funciones    # Importamos funciones, haciendo que las funciones de funciones.py estén disponibles desde main.py
import modulos.funciones    # Importamos funciones, haciendo que las funciones de modulos/funciones.py estén disponibles desde main.py

def main():         # Hacemos una función llamada main()
    print(funciones.cuadrado(5))    # Llamamos la función declarada en el archivo o módulo funciones.py
    # Para llamarla, primero debemos especificar desde dónde la llamamos, es decir, la llamamos a funciones
    print(modulos.funciones.cuadrado(6))  # Llamamos la función declarada en el archivo o módulo modulos/funciones.py
    # Para llamarla, primero debemos especificar desde dónde la llamamos, es decir, la llamamos a modulos.funciones

# Esta parte de aquí es una buena práctica que se hace para tener el código más ordenado 
# Sirve para ejecutar la función main() si se está ejecutando el archivo
if __name__ == "__main__":
    main()
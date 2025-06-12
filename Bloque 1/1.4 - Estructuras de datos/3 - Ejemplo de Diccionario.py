# Ejemplo de Diccionario
diccionario = {
    "fruta" : ["Manzana", "Pera", "Sandia"],
    "verduras" : ("Tomate", "Zanahoria")
}

print(diccionario)  # Imprime el diccionario

# Añadir un nuevo elemento al diccionario
diccionario["ciudades"] = ["San Pedro Sula", "Tegucigalpa"]

# Imprimir el diccionario actualizado
print(diccionario)

# Crea una variable para acceder a un elemento del diccionario
clave = "frUTa"
print(diccionario[clave.lower()])   # Imprime la lista de frutas en minúsculas

# Imprimir las claves del diccionario
print(diccionario.keys())

# Imprimir los valores del diccionario
print(diccionario.values())
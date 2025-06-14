# Lectura y escritura de archivos de texto

Supongamos que necesitamos guardar información, que se mantenga aunque cerremos el programa. O que necesitamos escribir o modificar un documento `.txt` o de un tipo parecido. Bueno, podemos hacerlo con facilidad usando Python.

Para abrir y leer un archivo `.txt` o cualquier archivo de texto, utilizamos la función `open()` y haciendo uso de `with`:
```python
# Arbirmos el archivo llamado 'archivo.txt' que está en el mismo directorio que el main.py
# Lo abrimos en modo lectura, por eso escribimos 'r'
with open("archivo.txt", "r") as archivo:
    datos = archivo.read()
```
De esta forma, abrimos el archivo (que llamamos `archivo.txt`) y guardamos su contenido en la variable `datos`. Ahora, si queremos ver en pantalla el contenido del archivo bastará con usar `print()`.
```python
print(datos)
```
Esto nos los mostrará todo, y si queremos irlo leyendo línea por línea podemos hacerlo de la siguiente manera:
```python
with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip())  # .strip() quita el salto de línea
```
También podemos guardar cada línea en una lista:
```python
with open('archivo.txt', 'r') as archivo:
    lineas = archivo.readlines()
    # lineas será una lista con cada una de las líneas que contenga el archivo
```
Ahora bien, esto sirve para **leer** un archivo, pero, ¿y para escribirlo?

Para escribir un archivo se hace de manera parecido, pero lo abrimos en modo escritura:
```python
# Ahora lo abrimos en modo escritura 'w'
# De este modo se sobreescribe el archivo
with open('archivo.txt', 'w') as archivo:
    archivo.write("Primera\n")
    archivo.write("Segunda\n")
```
Al abrirlo con `w` lo estaremos sobrescribiendo. Por lo que borrará el contenido del archivo si ya existe. En caso que no exista, lo creará.

¿Y si queremos modificar un archivo? Podemos abrirlo en modo de adición `a`:
```python
# Ahora lo abrimos en modo adición 'a'
# De este modo escribiremos al final del archivo
with open('archivo.txt', 'a') as archivo:
    archivo.write("Esto está al final.")
```

Algo importante, especialmente si sabemos que el archivo puede contener carácteres no ingleses, es la decodificación. podemos especificar la codificación del archivo agregando el parámetro `encoding='utf-8'` si la codificación es UTF-8.
```python
with open("archivo.txt", "r", encoding='utf-8') as archivo:
    datos = archivo.read()
```

# Lectura y escritura de archivos binarios
De igual manera, podemos hacer las mísmas operaciones en archivos binarios reemplazando `r`, `w` y `a` por `rb`, `wb` y `ab`.

Por ejemplo:
```python
# Lectura
with open('archivo', 'rb') as archivo:
    contenido = archivo.read()

# Escritura (debemos escribirlo en bytes)
with open('archivo', 'wb') as archivo:
    datos = b'Hola mundo'  # la 'b' al principio lo convierte a bytes
    archivo.write(datos)

# Adición
with open('archivo', 'ab') as archivo:
    archivo.write(b'\nNueva línea en binario')
```

Todos funcionando de manera análoga a como lo hacen con un archivo de texto.

Esto puede resultar útil si el archivo es muy grande, pues nos permite leer o escribir en bloques:
```python
with open('archivo', 'rb') as archivo:
    while True:
        bloque = archivo.read(1024)  # Lee de 1024 en 1024 bytes
        if not bloque:
            break
        print(bloque)   # También podríamos guardarlo en una lista o similar en lugar de imprimierlo
```

Esto resulta particularmente útil si necesitamos guardar algún valor de una variable. Por ejemplo, un diccionario con la información del usuario o un modelo de IA entrenado. Esto se puede lograr haciendo uso de la librería `pickle`.
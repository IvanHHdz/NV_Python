# Comprensión de listas
La comprensión de listas es una técnica que nos permite crear una nueva lista a partir de otra de una manera sencilla. En pocas palabras, es una manera corta de trabajar con una lista que resulta equivalente a usar un bucle `for`.

Por ejemplo, supongamos que tenemos una lista de numeros enteros y queremos elevarlos al cuadrado. Podemos hacerlo con un bucle `for` de manera sencilla:
```python
numeros = [1, 2, 3, 4, 5]
resultado = []
for i in range(len(numeros)):
    resultados.append(numeros[i] ** 2)
```

El resultado será `[1, 4, 9, 16, 25]`.

Esto también lo podemos simplificar un poco por medio de una pequeña simplificación (a veces llamada _for each_):
```python
numeros = [1, 2, 3, 4, 5]
resultado = []
for n in numeros:
    resultados.append(n ** 2)
```
Esto hace que la variable `n`, la cual cambia en cada iteración, tome todos los valores de la lista `numeros`. El resulado es el mismo, pero es un poco más claro y simple.

Sin embargo, se puede simplificar aún más, usando las llamadas _list comprehensions_:
```python
numeros = [1, 2, 3, 4, 5]
resultado = [n ** 2 for n in numeros]
```

Como antes, esto hace exactamente lo mismo: dar una lista con el cuadrado de los numeros de la primera. La única diferencia es que de esta forma puede ser más sencilla de entender o escribir.


# Importaciones, módulos y paquetes

Como vimos anteriormente, las funciones resultan de mucha utilidad tanto para organizar nuestro código como para reutilizar partes de este. Pero, ¿y si el código crece mucho? No es buena idea utilizar un solo archivo para todo, pues se vuelve desorganizado y enredado.

Una solución a esto son los **módulos**. Imaginemos que tenemos muchas funciones que realizan operaciones, resuelven cosas de matemáticas por ejemplo, podemos sacarlas de nuestro archivo principal y llevarlas a otro en el cual tengamos únicamente funciones de ese estilo.

Pero, si las sacamos de nuestro archivo principal, ¿cómo las utilizamos? Para esto debemos de **importarlas** haciendo uso de `import`.

Por ejemplo, imaginemos que tenemos una carpeta llamada `programa` donde tenemos nuestro archivo principal, al que por convención llamamos `main.py`. Y creamos otro archivo llamado `funciones.py` en el cual ponemos todas las funciones (o parte de estas).

Aquí un ejemplo completo:

`main.py`
```python
import funciones    # Importamos funciones, haciendo que las funciones de funciones.py estén disponibles desde main.py

def main():         # Hacemos una función llamada main()
    print(funciones.cuadrado(5))    # Llamamos la función declarada en el archivo o módulo funciones.py
    # Para llamarla, primero debemos especificar desde dónde la llamamos, es decir, la llamamos a funciones

# Esta parte de aquí es una buena práctica que se hace para tener el código más ordenado 
# Sirve para ejecutar la función main() si se está ejecutando el archivo
if __name__ == "__main__":
    main()
```
`funciones.py`
```python
# Declaramos aquí la función, en el archivo funciones.py
def cuadrado(n):
    return n ** 2
```
Es importante que para esto ambos archivos deben de estar en la misma carpeta.

Ahora bien, ¿y si terminamos teniendo muchos módulos? Puede que nuestro programa crezca tanto que no solo tengamos ya muchas funciones, sino muchos módulos. En ese caso, lo mejor es meterlos en un **paquete**.

Un paquete es una carpeta con módulos, que al igual que un módulo sirve para ordenar funciones, un paquete sirve para ordenar módulos.

Por ejemplo, podemos meter el archivo `funciones.py` en una carpeta (el paquete) que llamaremos `modulos`. Esta debe incluir un archivo `__init__.py` (puede estar vacío).

En el archivo `main.py` esto quedaría como:
```python
import modulos.funciones    # Importamos funciones, haciendo que las funciones de modulos/funciones.py estén disponibles desde main.py

def main():
    print(modulos.funciones.cuadrado(6))  # Llamamos la función declarada en el archivo o módulo modulos/funciones.py
    # Para llamarla, primero debemos especificar desde dónde la llamamos, es decir, la llamamos a modulos.funciones

if __name__ == "__main__":
    main()
```

# Manejo de errores
Hasta este punto, hemos asumido que en todo nuestro programa no habrán **errores en ejecución**. ¿Qué quiere decir esto? Que el programa no fallará mientras se ejecuta.

Pero claro, en la vida real esto es algo que puede pasar, de hecho es común. Por ejemplo, analizemos el siguiente programa:
```python
edad = int(input("Ingrese su edad: "))
```

Esto es algo que ya habíamos hecho. ¿Qué podría fallar? Sencillo, el usuario podría **no** colocar su edad, sino colocar lo que sea. Ya sea por error o _"por ver qué pasa"_.

¿Qué pasará entonces si, por ejemplo, ingresa la palabra "edad"? Veamos:
```shell
Ingrese su edad: edad
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    edad = int(input("Ingrese su edad: "))
ValueError: invalid literal for int() with base 10: 'edad'
```

¿Qué nos quiere decir? Nos dice que no pudo convertir lo que ingresamos (`edad`) a un entero. Porque claro, no es posible convertir `edad` a un entero. El programa falla y se cierra por esto mismo.

Pero, lo ideal es que esto no ocurra, es decir, que el programa no se cierre por un error.

El problema es que, como mencionábamos, es muy probable que el programa falle, pues es muy probable que el usuario se le ocurra, por ejemplo, meter un dato que no es un número cuando se le solicita un número.

Para resolver esto, debemos que aprender a **manejar errores**. Para esto existen muchas formas, por ejemplo, el caso anterior se resuelve si simplemente verificamos que el usuario haya ingresado un número con el método `.isdigit()`:
```python
dato = input("Ingrese su edad: ")
if dato.isdigit():
    edad = int(dato)
else:
    print("No ha ingresado una edad.")
```
Esto nos asegura que al convertir lo ingresado a entero no tendremos errores. Esta forma es válida, y soluciona este problema. Sin embargo, es muy específica. ¿Y si el problema fuera otro?

Python (como la mayoría de los lenguajes) tiene una forma de manejar errores de manera general: los bloques `try-except`:
```python
try:
    edad = int(input("Introduce tu edad: "))
except ValueError:
    print("No ha introducido un valor válido.")
```

El primer bloque, el `try` consiste en la parte del código que sabemos que puede llegar a fallar, en este caso, convertir lo ingresado a entero.

Luego de ese, le sigue el bloque `except`. Este tiene el código que se ejecutará si algo falla.

Podemos especificar, como en este caso, el error que creemos que puede ocurrir: en este caso el `ValueError`. Esto es una buena práctica. Aunque igual podemos simplemente colocar:
```python
try:
    edad = int(input("Introduce tu edad: "))
except:
    print("No ha introducido un valor válido.")
```
Esto funcionará igual.

Ahora, ¿y si hay varios errores que se puedan dar? Podemos colocar tantos `except` como necesitemos:
```python
try:
    edad = int(input("Introduce tu edad: "))
    100 / edad  # Para ejemplificar, aunque no tenga mucho sentido
except ValueError:
    print("No ha introducido un valor válido.")
except ZeroDivisionError:
    print("Ha intentado hacer una division entre 0.")
```

En este caso, se mostrará en pantalla aquello correspondiente al error que haya ocurrido, si ocurrió uno.

También podemos agrupar los errores:
```python
try:
    edad = int(input("Introduce tu edad: "))
    100 / edad
except (ValueError, ZeroDivisionError):
    print("Ha ocurrido un error.")
```

Esto hará que diga `"Ha ocurrido un error."` si cualquiera de los dos errores se dá.

¿Y si no ocurre ninguno? Normalmente pasará a la siguiente línea después del último bloque `except` (hará eso mismo si hay un error), pero podemos especificar que haga algo usando un `else`:
```python
try:
    edad = int(input("Introduce tu edad: "))
    100 / edad
except (ValueError, ZeroDivisionError):
    print("Ha ocurrido un error.")
else:
    print("Todo salió bien.")
```

Al igual que colocar algo sea que haya un error o no con `finally`:
```python
try:
    edad = int(input("Introduce tu edad: "))
    100 / edad
except (ValueError, ZeroDivisionError):
    print("Ha ocurrido un error.")
else:
    print("Todo salió bien.")
finally:
    print("Continuamos...")
```
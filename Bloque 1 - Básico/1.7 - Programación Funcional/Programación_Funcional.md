# Funciones como objetos

Anteriormente, hemos explicado cómo crear y utilizar, de manera resumida:
```python
# Declaramos una función con un parámetro obligatorio (nombre), y un parámetro opcional (ciudad)
def bienvenida(nombre, ciudad='Tajo'):  # Si no ingresa una ciudad, se usará 'Tajo'
    # Se ejecuta este código
    print(f"Sea usted, estimado {nombre}, bienvenido a la ciudad de {ciudad}!")
    razon = input(f"Ingrese el porqué vino a la ciudad de {ciudad}\n")
    # Y se retorna 'razon'
    return razon
```
Esto es lo que hemos visto hasta el momento de lo que son las funciones. Sin embargo, son mucho más de lo que pueden parecer a simple vista. 

En la **Programación Funcional**, las funciones son tratadas como el centro o el elemento fundamental del código. Su objetivo es, en esencia, utilizar las funciones siguiendo el ideal matemático de que estas son (o deben ser) inmutables y deterministas (o puras).

Su objetivo es crear código más consiso y fácil de entender y testear.

Algunos de sus pilares consisten en la **inmutabilidad**, **determinismo**, y el buscar que cada función realize únicamente un trabajo específico. Busca combinar funciones mediante diversas técnicas para, igual que en matemáticas, crear funciones complejas a partir de funciones sencillas.

Para todo esto, a partir de ahora debemos entender que las funciones no solamente pueden ser llamadas, sino también manipuladas como objetos:

```python
# Declaramos una función que suma
def sumar(a, b):
    return a + b

# Declaramos una función que resta
def restar(a, b):
    return sumar(a, -b) # Esta función está hecha con otra función

# Declaramos una función que recive funciones y las ejecuta
def operar(a, b, operacion):
    return operacion(a, b)

def main():
    print(operar(30, 7, restar))    
    # Ejecutamos la función 'operar' que recive de parámetro la función 'restar' y la ejecuta, retornando un valor que recivirá la función 'print'

if __name__ == "__main__":
    main()
```

Esto incluso nos da la posibilidad de guardar las funciones dentro de estructuras de datos compuestos, como por ejemplo:
```python
# Declaramos las funciones que usaremos 
def sumar(a, b):
    return a + b

def restar(a, b):
    return sumar(a, -b)

def main():
    # Aquí guardamos las funciones en una lista
    lista = [sumar, restar]
    print(lista[0](20, 3))  # Y llamamos a una, a sumar(), pasándole los parámetros para ejecutarla

    # Aquí las guardamos en un diccionario
    diccionario = {
        "+" : sumar,
        "-" : restar
    }
    print(diccionario["-"](50, 9))  # Y de igual forma podemos utilizarlas
    # Esto resulta muy útil si queremos que el usuario ejecute comandos
    user = input("Ingrese la operación: ")
    print(diccionario[user](15, 2))

if __name__ == "__main__":
    main()
```

Aunque Python soporta programación funcional y puede usarse cómodamente con ese estilo, no es un lenguaje funcional puro. Existen lenguajes como Haskell, PureScript, Scala o Elm que están mejor adaptados al paradigma funcional. Incluso lenguajes como Rust, aunque no sean funcionales en esencia, incorporan muchas ideas del paradigma funcional.

# funciones `lambda`
También llamadas funciones anónimas, son aquellas que se definen en una sola línea usando la palabra reservada `lambda`. Su sintaxis es la siguiente:
```python
lambda argumento: expresion
```
Estas funciones las podemos guardar en variables, declarandolas como si estuvieramos creando una variable. Por ejemplo, el código del programa que habíamos hecho antes, puede reducirse a:
```python
sumar = lambda a, b: a + b
restar = lambda a, b: sumar(a, -b)
operar = lambda a, b, operacion: operacion(a, b)

def main():
    print(operar(30, 7, restar))

if __name__ == "__main__":
    main()
```

Esto nos ayuda a declarar de manera sencilla funciones sencillas. Lo que resulta muy útil si, por ejemplo, utilizamos funciones que reciben otras funciones como parámetros. Haciendo posible declararlas dentro de la llamada. En el ejemplo anterior:
```python
operar = lambda a, b, operacion: operacion(a, b)

def main():
    print(operar(30, 7, lambda a, b: a * b))
    # En pantalla se imprimirá '210'

if __name__ == "__main__":
    main()
```

Una pequeña limitación de esto, es que solamente podemos utilizar una expresión dentro de la función lambda. Así que no podremos crear una función lambda que haga dos cosas.

Las funciones lambda no ayudan también a ver de mejor manera que las funciones, al igual que cualquier otra variable, tienen un alcance que puede, o no, ser global. Ya que, por ejemplo, en este caso las tres funciones las declaramos con alcance global, pero también podemos declararlas dentro de ciertos bloques. Lo que nos lleva al siguiente tema.

# Funciones anidadas y clausuras
Esto consiste en la posibilidad de declarar funciones dentro de otras funciones. Por ejemplo, podemos tener:
```python
# Aquí declaramos una función que nos retornará un diccionario con funciones
def operaciones():
    # Estas funciones solo serán accesibles por medio del diccionario que nos retorne
    def sumar(a, b):
        return a + b
    
    def restar(a, b):
        return sumar(a, -b)

    return {
        "+" : sumar,
        "-" : restar
    }

def main():
    diccionario = operaciones()         # Aquí guardamos el diccionario con funciones
    print(diccionario["+"](12, 11))     # Podemos usarlas con normalidad por medio del diccionario

    # Sin embargo, no podemos usar las funciones sin el diccionario pues no existen fuera del diccionario
    # print(sumar(1,2))     # Esto dará error                

if __name__ == "__main__":
    main()
```

Y de igual forma que antes, esto lo podemos simplificar con las funciones lambda:
```python
def operaciones():
    sumar = lambda a, b: a + b
    restar = lambda a, b: sumar(a, -b)

    return {
        "+" : sumar,
        "-" : restar
    }

def main():
    diccionario = operaciones()
    print(diccionario["-"](50, 9))

if __name__ == "__main__":
    main()
```

O incluso, declararlas dentro del diccionario:
```python
def operaciones():
    return {
        "+" : lambda a, b: a + b,
        "-" : lambda a, b: sumar(a, -b)
    }

def main():
    diccionario = operaciones()
    print(diccionario["-"](50, 9))

if __name__ == "__main__":
    main()
```
Y así, se puede incluso simplificar más, pero la idea ya ha quedado clara.

En cuanto a la clausura, consiste en una función anidada que tiene la capacidad de "recordar" estados anteriores. Es decir, una vez llamada la función puede "recordar" las variables de otras llamadas. 

Aunque dicho en otras palabras, se puede entender como una función que retorna funciones siguiendo algo así como una plantilla. Ejemplo:
```python
# Creamos una función que puede retornar funciones 
def multiplicador(k):
    def mulp(x):
        return k * x
    return mulp

def main():
    # Llamamos a la función, y retorna funciones en base a la plantilla de antes
    doble = multiplicador(2)
    triple = multiplicador(3)

    print(doble(10))    # Retorna 20
    print(triple(3))    # Retorna 9

if __name__ == "__main__":
    main()
```

Claro que esta no es la única forma de utilizar la clausura, también podemos hacer que cree funciones con cierta "memoria" al hacer que contenga una referencia (como las listas):
```python
def contador():
    count = [0]

    def incrementar():
        count[0] += 1
        return count[0]
    
    return incrementar

c = contador()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

# Funciones de orden superior y `map()`, `filter()`

Antes hemos visto funciones que tienen la capacidad tanto de recibir otras funciones como parámetros como funciones que pueden retornar otras funciones. A este tipo de funciones se les suele llamar como **funciones de orden superior**. Existen 3 funciones especiales de orden superior que resultan muy útiles: `map()` y `filter()`.

`map()` recibe una función y un dato iterable (listas, tuplas, etc.). Lo que hace es aplicar la función a cada dato de la secuencia dada, retornando un dato que podemos convertir en una lista que contiene los datos que habíamos ingresado antes, pero después de aplicar la función. Por ejemplo:
```python
def doble(x):
    return 2 * x

def main():
    lista = [1, 2, 3, 4, 5]
    lista_doble = map(doble, lista)
    print(list(lista_doble))    # [2, 4, 6, 8, 10]

if __name__ == "__main__":
    main()
```

`filter()` de igual forma, aplica una función sobre todos los elementos de una lista u otro dato iterable. Con la diferencia que debe ser una función que retorne `True` o `False` y solamente incluirá los `True` en la salida. Ejemplo:
```python
def par(x):
    return x % 2 == 0

def main():
    lista = [1, 2, 3, 4, 5]
    lista_doble = filter(par, lista)
    print(list(lista_doble))    # [2, 4]

if __name__ == "__main__":
    main()
```

# Decoradores
Un decorador es una función que toma otra función como argumento, le añade funcionalidad y devuelve una nueva función. Se usa para modificar el comportamiento de funciones o métodos de manera clara, concisa y reutilizable, sin cambiar su código original.

La forma más común de utilizarlos es por medio de _azúcar sintáctico_. Este método consiste en crear una función que reciba otra como parámetro, crear una función que "decoraremos" y colocarle @ arriba junto con el nombre de la función que la decorará.

Por ejemplo:
```python
# definimos el decorador
def saludos(f):
    print("Hola!")
    f()
    print("Adios!")

# creamos la función y la decoramos
@saludos
def anuncio():
    print("Anuncio importante")

def main():
    anuncio()

if __name__ == '__main__':
    main()
```

Ahora bien, ¿Cómo lo hacemos si la función que deseamos decorar necesita parámetros? Esto es un poco más complejo al principio, vamos a analizarlo:
```python
def saludos(f):
    def g(*args, **kwargs):
        print("Hola!")
        f(*args, **kwargs)
        print("Adios!")
    return g

@saludos
def anuncio(texto):
    print("Anuncio importante")
    print(texto)

def main():
    anuncio("De lunes a viernes")

if __name__ == '__main__':
    main()
```

De la misma forma, también podemos agregar decoradores sobre decoradores, anidándolos:
```python
def bip(f):
    def g(*args, **kwargs):
        print("bip!!!")
        f(*args, **kwargs)
    return g

def saludos(f):
    def g(*args, **kwargs):
        print("Hola!")
        f(*args, **kwargs)
        print("Adios!")
    return g

@bip
@saludos
def anuncio(texto):
    print("Anuncio importante")
    print(texto)

def main():
    anuncio("De lunes a viernes")

if __name__ == '__main__':
    main()
```

Además, podemos crear decoradores que reciben parámetros. Para esto, necesitamos una función que retorne un decorador:
```python
def bips(n):
    def bip(f):
        def g(*args, **kwargs):
            for i in range(n):
                print("bip!!!")
            f(*args, **kwargs)
        return g
    return bip

def saludos(f):
    def g(*args, **kwargs):
        print("Hola!")
        f(*args, **kwargs)
        print("Adios!")
    return g

@bips(3)
@saludos
def anuncio(texto):
    print("Anuncio importante")
    print(texto)

def main():
    anuncio("De lunes a viernes")

if __name__ == '__main__':
    main()
```

Python también cuenta con un par de decoradores que resultan útiles. De estos, podemos destacar:
| Decorador       | Uso                                      | Se aplica a...         |
| --------------- | ---------------------------------------- | ---------------------- |
| `@staticmethod` | Método sin `self`, no accede a instancia | Métodos de clase       |
| `@classmethod`  | Método con `cls`, accede a la clase      | Métodos de clase       |
| `@property`     | Define un atributo computado             | Atributos de instancia |
| `@wraps`        | Preserva metadatos al decorar funciones  | Decoradores            |


# Inmutabilidad y pureza
# Composición
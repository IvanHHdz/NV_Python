# NumPy
NumPy (_Numerical Python_) es una librería fundamental en la computación numérica y científica. Proporciona estructuras de datos, funciones y herramientas eficientes para trabajar con arrays y matrices multidimensionales, así como una amplia colección de funciones matemáticas de alto rendimiento.

Para instalarla: 
```shell
pip install numpy       # con pip
conda install numpy     # con conda
```

Y la forma estándar para importarla es siguiendo la convención:
```python
import numpy as np
```

# Arreglos 
Es una estructura similar a la lista, pero más eficiente. Funciona de manera similar a los arreglos de otros lenguajes como C++. Y se les conoce como tipo `ndarray`.

Podemos entender los arreglos de manera similar a las matrices de matemáticas: varios números (o datos) agrupados. De esta forma, si tenemos:
```
[1  2  3]
```
podemos representarlo en Python, usando NumPy, como:
```python
a = np.array([1, 2, 3])
```

Y lo mismo ocurre con matrices como:
```
[1  0  0]
[0  1  0]
[0  0  1]
```

que podemos representar como:
```python
b = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
```

Y de manera análoga a las listas, podemos acceder a sus elementos de la siguiente forma:
```python
print(a[0])     # imprimirá 1
```

Y al igual que las listas, los arreglos también son mutables:
```python
a[0] = 7
print(a[0])     # imprimirá 7
```
Y podemos acceder a ellos por _slicing_:
```python
c = np.array([0, 10, 20, 30, 40, 50])
print(c[1:4])  # Elementos desde el índice 1 al 3
```

Consideremos ahora el arreglo:
```python
arr = np.arange(0, 11, 1)
print(arr)  # [ 0  1  2  3  4  5  6  7  8  9 10]
```

Como habíamos dicho anteriormente, podemos acceder a los elementos del arreglo de la misma forma en que accedíamos a los elementos de una lista:
```python
print(arr[4])   # 4
print(arr[3:6]) # [3, 4, 5]
```
Esto funciona exactamente igual que cuando trabajamos con listas. Sin embargo, los arreglos de NumPy tienen formas especiales para acceder a los elementos:
```python
# establecer  una condición
print(arr[arr > 7]) # [8, 9, 10]

# establecer  dos condiciones
print(arr[(arr % 2 == 0) | (arr % 3 == 0)]) # [ 0  2  3  4  6  8  9 10]
```

De la misma forma, podemos crear arreglos booleanos a partir de un arreglo:
```python
b = (arr > 1) & (arr % 2 == 0)

print(b)    # [False False  True False  True False  True False  True False  True]
```

Una pequeña diferencia importante es el hecho que acceder a los elementos de esta forma no hace una copia, sino una referencia. Lo que ocasiona que si modificamos los datos en la variable que creamos, se modifican así mismo en el arreglo original:
```python
temp = c[1:4]   
print(temp)     # imprime [10, 20, 30]
temp[1] = 23    # cambiamos el valor de 20 a 23
print(temp)     # imprime [10, 23, 30]
print(c)        # imprime [0, 10, 23, 30, 40, 50]
```

Para evitar esto, debemos hacer copias de los arreglos con `.copy()`:
```python
temp = c[1:4].copy()  
print(temp)             # imprime [10, 20, 30]
temp[1] = 23            # cambiamos el valor de 20 a 23
print(temp)             # imprime [10, 23, 30]
print(c)                # imprime [0, 10, 20, 30, 40, 50]
```

Y ahora, si tenemos una matriz, podemos acceder a cada elemento de la siguiente forma:
```python
d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(d)        # imprime la matriz completa
print(d[2,1])   # accedemos a la posición (2, 1), es decir, el 8 
# fila 2, columna 1
# contando desde 0
```

Lo mismo se extiende a mayores dimensiones (tensores):
```python
f = np.array([
    [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
    ],
    [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ],
])

print(f)        # imprime la matriz completa
print(f[1, 2, 0])   # accedemos a la posición (1, 2, 0), es decir, el 7 
```

# Funciones básicas

Ahora, algunas funciones básicas:
- `np.zeros()` crea arreglos llenos de ceros.
```python
t = np.zeros(3)
print(t)    # [0. 0. 0.]

t = np.zeros((3,3))
print(t)    # [[0. 0. 0.]
            #   [0. 0. 0.]
            #   [0. 0. 0.]]
```

- `np.ones()` funciona igual, pero con 1.
```python
t = np.ones(3)
print(t)    # [1. 1. 1.]

t = np.ones((3,3))
print(t)    # [[1. 1. 1.]
            #   [1. 1. 1.]
            #   [1. 1. 1.]]
```

- `np.empty()` lo mismo, pero los crea "vacíos". 
```python
t = np.empty(2) 
print(t)        # [7.06673073e-96 6.96320200e-77]
# Estos datos son aleatorios
# Datos basura, como al crear una variable y no inicializarla en lenguajes como C++
```

La ventaja de usar `np.empty()` es que resulta más rápido que `np.zeros()` y que `np.ones()`.

- `np.arange()` que funciona similar a `range()`
```python
t = np.arange(1, 5.5, .5)   # inicio, fin, intervalo
print(t)    # [1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.]
```

Como en `range()`, solo el final es obligatorio. La ventaja que tiene, es que pueden usarse valores no enteros.

- `np.linspace()` sirve para partir un intervalo en cierta cantidad de datos:
```python
t = np.linspace(0, 23, num=6)   # inicio, fin, cantidad
print(t)    # [ 0.   4.6  9.2 13.8 18.4 23. ]
```

Lo que obtenemos es un arreglo que va desde el inicio al fin teniendo cierta cantidad de elementos, separados de manera uniforme.

# Atributos de los arreglos

Para esta sección, consideraremos los siguientes arreglos:
```python
a = np.array([1, 2, 3])
b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
c = np.array([
    [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
    ],
    [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ],
])
```

Ahora bien, existe mucha información que podríamos necesitar de un arreglo, como su forma, sus dimensiones, etc.

El número de dimensiones de un arreglo lo podemos obtener por medio de `.ndim`:

```python
print(f"primer arreglo (vector): {a.ndim}")     # imprime 1
print(f"segundo arreglo (matriz): {b.ndim}")    # imprime 2
print(f"tercer arreglo (tensor): {c.ndim}")     # imprime 3
```

Al igual que la forma que tiene el arreglo, que es una tupla que especifica los elementos en cada dimensión. Esto lo obtenemos con `.shape`:

```python
print(f"primer arreglo (vector): {a.shape}")     # imprime (3, )
print(f"segundo arreglo (matriz): {b.shape}")    # imprime (3, 3)
print(f"tercer arreglo (tensor): {c.shape}")     # imprime (2, 3, 3)
```

Notemos que el tamaño de esta tupla es igual a las dimensiones:
```python
len(c.shape) == c.ndim   # True
```

Y para saber el número total de elementos de un arreglo, podemos usar `.size`:
```python
print(b.size)   # tiene 9 elementos
```

# Operaciones básicas con arreglos
Bueno, una vez que tenemos los arreglos, vamos a querer trabajar con ellos. Consideremos primero los siguientes arrelgos:
```python
a = np.array([1, 2, 3])
b = np.ones(3)
```

Podemos **sumar** arreglos con el signo de suma `+`:
```python
d = a + b
print(d)
# [2. 3. 4.]
```
Lo mismo aplica a la **resta**, **división** y **multiplicación**:
```python
e = a - b
print(e)    # [0. 1. 2.]

f = b / a
print(f)    # [1.         0.5        0.33333333]

g = a * a
print(g)    # [1 4 9]
```

Y también podemos sumar los valores del propio arreglo, es decir, sumar todos los elementos dentro de un arreglo:
```python
h = a.sum()
print(h)    # 6
```

Además de poder crear arreglos de las sumas de partes de arreglos de dimensiones superiores:
```python
# consideremos el arreglo:
arr = np.array([[1, 1], [2, 2]])

# podemos sumar sus columnas
col = arr.sum(axis=0)
print(col)  # [3 3]

# o sus filas:
fil = arr.sum(axis=1)
print(fil)  # [2 4]
```

Y claro, está también la multiplicación por escalares:
```python
r = a * 7
print(r)    # [ 7 14 21]
```



# Funciones y métodos útiles

Consideremos que tenemos los arreglos:

```python
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])
```

Pero, nosotros nos gustaría, por la razón que sea, colocar uno sobre otro, por así decirlo. O colocarlos a la par. ¿Cómo lo hacemos? Usando `np.vstack()` y `np.hstack()` de la siguiente forma:
```python
vertical = np.vstack((a1, a2))
horizontal = np.hstack((a1, a2))

print(vertical)
#   [[1 1]
#    [2 2]
#    [3 3]
#    [4 4]]

print(horizontal)
#   [[1 1 3 3]
#    [2 2 4 4]]
```

Lo anterior también podemos lograrlo por medio de `np.concatenate()` de la siguiente forma:
```python
concatenacion1 = np.concatenate((a1, a2), axis=0)
print(concatenacion1)
#   [[1 1]
#    [2 2]
#    [3 3]
#    [4 4]]

concatenacion2 = np.concatenate((a1, a2), axis=1)
print(concatenacion2)
# [[1 1 3 3]
#  [2 2 4 4]]
```

las diferencias entre hacerlo de una forma u otra son principalmente conveniencia (ya que la primera forma es más sencilla al no tener que especificar el eje), la flexibilidad (ya que `np.concatenate()` funciona bien en muchas dimensiones y brinda control en el eje) y el hecho que la primera opción permite ser usada aunque no coincida completamente la forma.

Ahora, tocando el tema de la forma. Como vimos anteriormente, podemos ver la forma de un arreglo por medio de `.shape`:
```python
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr1.shape)   # (8,)
```

Ahora, una pregunta importante: ¿Podemos cambiar la forma de un arreglo? Sí, podemos hacerlo por medio de `.reshape()`:
```python
arr2 = arr1.reshape(4, 2)
print(arr2.shape)   # (4, 2)
print(arr2)
#   [[1 2]
#    [3 4]
#    [5 6]
#    [7 8]]
```
Podemos reformar un arreglo a cualquier forma que sea compatible. ¿Cómo sabemos cuándo una forma es compatible? Simple, al multiplicar sus valores deben de ser igual al número de sus elementos:
- $8 = 8$
- $4 \times 2 = 8$
- $2 \times 2 \times 2 = 8$
- etc.
```python
arr3 = arr2.reshape(2, 2, 2)    # Notemos que decidimos usar arr2, para mostrar que funciona con arreglos de cualquier forma también
print(arr3.shape) # (2, 2, 2)
print(arr3)
#   [[[1 2]
#     [3 4]]
#
#    [[5 6]
#     [7 8]]]
```

Otras funciones que pueden resultar útiles y que posee NumPy son funciones matemáticas y estadísticas. 

Entre las funciones matemáticas tenemos algunas que pueden resultar especialmente útiles por su velocidad al aplicarse sobre un arrglo para, por ejemplo, obetener valores para graficarlas. 

Ejemplo: Imaginemos que deseamos graficar los valores de seno, y utilizaremos los valores desde $0$ hasta $2 \pi$ en intervalos de $0.01$. Para lograrlo, lo primero que debemos hacer es obtener dos arreglos con los números. Esto lo haremos ahora, más adelante aprenderemos cómo graficarlas.
```python
x = np.arange(0, 2 * np.pi, 0.01)
y = np.sin(x)
```
De esta forma, obtenemos de manera sencilla (y eficiente) los valores de $x$ y $y$ para graficar $y = \sin(x)$. Como mencionamos antes, próximamente veremos cómo graficarlas.

Además de `np.sin()` y `np.cos()`, existen muchas más funciones matemáticas. Podemos encontrar más información en la documentación oficial de NumPy, disponible en el [siguiente enlace](https://numpy.org/doc/stable/reference/routines.math.html).

De la misma forma, podemos utilizar la sub-librería `np.random` con la que podemos:
```python
print(np.random.rand())                     # obtener número aleatorio entre 0 y 1
print(np.random.rand(2, 2))                 # obtener un arreglo (2, 2) con números aleatorios entre 0 y 1
print(np.random.randint(0, 101, size=5))    # arreglo de 5 elementos con números de 0 a 100

arr = np.array([1, 2, 3, 4, 5])

np.random.shuffle(arr)                      # mezcla el arreglo aleatoriamente
print(arr)

print(np.random.choice(arr))                # toma una muestra al azar

np.random.seed(1)                           
# configura una semilla, a partir de esta línea siempre se obtendrá el mismo resultado con la semilla 1

print(np.random.normal(0, 1, 10))           
# genera un arreglo de 10 números aleatorios que siguen la distribución normal (gaussiana) con media en 0 y desviación en 1
```

Al igual que algunas funciones útiles, como mencionábamos, para estadística y análisis (lo que nos compete aquí):
```python
a = np.array([1, 2, 3, 4])
print(a.mean())   # 2.5
print(a.std())    # 1.118...
print(a.max())    # 4
print(a.min())    # 1
print(a.argmin()) # 0
print(a.argmax()) # 3
```

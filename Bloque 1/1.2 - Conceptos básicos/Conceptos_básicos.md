# Tipos de datos primitivos (`int`, `float`, `str`, `bool`)

Al comenzar a programar, lo primero que veremos son los tipos de datos primitivos en Python. Estos son la forma en que se clasifican los datos según lo que representan y lo que se puede hacer con ellos. Los tipos de datos primitivos son los más básicos y esenciales de un lenguaje de programación.

Python usa 4 tipos de datos primitivos principales:
- `int` para números enteros, ya sean positivos o negativos. Ejemplo: `-1`.
- `float` para números decimales (números con parte fraccionaria). Ejemplo: `3.14`.
- `str` para cadenas de texto. Estas se escriben entre comillas (como hicimos en el ejercicio de `"Hola mundo!"`), ya sean dobles (`"str"`) o sencillas (`'str'`) para indicarle a Python que es una cadena de texto. 
- `bool` para valores booleanos (`True` y `False`).

Cada tipo de dato tiene sus propias operaciones que veremos más adelante.

# Variables y constantes

En un programa se suelen usar muchos datos, algunos son datos primitivos, otros compuestos, etc. En la mayoría de casos usaremos el mismo dato muchas veces o no conoceremos su valor al momento de escribir el código. ¿Cómo manejamos eso? Para eso existen las variables.

Las variables son espacios de la memoria a los que le asignamos un dato e identificamos con un nombre. De esta forma, cuando querramos usar un dato, lo podemos poner en la variable y usarlo con el nombre que le dimos.

Funcionan como pequeñas cajas que pueden almacenar valores para usarlos cuando y como queramos.

Para declarar una variable, colocamos el nombre que usaremos y le asignamos un valor:

```python
x = 1
s = "Hola"
b = True
y = 0.5
```

En este ejemplo, la variable `x` es de tipo `int`, ya que `1` es un número entero. `s` es de tipo `str`, ya que es un texto. `b` es de tipo `bool` ya que su valor es `True` y `y` es un `float` pues es un número decimal.

En Python (a diferencia de otros lenguajes) no es necesario especificar qué tipo es cada variable: Python lo detecta automáticamente según el valor asignado.

Podemos nombrar a las variables con los nombres que queramos, siempre y cuando cumplamos con las reglas comunes de nombres de variables:
- Solo puede tener letras (mayúsculas o minúsculas) el alfabeto inglés, número y guión bajo.
- No puede empezar con un número.
- No puede tener espacios.
- No puede usar otros carácteres.
- No puede usar palabras reservadas.
- Se distinga entre mayúsculas y minúsculas.

Siempre se recomienda, como una buena práctica utilizar nombres descriptivos para entender mejor lo que es cada variable.

En cuanto a las constantes, Python no tiene. Aún así, se suele usa la convención que las variables escritas en mayúsculas son constantes. Aún así, python no prohíbe que cambien como en otros lenguajes:
```python
PI = 3.1415926
```

# Comentarios
Los comentarios son partes del código que el intérprete de Python ignorará y no ejecutará. Sirven principalmente para explicar lo que hace el código o dejar notas con cualquier propósito. Es bastante recomendable ir añadiendo comentarios para explicar el código, ya sea por si compartimos el código y alguien más tiene que leerlo o si nosotros mismos podemos llegar a querer volver a entender nuestro propio código. 

Los comentarios se crean usando el `#`:
```python
# Esto es un comentario de una línea
x = 5  # Esto también es un comentario
```

También existen las llamadas _docstring_ que se hacen usando 3 comillas (`""" """`) y ayudan a escribir varias líneas:
```python
'''
Esta
es 
una
docstring
'''
```

Estas últimas suelen usarse para documentar funciones.

# Operadores (Aritméticos, de Comparación y lógicos)

Como mencionamos antes, cada tipo de dato tiene distintas operaciones en las que se pueden usar. Estas operaciones se llevan a cabo con los operadores lógicos.

Los datos numéricos `int` y `float` tienen ambos las operaciones de suma `+`, resta `-`, multiplicación `*`, división `/`, módulo `%` y división entera `//` (aclarando que módulo es el residuo de una división y la división entera es el cociente sin decimales).

A continuación un ejemplo, donde usaremos `print()` para ver el resultado de la operación (los `#` son para comentarios, partes de código que se ignoran al ejecutar el programa):
```python
a = 10
b = 5
print(a + b)    # Mostrará 15
print(a - b)    # Mostrará 5
print(a * b)    # Mostrará 50
print(a / b)    # Mostrará 2
print(a % b)    # Mostrará 0
print(a / b)    # Mostrará 2
```

Lo anterior funciona igual si son `float` o si uno es `float` y el otro es `int`:
```python
c = 20
d = 3.5
print(d + d)    # Mostrará 7
print(d - c)    # Mostrará -16.5
print(c * d)    # Mostrará 70.0
print(c / d)    # Mostrará 5.714285714285714
print(c % d)    # Mostrará 2.5
print(c // d)   # Mostrará 5.0
```

Notemos que al multiplicar `c * d` el resultado tiene `.0`. Esto para indicar que es un `float`, pues al operar un `float` con un `int` el resultado siempre es `float`. Esto ocurre tanto en la división como en la multiplicación.

Podemos usar los paréntesis `()` para agruparlos.

Con los datos `str`, podemos usar la concatenación `+` y la repetición `*`.

La concatenación es unir dos cadenas de texto, y la repetición es repetirlas.
```python
a = "Hola "
b = "mundo!"
print(a + b)    # Mostrará "Hola mundo!"
print(a * 3)    # Mostrará "Hola Hola Hola "
```

También se pueden usar estos operadores a la hora de asignar, simplificando algunas cosas:
```python
v = 2
v += 3   # Ahora v vale 5
v -= 1   # Ahora v vale 4
v *= 10  # Ahora v vale 40
v /= 2   # Ahora v vale 20
```

Ahora bien, supongamos que tengo dos variables: ¿Cómo puedo saber si ambas son iguales? Esto se hace por medio de operadores de compración. Estos son: 
- `==` igual.
- `!=` no igual.
- `<=` menor o igual.
- `>=` mayor o igual.
- `>` mayor.
- `<` menor.

Estos devuelven el valor booleano (verdadero o falso) de la comparación.

```python
a = 1
b = 0

a == b  # False
a != b  # True
a <= b  # False
a >= b  # True 
a < b   # False
a > b   # True 
```

Pero, ¿y si tengo tres variables y quiero saber si una es mayor a una o menor que otra? Esto se logra por medio de operadores lógicos: `and`, `or` y `not`.
- `and` es el operador lógico _y_.
- `or` es el operador lógico _o_.
- `not` es el operador lógico _no_.

Podemos usar los paréntesis `()` para agruparlos, al igual que los operadores aritméticos:

```python
a = 1
b = 0
c = -1

a >= b and a != c   # True
b > c or b == a     # True
not (a == b)        # True
```

# Funciones básicas

Como mencionabamos al principio con `print()`, esta es una función. Las funciones son bloques de código a los que les damos un nombre y podemos reutilizar para realizar una tarea. Como mencionamos, suelen tener parámetros que se colocan entre los paréntesis (no todas necesitan parámetros).

La función `print()` es la primera que utilizamos, pero existen muchas más. Incluso aprenderemos a hacer nuestras propias funciones pronto.

`print()` muestra en pantalla lo que le pasamos como parámetro (ya sea texto o variables):

```python
print("Hola mundo")
```

`input()` pide datos al usuario:

```python
nombre = input("Tu nombre es: ")
```

`len()` mide la longitud (número de elementos):

```python
lista = [1, 2, 3]
len(lista)  # 3
```

`type()` nos dice el tipo de dato:

```python
dato = 3.1415926

type(dato)  # <class 'float'>
```

`int()`, `float()`, `str()` convierte datos a otros tipos (siempre que la conversión sea válida):

```python
int("5")     # 5
float("3.2") # 3.2
str(8)       # "8"
```   

`sum()`, `max()`, `min()` operaciones sobre listas:

```python
numeros = [1, 2, 3]
sum(numeros)   # 6
max(numeros)   # 3
min(numeros)   # 1
```
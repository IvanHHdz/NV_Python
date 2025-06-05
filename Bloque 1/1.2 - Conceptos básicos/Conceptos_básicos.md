# Tipos de datos primitivos (`int`, `float`, `str`, `bool`)

Al comenzar a programar, lo primero que veremos son los tipos de datos primitivos en Python. Estos son la forma en que se clasifican los datos según lo que representan y lo que se puede hacer con ellos. Los tipos de datos primitivos son los más básicos y esenciales de un lenguaje de programación.

Python usa 4 tipos de datos primitivos principales:
- `int` para números enteros, ya sean positivos o negativos. Ejemplo: `-1`.
- `float` para números decimales (números con parte fraccionaria). Ejemplo: `3.14`.
- `str` para cadenas de texto. Estas se escriben entre comillas (como hicimos en el ejercicio de `"Hola mundo!"`), ya sean dobles (`"str"`) o sencillas (`'str'`) para indicarle a Python que es una cadena de texto. 
- `bool` para valores booleanos (`True` y `False`).

Cada tipo de dato tiene sus propias operaciones que veremos más adelante.

# Variables

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

# Tipos de datos compuestos (`dict`, `list`, `tuple`, `set`)

Además de los tipos de datos que ya vimos, también existen otros datos denominados datos compuestos, porque pueden estar hechos de otros datos primitivos (o compuestos).

El más simple de estos es la tupla, el cual son valores que funcionan como pares ordenados (pueden tener uno o más elementos). Las tuplas son útiles para almacenar varias variables en una sola.

Puden tener elementos de cualquier tipo, incluido también otras tuplas o estar vacios. Las tuplas son inmutables, por lo que una vez declarada no puede cambiarse su valor.

Las tuplas se declaran con los paréntesis `()`.

```python
a = (1, 2, 3)
b = (1.2, 3.14)
c = ('Hola', 'Mundo')
d = (True, False)
e = ((1,2), (2.1, 2.2))
f = ('Normal', 222, (0, 0))
g = ()

c[0]  # Se accede al valor de la posición 0 de la tupla
```

Como dijimos antes, las tuplas no pueden cambiar una vez las creamos. Pero, ¿y si queremos que cambien? A veces es necesario, por eso existen las listas.

Las listas funcionan como las tuplas, agrupan varias variables en una sola, con la diferencia que estas **sí** son mutables y por ende pueden cambiar en cualquier momento que queramos.

También poseen ciertos comandos, llamados _métodos_, con los que podemos trabajar sobre las listas. Los más importantes son `.append()`, `.pop()`, `.index()`, `.remove()`, `.insert()` y `.sort()`. 

Las listas se declaran con los corchetes `[]`.
```python
a = [-1, 0 ,1]
b = [2.16, 1.12]
c = ['Hello', 'World']


print(c)       # ['Hello', 'World']

c[0]           # Accedo a un valor de la lista

c[0] = 'Bye'   # Cambio un valor de la lista

print(c)       # ['Bye', 'World']

c.append('!')  # Agrego un nuevo elemento al final de la lista

print(c)       # ['Bye', 'World', '!']

c.pop()        # Elimino el último elemento de la lista

print(c)       # ['Bye', 'World']
```

También existen los conjuntos, que funcionan de manera similar a las listas, con la excepción que no se pueden repetir los elementos. Los conjuntos tienen la particularidad de que su orden no importa, es decir: `{1, 2}` es lo mismo que `{2, 1}`. Al igual que los otros tipos anteriores, pueden tener elementos de cualquier tipo. Además de tener sus propios métodos.

Los conjuntos se declaran con las llaves `{}`.

```python
a = {0, 1, 2, 3}
b = {'1', 2, 3.14}

a.add(4)    # Agrega un nuevo elemento

a.remove(0) # Elimina un elemento

print(5 in a)  # Da True si está en el set, False si no
```

Como dato curioso, los conjuntos también tienen sus propias operaciones, las _operaciones de conjuntos_, que son precisamente las operaciones de conjuntos matemáticos: unión ($A \cup B$), intersección ($A \cap B$), diferencia ($A - B$) y diferencia simétrica ($(A \cup B) \land \neg(A \cap B)$).
```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Unión: {1, 2, 3, 4, 5}
print(a & b)   # Intersección: {3}
print(a - b)   # Diferencia: {1, 2}
print(a ^ b)   # Diferencia simétrica: {1, 2, 4, 5}
```

Por último, tenemos a los diccionarios, los cuales funcionan como una correspondencias de pares de _clave-valor_. Es decir, con cada clave puedo acceder a un valor.

```python
a = {
   "clave"  : "valor",
   "clave2" : "valor",
}

a["clave"]  # Accedemos al valor asociado a clave, en este caso "valor"
```

Es decir, funcionan como una lista, pero en lugar de usar los índices uso una clave. La clave puede ser de cualquier tipo de valor inmutable que ya hemos visto (`int`, `float`, `str`, `bool`, `tuple`), aunque lo más recomendable es usar valores `str` o `int`. La clave, en cambio, puede ser de cualquier tipo.

Una vez creado un diccionario, es posible editar sus valores, agregar nuevos o eliminarlos.

```python
d = {
   "Lenguaje"  : "Python",
   "Version"   : "3.10",
   "Entorno"   : ".venv",
}

print(d['Entorno'])     # Accedemos al valor asociado a "Entorno", que es ".venv"
d['Entorno'] = ".conda" # Cambiamos el valor a ".conda"
print(d['Entorno'])     # Ahora cuando accedemos al valor asociado a "Entorno", es ".conda"

d["IDE"] = "VS Code" # Agregamos un nuevo valor al diccionario

del d["Entorno"]     # Eliminamos el valor del diccionario
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
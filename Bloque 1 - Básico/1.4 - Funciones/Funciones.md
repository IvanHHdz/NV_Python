# Definición de funciones

Las funciones, como mencionabamos en temas anteriores, _son bloques de código a los que les damos un nombre y podemos reutilizar para realizar una tarea_. Como mencionabamos al principio, la primera que aprendemos a utilizar es la función `print()`, aunque claro, exiten muchas otras más. 

Y como mencionabamos anteriormente, no solo existen muchas, sino que incluso nosotros podemos crear nuestras propias funciones para realizar procesos que necesitemos.

Crear, definir o declarar una función, se logra haciendo uso de la palabra reservada `def`.

`def` nos sirve para poder declarar una función. Para ello necesitamos darle un nombre, colocar los parámetros que necesita, el código y el valor que retornará (si retorna algún valor). A diferencia de otros lenguajes de programación (como C++, Java o Rust) no es necesario especificar de qué tipo es cada dato, incluso, podemos hacer que una función reciba como parámetro datos de distinto tipo o que retorne de más de un tipo.

La sintaxis básica para declarar una función es:
```python
def funcion(parametro):
    # Codigo
    return retorno
```
Para entender mejor esto, vamos con un ejemplo, una función que salude al usuario por su nombre:
```python
def saludar(nombre):
    print("Hola " + nombre + "!")
# Notemos que para incluir el nombre del usuario, concatenamos el nombre con el resto de la cadena de texto
```

# Funciones, parámetros y retorno

Las funciones suelen ser bastante útiles tanto para mantener el código más ordenado como para reutilizar partes del mismo. 

Para mostrar su utilidad, vamos a analizar un programa que nos ayude a calcular las soluciones de una ecuación cuadrática:

Comenzamos declarando la función que resuelve la ecuación cuadrática $x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

```python
def cuadratica(a, b, c):    # Los parámetros que colocamos aquí (a, b, c) serán datos que nos envíen desde donde llamen a la función, siempre que la llamen
    d = b ** 2 - 4 * a * c  # Calculamos el discriminante
    if d < 0:               # Verificamos si el discriminante es negativo
        return None         # Si es negativo entonces no tiene soluciones reales, no podemos seguir
    else:                   # Si no es negativo, entonces continuamos
        # Calculamos ambas soluciones
        x_1 = (- b + d ** 0.5) / (2 * a)
        x_2 = (- b - d ** 0.5) / (2 * a)
        return (x_1, x_2)   # Retornamos las soluciones en una tupla
        # Al retornar un valor, lo que hacemos en enviarlo donde llamamos la función
```

Y ahora la utilizamos:
```python
# Solicitamos al usuario que ingrese los coeficientes, y los convertimos a números decimales
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

# Calculamos las soluciones llamando a la función y pasando los valores de los parámetros, y guardamos las soluciones en una variable que llamamos 'resultado'
# Al colocar los parámetros de una función, debemos asegurarnos que los coloquemos en el orden correcto
# Sin embargo, no es necesario que tengan los mismos nombres que los que usamos en la función
resultado = cuadratica(a, b, c)
# Como habíamos dicho, al retornar un valor lo enviamos a donde llamaron la función, lo que significa que una vez que llamemos la función, esta nos dará un resultado que almacenaremos en la variable 'resultado'
if resultado is None:   # Verificamos si nos tenía soluciones reales
    print("La ecuación no tiene soluciones reales.")
else:
    # Si tenía soluciones reales, las mostramos
    print(f"Las soluciones son: {resultado[0]} y {resultado[1]}")
    # Aquí utilizamos lo que es llamado como cadena de texto formateada, que sirve para colocar variables dentro de la cadena de texto.
    # Esto se hace colocando una 'f' antes de abrir las comillas y colocando las variables entre llaves {}
```

Ahora bien, uno puede preguntarse ¿Y para qué crear una función que hace eso si puedo simplemente colocar el código y listo? Pues bien, además de verse más ordenado, ayuda a poder **reutilizar** el código.

Por ejemplo, supogamos que después necesitamos volver a calcular las soluciones de una ecuación cuadrática, al usar funciones solamente tenemos que escribir `cuadratica()` y pasarle los parámetros que necesita, sin necesidad de volver a programar esa parte.

También podemos hacer que un parámetro sea opcional al declararle un valor en la declaración de la función. Por ejemplo:
```python
def saludar(nombre = 'Fulano de Tal'):
    print('Hola ' + nombre + '!')
```
De esta forma, si no se pasa un nombre de parámetro, se usará el nombre que definimos aquí. Entonces, podemos hacer lo siguiente:
```python
saludar()
```
y  el resultado sería:
```txt
Hola Fulano de Tal!
```

Y en caso que existan muchos parámetros, entre ellos muchos que no son obligatorios, podemos especificar cuales de ellos vamos a pasar al llamar la función. Por ejemplo:
```python
saludar(nombre = "Pablo")
```
Así, si la función tuviera más parámetros, especificaríamos que estamos pasando el que irá en la variable `nombre`.

# Alcance de variables

Como mencionábamos antes, no tiene importancia si el nombre de las variables que pasamos como parámetros son los mismos que utilizamos en la declaración de la función. Pero, ¿Por qué? Porque lo único que se transmite entre la llamada a la función y la función es el valor, no la variable completa. 

Las funciones y el resto del programa funcionan, por así decirlo, en lugares distintos. Esto quiere decir que las variables que se declaran en una función se quedan en esa función y lo único que comunica una función con otra o con otras partes del programa son los parámetros que entran y el retorno que sale.

Esto también implica que una variable declarada dentro de una función se quede únicamente en esa función. Así, por ejemplo, la variable `d` del determinante que declaramos dentro de la función **no existe fuera de la función**. Funcionando igual para cualquier variable declarada dentro de una función. 

Ahora bien, existen ciertas variables que podríamos necesitar usar en muchas partes del programa (por ejemplo, el valor de pi, o el nombre del usuario, etc.). Para poderlas usar en muchas partes del programa las declaramos como _variables globales_. Esto se verá mejor más adelante, pero para irlo aclarando desde ahora: una variable global es una variable que puede usarse desde cualquier parte del programa.

Para declararlas, solamente debemos declararlas desde una parte del programa que esté fuera de cualquier función. Para acceder a ellas simplemente usarlas como cualquier otra variable **excepto** que las queramos modificar, en cuyo caso debemos colocar la palabra reservada `global` antes de la variable "declarandola" por así decirlo:
```python
global nombre_del_usuario
```
En este ejemplo decimos que vamos a usar (o modificar) la variable global `nombre_del_usuario`.

# Recursividad

La recursividad es una técnica consiste en que una función se llama a si misma varias veces. Se usa para dividir un problema grande en problemas más pequeños y más fáciles.

Por ejemplo:
```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```

Como podemos ver, la función lo que hace es calcular el factorial de un número (que consiste en multiplicar los números enteros del 1 hasta el solicitado). Para lograrlo, la función se llama a sí misma con un valor menor, es decir, va disminuyendo el número en 1 cada vez (n - 1), hasta que llega al caso base: cuando n es igual a 0.

El caso base (`if n <= : return 1`) es muy importante, porque detiene la recursión. Si no lo tuviera, la función se seguiría llamando a sí misma para siempre, causando un error (pues al menos Python cuenta con un _límite de profundidad de recursión_).

Por ejemplo, si queremos calcular `factorial(3)`, la función haría esto:
```python
factorial(3)  
= 3 * factorial(2)  
= 3 * (2 * factorial(1))  
= 3 * 2 * 1 
= 6
```
El proceso consiste en ir descomponiendo el problema en pasos más pequeños y fáciles de manejar. Puede llegar a facilitar mucho algunos cálculos, en especial reemplazado bucles y simplificando algunos algoritmos (como **árboles**, gráfos, etc.).

Si bien la recursividad puede llegar a enredar un poco al principio, al dominarla es en extremo útil. Veamos otro ejemplo calculando la serie de Fibonacci:
```python
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

Recordemos que la serie de Fibonacci es una secuencia de números donde cada número es la suma de los dos anteriores. Comienza así:
```
1, 1, 2, 3, 5, 8, 13, 21, ...
```
En esta serie: el primer número es 1, el segundo número es 1, el tercero es 1 + 1 = 2, el cuarto es 1 + 2 = 3, el quinto es 2 + 3 = 5 ... y así sucesivamente.

La función `fibonacci(n)` que vimos, usa recursividad para calcular el n-ésimo número de la serie. Por ejemplo:
```python
fibonacci(5)
= fibonacci(4) + fibonacci(3)
= (fibonacci(3) + fibonacci(2)) + (fibonacci(2) + fibonacci(1))
= ...
= 5
```
Cada llamada se divide en dos llamadas más pequeñas, y se van sumando hasta llegar a los casos base: `fibonacci(1)` y `fibonacci(2)`, que devuelven 1.
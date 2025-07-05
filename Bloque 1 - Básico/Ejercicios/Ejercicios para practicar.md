Felicidades por completar el primer bloque del curso de Python. Si ha llegado hasta aquí, seguramente le gusta mucho programar. 

Y como nos gusta ~~torturar~~ fomentar a los estudiantes a mejorar sus habilidades en programación, hemos decidido proporcionarle un conjunto de ejercicios con los cuales pueda poner en práctica todo aquello que ~~se supone~~ aprendió. Recuerde además que en programación casi siempre existen muchas formas de hacer una cosa, así que seguramente encontrará más de una forma de completar el ejercicio.

No se preocupe, no perderá nada si falla. Aunque tampoco ganará mucho si los completa, le animamos a intentarlo. Le aseguramos que se divertirá.

### Ejercicio N.1

> TicTacToe

Cree un programa en el cual se pueda jugar el clásico tictactoe (tres en raya, X-0 o como guste llamarlo).

El objetivo es que pueda imprimir en pantalla algo similar a esto:
```
Tablero:
 X | X | X
-----------
 O | X |
-----------
   | O | O

¡X ha ganado!
```

Debe permitir que dos jugadores se turnen para ingresar sus movimientos. Si su programa puede detectar automáticamente quién gana, mejor. Si no… bueno, al menos se verá bonito.

### Ejercicio N.2

> Calculadora básica

Cree un programa que funcione como una calculadora simple. Debe permitir al usuario elegir una operación entre suma, resta, multiplicación y división, e ingresar dos números. Luego, el programa debe mostrar el resultado de la operación.

Ejemplo de uso:

```
Elige la operación (+, -, *, /): *
Ingresa el primer número: 4
Ingresa el segundo número: 5
Resultado: 20
```

No olvide cuidar que, si se intenta dividir entre cero, el programa no se vuelva loco y avise que no se puede.

### Ejercicio N.3

> Lista de compras

Imagine que necesita ir a comprar varias cosas. Lo normal es hacer una lista de compras, anotando todas las cosas que necesita comprar. Pues ese será su objetivo en este ejercicio.

Tendrá que crear un programa que pueda contener una lista de compras. Que pueda agregarle cosas, cantidad de cada cosa, precio estimado, precio real (para cuando las compre), mostrar las que faltan comprar, y calcular cuanto gastó (con lo que ya compró) y cuanto le falta gastar (con los precios estimados de lo que le falta comprar).

Y que la interfaz sea algo similar a esto (no necesariamente igual):

```
Lista de compras:
- cantidad nombre    | precio estimado | precio real  | Estado       | 
---------------------|-----------------|--------------|--------------|
- 9 guineos verdes   | L. 27           | ~~~          | no comprado  |
- 1 Coca de 3 litros | L. 55           | L. 55        | listo        |
----------------------------------------------------------------------
total estimado:      L. 77
total gastado:       L. 55
estimado por gastar: L. 27
```

### Ejercicio N.4

> Secuencias

¿Conoce la sucesión de Fibonacci? Es una secuencia muy bonita que sigue el patrón $1, 1, 2, 3, 5, 8 \cdots$ que es la suma de los dos números anteriores.

Es una secuencia muy conocida y útil para aprender conceptos como la recursividad. De hecho, anteriormente vimos la secuencia de Fibonacci en un ejemplo del tema de recursividad.

Es por eso que no puedo solicitarle que haga solamente la secuencia de Fibonacci, pues ya la tiene.

Así que, su objetivo será:
```
Seleccione una sucesión:
   [1] - Sucesión de Fibonacci
   [2] - Sucesión de cuadrados
   [3] - Sucesión de triángulos
   [4] - Sucesión de Padovan
   [5] - Sucesión de Catalan
```

Y al elegir una:
```
Seleccione cuantos números desea ver: 
```

Básicamente, que muestre la sucesión hasta la $n$ posición. Por ejemplo, si elegimos la de Fibonacci hasta el $7$, sería: $1, 1, 2, 3, 5, 8, 13$.

Yo le incito a investigar sobre cada sucesión, pero para ahorrarle trabajo por si no quiere buscar:
- Sucesión de Fibonacci: Cada número es la suma de los dos anteriores, es decir $P(k) = P(k - 1) + P(k - 2)$.
- Sucesión de cuadrados: Los cuadrados de los naturales, o sea $P(k) = k^2$.
- Sucesión de triángulos: La suma desde $0$ hasta $k$, es decir $P(k) = \frac{k(k+1)}{2}$.
- Sucesión de Padovan: la suma del segundo y tercer anteriores, o sea $P(k) = P(k - 2) + P(k - 3)$. Como Fibonacci más o menos.
- Sucesión de Catalan: $P(k) = \frac{1}{k+1}\binom{2k}{k} = \frac{(2k)!}{(k+1)! \cdot k!}$

### Ejercicio N.5

Es usted un estudiante de física. Y por alguna razón desea comprobar sus cálculos usando un programa en Python. Por el momento, solo está estudiando caída libre y proyectiles (consideraremos que caída libre es un caso especial de proyectiles tal que $v_0=0$ y $\theta = 270\degree$).

Pues bien, creará un programa en que se ingresen la velocidad inicial $v_0$ y el ángulo de lanzamiento $\theta$. El programa mostrará las coordenadas del proyectil en ciertos intervalos de tiempo (proporcionado por el usuario) asumiendo que el proyectil salió desde el punto de referencia $(0, 0)$. Considere que la gravedad sea $g = 9.8\text{m/s}^2$.

```
Velocidad inicial v0 (m/s): 20
Ángulo de lanzamiento θ (grados): 45
Intervalo de tiempo (s): 0.5
Tiempo total de simulación (s): 3

Tiempo (s)	X (m)		Y (m)
0.00		0.00		0.00
0.50		7.07		5.33
1.00		14.14		8.58
1.50		21.21		9.75
2.00		28.28		8.83
2.50		35.36		5.83
3.00		42.43		0.75
```

Es importante aclarar que deberá usar `math.sin` y `math.cos`. Y también podría usar `math.sqrt` para la raíz. Estas son funciones que se pueden usar al colocar al principio `import math`. Y se usan como cualquier función.

#### **Posición en función del tiempo:**

$x(t) = v_0 \cos(\theta) \cdot t$

$y(t) = v_0 \sin(\theta) \cdot t - \frac{1}{2} g t^2$

---
Bueno, eso es todo, diviértase :)

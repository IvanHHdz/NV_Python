Miau, miau miau miau.
> Proximamente, todavía se está trabajando en esta parte

# Ejercicio 1
Existen muchos algoritmos para ordenar arreglos o listas. Al igual que existe más de una forma de encontrar elementos dentro de un arreglo. 

Estos algoritmos tienen distintos tiempos para ordenar, todos en función del la cantidad de elementos que contiene el arreglo. A esto se le llama _complejidad_. Una de las medidas más usadas es la de _Big O_. 

Para este ejercicio, usted tomará en consideración 5 de los algoritmos más usados para ordenamiento:
| Nombre            | Descripción                                   | Complejidad   |
|-------------------|-----------------------------------------------|---------------|
| Bubble Sort       | Intercambia pares adyacentes.                 | $O(n^2)$      |
| Selection Sort    | Selecciona el mínimo y lo coloca al inicio.   | $O(n^2)$      |
| Insertion Sort    | Inserta cada elemento en su lugar.            | $O(n^2)$      |
| Merge Sort        | Divide y combina ordenadamente.               | $O(n \log n)$ |
| Quick Sort        | Usa pivotes para dividir y ordenar.           | $O(n \log n)$ |

Su tarea no será complicada, no se preocupe. Simplemente tendrá que implementar los 5 algoritmos presentados anteriormente, medir el tiempo de cada uno (la sugerencia es utilizar decoradores, aunque cualquier forma de medirlos estará bien), guardar los tiempos y graficarlos.

Esta última parte es importante, usted graficará los tiempos de ordenamiento de cada algoritmo utilizando `matplotlib`. Lo hará en relación tamaño - tiempo.

Utilizará arreglos con datos aleatorios que vayan desde 0 hasta 100. Los arreglos tendrán tamaños de 1, 5, 10, 15, 20, 30, 40, 50, 75, 100, 150, 200, 300, 400, 500, 750, 1000, 2000, 5000, 10000. Haga cada tamaño 10 veces, y use el promedio para la gráfica (para evitar el ruido). 

# Ejercicio 2

Imagine que un día va de visita a casa de sus bisabuelos. Su bisabuelo (Richard) entonces empieza a contarle:

> Mire, yo no le he contado, pero yo estuve en el Titanic, y sobreviví.
> Sí, aunque no me crea, ahí estuve cuando se hundió.
> Hasta agarré un pedazo del iceberg.

Usted sabe que su bisabuelo es un mentiroso de primera, así que pone en duda la historia.
Además, ¿en serio agarró un pedazo del iceberg?
Pero entonces él saca una prueba:

> Tienes razón, no agarré un pedazo del iceberg. Era muy pequeño, y es más, ni siquiera recuerdo nada. Era tan solo un bebé. Viajé con mis dos hermanas y mi mamá. Y como prueba, aquí tienes el ticket.

Es entonces cuando saca un arrugado y dañado ticket. Estaba demasiado dañado como para leerlo todo, pero si logras leer algunas partes:
- Era, efectivamente, para el Titanic
- Abordaban en Southampton
- El número comenzaba por 23

Aunque sonaba muy convincente, no podías creerla por completo. Después de todo, tu bisabuelo ya te había engañado varias veces con historias falsas.

Así que, como buen _data scientist_, decide usted investigar más y encuentra el _DataSet_ de los pasajeros del Titanic, [este _DataSet_](../Data/titanic.csv) lo utiliza para invesigar, necesita saber la verdad de uan vez por todas.

Poco después de salir de la casa de su bisabuelo, se encuetra con su mejor amigo, a quien le cuenta la historia. Y el afirma que también su bisabuelo estuvo en el Titanic. Usted no se lo cree, sería mucha coincidencia. Pero su amigo se lo asegura. 

Él afirma que, aunque no tiene ya el boleto, su bisabuelo, de apellido Smith, le había contado que él estuvo el Titanic, en primera clase, siendo un niño, viajaba con sus dos padres y abordó en Queenstown.

Suena muy convincente, y mucha coincidencia, también deberá investigarlo. No sea que su amigo le esté inventado una mentira.

Antes de empezar a investigar, tiene usted una cita con su novia, pues ya la tenía planeada y ponerse a investigar una historia de su mentiroso bisabuelo no es excusa para cancelar. En la cita, le cuenta la historia a su novia, que le dice:

> Casualmente, estaba limpiando unas cosas en casa y encontré esto y te lo quería mostrar:

Y por sorpresa, era un boleto de Titanic. A nombre de alguien con apellido _Salkjelsvik_, por el que se pagaron £7.65 en tercera clase y que aborda en Southampton. Su novia no tiene ni idea de quién podría ser pues es la primera vez que lee ese apellido, así que toca investigar también. Lastimosamente, no se alcanza a leer el número del ticket.

Pero claro, usted, como buen _Data Scientist_, sabe cómo resolver este problema e investigará la veracidad de la historia de su bisabuelo, la historia del bisabuelo de su mejor amigo y la historia detrás del misterioso boleto que encontró su novia.
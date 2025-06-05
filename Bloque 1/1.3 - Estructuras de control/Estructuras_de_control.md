# Condicionales (`if`, `elif`, `else`)

Ahora, supongamos que le solicito al usuario su edad, ¿cómo puedo saber si es menor o mayor de edad? ¿o si es de la tercera edad?

Esto se hace por medio de condiciones. Python (como cualquer lenguaje de programación) tiene estructuras de control que sirven para que el programa haga ciertas cosas **si** ciertas condiciones se cumplen.

Estas estructuras de control son `if`, `elif`, y `else`.

La estructura básica es:
```python
if condicion1:    # Primera condición que se verificará
   codigo1        # Código que se ejecutará si se cumple la primera condición
elif condicion2:  # En caso que la primera condición no se cumpla, se verifica la segunda
   codigo2        # Código que se ejecutará si se cumple la segunda condición
else:             # En caso que ninguna condición se cumpla
   codigo2        # Código que se ejecutará si ninguna condición se cumple
```

Las condiciones suelen ser comparaciones u operaciones lógicas que tengan un valor booleano, y el código se ejecutará si la condición tiene un valor `True`.

Se pueden colocar todos los `elif` que necesitemos (incluso no colocar si no los necesitamos) y se puede omitir el `else`.

Ahora, volviendo a la pregunta del principio: ¿cómo puedo saber si es menor o mayor de edad? ¿o si es de la tercera edad? Sencillo, con estructuras de control.

```python
# Creamos una variable llamada edad que almacenará la edad del usuario. Preguntamos al usuario su edad utilizando la función input() y convertimos ese valor a entero con la función int(), ya que las edades son números enteros.
edad = int(input("¿Cuántos años tienes? "))

# Verificamos si su edad es menor que 18
if edad < 18:
   # Si es menor de 18, es menor de edad
   print("Eres menor de edad.")
# Si no es menor de 18, entonces vemos si es menor de 65, ya que si es mayor de 18 y menor de 65 es un adulto
elif edad < 65:
   # Si es menor de 65 significa que su edad está entre 18 y 65, y por lo tanto es un adulto.
   print("Eres adulto.")
# Si ninguna de las condiciones anteriores se cumplen, entonces debe ser mayor de 65
else:
   # Si no es menor de 65, entonces es mayor a 65, y por ende es una persona de la tercera edad
   print("Eres una persona de la tercera edad.")
```

**Nota importante**: Hay que asegurarnos que el interlineado sea correcto.

# Bucles (`while`, `for`)

Ahora imaginemos que no quiero saber la edad de una persona, sino que quiero la edad de 3, y calcular la media de esas edades. O mejor aún, que no sé cuantas edades voy a ingresar. ¿Cómo lo hago? ¿Tendré que escribir ese mismo código 3 veces? ¿Y si no sé cuantas veces necesito repetirlo? Bueno, para eso están los bucles.

Los bucles son una forma de hacer que el programa repita varias veces un bloque de código. En Python tenemos dos tipos: `while` y `for`.

`for` repite un bloque de código una cierta cantidad de veces. Hay muchas formas de usar el `for`, en esta ocación nos centraremos en usarlo junto con la función `range`.

```python
# i es una variable cualquiera (por conveniencia se usa i) preferiblemente no usada. n es la cantidad de veces que se ejecutará el bucle. A lo largo del bucle, i tomará los valores desde 0 hasta n - 1.
for i in range(n):   # range(último valor) o también range(primer valor, último valor, intervalo) en ambos casos no incluye el último valor, sino el anterior a este
   codigo            # Aquí va el código que se ejecutará en cada ciclo del bucle
```

Con el problema que teníamos antes (pedir la edad 3 veces y calcular la media) lo conseguimos de la siguiente forma:
```python
suma = 0   # Creamos una variable que tendrá la suma de las edades
# Con la media lo que haremos es sumar todas las edades y luego dividirlas entre 3, por lo que la iniciamos en 3
for i in range(3):   # Hacemos un for que se repetirá 3 veces
   edad = int(input("¿Cuántos años tienes? "))  # Preguntamos la edad
   suma += edad  # Sumamos la edad ingresada
   # Verificamos si es menor o mayor de edad, o si es de la tercera edad
   if edad < 18:
      print("Eres menor de edad.")
   elif edad < 65:
      print("Eres adulto.")
   else:
      print("Eres una persona de la tercera edad.")
media = suma / 3  # Calculamos la media
print("La media de las edades es: " + str(media)) # Mostramos en pantalla cuanto es la media, convirtiendola primero a str
```

Pero, ¿y si no son 3 edades, sino más? ¿y si ni siquiera sé cuántas edades son? Para eso está el `while`.

Lo que hace `while` es repetir el bloque de código _mientras_ una condición sea verdadera (`True`). Su sintaxis es:

```python
while condición:  # Condición que se evaluará para repetir el código
   código         # Código que se ejecutará si la condición se cumple
```

Con el problema que nos quedaba (no conozco el numero de edades) podemos hacerlo de la siguiente forma:
```python
suma = 0          # Creamos una variable que tendrá la suma de las edades
iteraciones = 0   # Creamos una variable para saber cuántas edades se ingresaron
edad = 0          # Iniciamos la variable de edad, ya que la usamos en la condición del while
while edad >= 0:  # Iniciamos el bucle, que s ejecutará mientras edad sea mayor o igual a 0
   edad = int(input("¿Cuántos años tienes? "))  # Preguntamos la edad
   if edad < 0:   # Verificamos si la edad es negativa
      break       # Si es negativa, entonces terminamos el bucle antes de sumar la edad o aumentar la variable iteraciones
   # Ya se explicará el break
   iteraciones += 1  # Sumamos una iteración
   suma += edad   # Sumamos la edad ingresada
   # Verificamos si es menor o mayor de edad, o si es de la tercera edad
   if edad < 18:
      print("Eres menor de edad.")
   elif edad < 65:
      print("Eres adulto.")
   else:
      print("Eres una persona de la tercera edad.")
media = suma / iteraciones # Calculamos la media
print("La media de las edades es: " + str(media)) # Mostramos en pantalla cuanto es la media, convirtiendola primero a str
```

# Interrupción de flujo

Anteriormente hemos visto el `break`, este comando sirve para interrumpir el flujo del programa. Existen principalmente 3 comandos que sirven para alterar el flujo de un programa: `break`, `continue` y `pass`.

Como mencionábamos, `break` sirve para interrumpir un bucle (ya sea `for` o `while`), saliéndose inmediatamente del bucle, aunque el bucle deba seguir. Un ejemplo:
```python
while True: # Como la condición es True, se debería ejecutar para siempre
    if input("Ingrese 's' para salir") == 's':  # Sin embargo, si ingresamos 's' cuando nos lo solicita, el programa entrará en el condicional
        break   # Y ejecutará el break
# Haciendo que se salga del bucle
```

`continue` también se utiliza en bucles, pero se usa para volver al inicio del bucle y verificar la condición, saltándose las líneas que siguen (si hay más líneas). Ejemplo:
```python
for i in range(1, 6):   # Un bucle for en el que i tomará los valores desde 1 hasta 5
    if i == 3:
        continue  # Salta esta vuelta si i es 3
    print(i)      # Imprime el número, excepto 3 ya que se lo salta
```

Por último, tenemos a `pass`, que simplemente pasa. Es útil cuando hay estructuras de control (funciones, condicionales, bucles, etc.) que sabemos que vamos a usar, pero aún no vamos a programar qué hacer. `pass` nos ayuda a dejar esa parte vacía sin que se detecte como un error. Ejemplo:
```python
for i in range(10):
   print(i)    # Imprimirá los valores desde 0 hasta 9
   if i == 3:  # Supongamos que queremos hacer algo especial cuando llegue a 3
      pass     # Pero como aún no sabemos qué harémos, dejamos un pass
```
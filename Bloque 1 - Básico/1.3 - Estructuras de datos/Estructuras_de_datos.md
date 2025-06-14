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

Como dato curioso, los conjuntos también tienen sus propias operaciones, las _operaciones de conjuntos_, que son precisamente las operaciones de conjuntos matemáticos: unión ($A \cup B$), intersección ($A \cap B$), diferencia ($A - B$) y diferencia simétrica ( $(A \cup B) \land \neg(A \cap B)$ ).
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

Una forma sencilla de entender los diccionarios, si se está acostumbrado a la matemática, es la definición formal de función: $f : X \to Y$ donde el diccionario sería la función, las claves serían $X$ y los valores $Y$. Más adelante también se ve el método `.items()` que básicamente retornaría el conjunto de $f \subset X\times Y$. Y con `.keys()` y `.values()` se obtendrían $X$ y $Y$ respectivamente.

# Métodos y funciones comunes de cada tipo de dato

Cada tipo de dato tiene distintas funciones y/o métodos que se suelen ser usadas a menudo. Las principales son:

Para `int` y `float`:
```python
a = -3
b = 1.618033988
c = 1

# Valor absoluto
abs(a)      # 3

# Redondear
round(b, 2) # 1.62

# Convertir a entero
int(b)    # 1

# Convertir a float
float(c)    # 1.0
```

Para `str`:
```python
texto = "Camello Patagonico"

# Recordemos que las str funcionan de forma similar a las listas

# Carácter en la posición 3
texto[3]       # 'e'

# Carácteres desde la posición 3 hasta la 10
texto[3:10]    # 'ello Pa'

# Carácteres desde el 3 hasta el 10 de 2 en 2
texto[3:10:2]  # 'el a'

# En cuanto a los métodos de las str

# Convierte a minúsculas
texto.lower()     # "camello patagonico"

# Convierte a mayúsculas
texto.upper()     # "CAMELLO PATAGONICO"

# Reemplaza una parte
texto.replace("Patagonico", "de la Patagonia")  # "Camello de la Patagonia"

# Divide la str
texto.split()     # ["Camello", "Patagonico"]
texto.split('a')  # ["C", "mello P", "t", "gonico"]    

# Encuentra algo en la str
texto.find("m")   # 2 (quiere decir que hay una 'm' en la posición 2)
```

Para `bool` solo hay conversiones:
```python
bool(0)        # False
bool("hola")   # True
```

Para las litas:
```python
lista = [1, 2, 3]
lista.append(4)      # [1, 2, 3, 4]
lista.remove(2)      # [1, 3, 4]
lista.pop()          # Quita el último: [1, 3]
lista.sort()         # Ordena
lista.reverse()      # Invierte el orden
```

Para las tuplas:
```python
tupla = (1, 2, 2, 3)
tupla.count(2)       # 2
tupla.index(3)       # 3 (posición)
```

Para los conjuntos:
```python
conjunto = {1, 2, 3}
conjunto.add(4)                  # {1, 2, 3, 4}
conjunto.remove(2)               # {1, 3, 4}
conjunto.union({5})              # {1, 3, 4, 5}
conjunto.intersection({3, 5})    # {3}
```

Y para los diccionarios:
```python
diccionario = {"a": 1, "b": 2}
diccionario.keys()      # dict_keys(['a', 'b'])
diccionario.values()    # dict_values([1, 2])
diccionario.items()     # dict_items([('a', 1), ('b', 2)])
diccionario.get("a")    # 1
diccionario.pop("b")    # {"a": 1}
```

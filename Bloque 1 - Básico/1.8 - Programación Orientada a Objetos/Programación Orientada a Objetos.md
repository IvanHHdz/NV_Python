# Clases y objetos

La programación orientada a objetos está basada en cómo funcionan los objetos en la vida real. Pues al igual que en la vida real, los objetos que creamos en Python (y en otros muchos lenguajes de programación), tienen ciertos atributos (o características únicas) y ciertos métodos (que son las acciones que pueden realizar o que se les puede realizar).

Un ejemplo sencillo que sirve como analogía para entender este concepto es el de una tasa de café. Imaginemos que existe la idea, el concepto o la **Clase** que representa una tasa. En Python quedaría así:
```python
# Usamos la palabra reservada class y le damos un nombre a nuestra clase, que llamaremos Tasa en esta ocación
class Tasa:
    # Esta parte de aquí es el iniciador, de momento vacío pero que llenaremos pronto
    def __init__(self):
        pass
```

Así, tendríamos la clase `tasa` la cual nos sirve para crear tasas en nuestro programa:
```python
def main():
    mi_tasa = Tasa()
```

Cuando utilizamos una clase, creamos una instancia de un objeto, en este caso estamos creando una instancia (o copia) de `Tasa` la cual estamos llamando `mi_tasa`.

Pero claro, como dijimos antes, los objetos en Python, al igual que en el mundo real, tienen atributos y métodos, los cuales veremos a continuación.

# Atributos y métodos

Como mencionabamos en la analogía, los atributos y los métodos representan las características y las acciones que posee un objeto. Por ejemplo, siguiendo con la tasa, una tasa puede tener diversas características: color, material, tamaño, etc. En Python, las colocaríamos de la siguiente manera:
```python
class Tasa:
    def __init__(self, color, material, size):
        self.color = color
        self.material = material
        self.size = size
```

Y ahora, al hacer una instancia de `Tasa` que tenga ciertas características:
```python
def main():
    mi_tasa = Tasa('Blanco', 'Plastico', 'Mediana')
```

Y también podemos ver cada atributo con:
```python
print(mi_tasa.color)
print(mi_tasa.material)
print(mi_tasa.size)
```

De la misma forma, además de tener atributos, podemos hacer que los objetos tengan ciertas acciones, a las que llamaremos métodos. Por ejemplo, una tasa podemos llenarla con algo, como café, o tomar de ella.

Estos métodos los declaramos como funciones dentro de la clase, de la siguiente forma:
```python
class Tasa:
    def __init__(self, color, material, size):
        self.color = color
        self.material = material
        self.size = size
        self.llena = False
        self.contenido = 'Vacía'
    
    def llenar(self, contenido):
        self.contenido = contenido
        self.llena = True
    
    def tomar(self):
        self.llena = False
```

Ahora podemos llenar la tasa con café:
```python
def main():
    mi_tasa = Tasa('Blanco', 'Plástico', 'Mediana')
    mi_tasa.llenar('Café')

    print(f"Mi tasa es de color {mi_tasa.color}, material {mi_tasa.material} y tamaño {mi_tasa.size}")

    if (mi_tasa.llena):
        print(f"Mi tasa está llena de {mi_tasa.contenido}")
        mi_tasa.tomar()
        print("Ahora está vacía")
    else:
        print("Mi tasa está vacía!")
```

Ahora bien, esta analogía ha sido muy útil para ilustrar los conceptos de lo que es una clase y un objeto, y cómo funcionan los atributos y las funciones. Pero claro, no es muy frecuente programar una tasa. Así que, dejando la analogía, a continuación un ejemplo más útil que consiste en una lista de cosas por hacer:
```python
class Lista:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea, prioridad, estado='Pendiente'):
        self.tareas.append({
            'tarea': tarea,
            'prioridad': prioridad,
            'estado': estado
        })
    
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
            return
        
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea['tarea']} - Prioridad: {tarea['prioridad']} - Estado: {tarea['estado']}")
    
    def completar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            self.tareas[indice - 1]['estado'] = 'Completada'
            print(f"Tarea '{self.tareas[indice - 1]['tarea']}' marcada como completada.")
        else:
            print("Índice de tarea inválido.")
```

# Métodos especiales (_Dunder methods_)
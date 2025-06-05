# Python
Python es un lenguaje de programación. Muy popular por su facilidad a la hora de escribirse y leerse, gran comunidad e inmensa cantidad de librerías.

Fue creado para ser fácil y rápido de programar, para que todo aquel que quisiera aprender pudiera hacerlo sin excesivas complicaciones.

Su filosofía reside ahí, en ser un lenguaje sencillo, limpio y fácil de aprender. Si usamos `import this` lo podemos leer:

```txt
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Como un poco de historia: Python fue creado por Guido van Rossum en 1989 en los Países Bajos. Quería un lenguaje fácil de leer y usar, como alternativa a otros lenguajes más complejos. En 1991, publicó la primera versión (Python 0.9.0). En la actualidad, Python es uno de los lenguajes más populares del mundo. Se usa en inteligencia artificial, ciencia de datos, web, automatización, educación y más.

# Descargar Python

Para utililzar Python, primero debemos descargarlo desde el [sitio oficial](https://www.python.org/). Al instalarlo, nos intalará IDLE (_Integrated Development and Learning Environment_) también. 

IDLE es IDE (_Integrated Development Environment_), que es un programa que te ayuda a escribir, probar y corregir código de forma más fácil.

Existen muchos IDEs para Python, además de IDLE, los más populares son: 
* [PyCharm](https://www.jetbrains.com/pycharm/download/)
* [Jupyter Notebook](https://jupyter.org/install)
* [Thonny](https://thonny.org/)
* [Sublime Text](https://www.sublimetext.com/)
* [Spyder](https://www.spyder-ide.org/)
* [Atom](https://atom.io/)
* [PyDev](https://www.pydev.org/)
* [Wing IDE](https://wingware.com/downloads)
* [Eric](https://eric-ide.python-projects.org/)
* [Rodeo](https://github.com/yhat/rodeo/releases)

Una vez instalado Python, lo recomendable es descargar algún IDE (el que a uno más le guste) para comenzar a programar.

Para efectos de enseñanza, se ha decidido usar VS Code como IDE aquí. Para descargarlo se va a la [página oficial](https://code.visualstudio.com/download). También se pueden instalar extensiones para facilitar ciertas cosas, estas se pueden descargar desde el menú de extensiones de VS Code.

# Hello World!

Una vez que está todo listo, es momento de empezar a programar. Comenzaremos con el programa por defecto que se hace al iniciar a aprender un lenguaje de programación: _Hola Mundo_.

En el IDE de preferencia, creamos un nuevo archivo y dentro escribimos:

```python
print("Hola mundo!")
```

Lo guardamos como `hola_mundo.py` (el nombre no es importante, la extensión `.py` sí). Y ejecutamos (el cómo ejecutar varía en cada IDE). En VS Code esto se hace seleccionando el ícono de _play_ en la parte superior derecha.

Este programa lo que hará es mostrar en consola:
```txt
Hola mundo!
```

Explicando un poco la línea que escribimos, `print()` es una función, es decir, una instrucción que realiza una tarea específica. En este caso, la función `print()` lo que hace es mostrar en pantalla. Las funciones tienen parámetros, en este caso `"Hola mundo!"` es el parámetro que pasamos, ya que es eso lo que queremos mostrar en pantalla. Usamos las comillas en `"Hola mundo!"` para que Python entienda que es texto.
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

**Instrucciones**:

1. Entrar al sitio web.
2. Clic en el botón "Download Python".
3. Ejecutar el instalador de Python.

Importante: durante la instalación, asegúrate de marcar la casilla "Add Python to PATH" antes de hacer clic en "Install Now". Esto permite que puedas usar Python desde la terminal o línea de comandos.

4. Una vez instalado, también se instalará una herramienta llamada IDLE.

IDLE (_Integrated Development and Learning Environment_) es el IDE (_Integrated Development Environment_) predeterminado de Python, que es un programa que te ayuda a escribir, probar y corregir código de forma más fácil.

Aunque IDLE funciona bien, existen muchos IDEs más avanzados que ofrecen mejores herramientas para programar de manera más cómoda y eficiente:
| IDE/Editor           | Enlace de descarga                                                    | Características principales                        |
| -------------------- | --------------------------------------------------------------------- | -------------------------------------------------- |
| **VS Code**          | [code.visualstudio.com](https://code.visualstudio.com/download)       | Editor ligero, extensible, muy usado.              |
| **PyCharm**          | [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/)  | IDE profesional, excelente para grandes proyectos. |
| **Jupyter Notebook** | [jupyter.org](https://jupyter.org/install)                            | Ideal para ciencia de datos y visualización.       |
| **Thonny**           | [thonny.org](https://thonny.org/)                                     | Muy simple, ideal para principiantes.              |
| **Sublime Text**     | [sublimetext.com](https://www.sublimetext.com/)                       | Editor rápido y personalizable.                    |
| **Spyder**           | [spyder-ide.org](https://www.spyder-ide.org/)                         | Enfocado en ciencia de datos y análisis.           |
| **Atom**             | [atom.io](https://atom.io/)                                           | Editor flexible y extensible (ya no se actualiza). |
| **PyDev**            | [pydev.org](https://www.pydev.org/)                                   | Plugin de Python para Eclipse.                     |
| **Wing IDE**         | [wingware.com](https://wingware.com/downloads)                        | IDE profesional con herramientas de depuración.    |
| **Eric**             | [eric-ide.python-projects.org](https://eric-ide.python-projects.org/) | Completo y con muchas funciones.                   |
| **Rodeo**            | [github.com/yhat/rodeo](https://github.com/yhat/rodeo/releases)       | Similar a RStudio, enfocado en análisis.           |


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
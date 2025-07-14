# Entornos Virtuales

Primero comencemos hablando de los entornos virtuales. Un entorno virtual es una instalación aislada de Python, junto a los paquetes que instalemos con él. Esto resulta muy útil para evitar conflictos de paquetes o versiones y mantener un mejor orden.

También es muy usado para administrar mejor las versiones de los propios paquetes. Por ejemplo, si un programa necesita una versión de un paquete y otra necesita otra, podemos trabajar con distintos entornos para que no exista problemas.

Pero, para entender mejor su utilidad, debemos tener en cuenta que podemos usar muchos paquetes que ya han sido creados. Hasta el momento, solamente hemos utilizado paquetes que nosotros mismos hemos creado y uno que otro que hemos mencionado. Pero existe una enorme cantidad de paquetes disponibles, tanto preinstalados como instalables (los cuales estamos a punto de ver) y para gestionarlos mejor existen los **entornos virtuales**.

Pero ¿cómo creamos y utilizamos un entorno virtual?

La forma más sencilla es con el comando 
```shell
python -m venv nombre_del_entorno
```
Esto creará el entorno con el nombre `nombre_del_entorno`. Y para activarlo:
```shell
nombre_del_entorno\Script\activate
```
nota: en linux se activa con `source nombre_del_entorno/bin/activate`.

Y se desactiva con:
```shell
deactivate
```

De todas formas, si usan VS Code, es más sencillo. Solo buscan abren el buscador de comandos (`Ctrl + Shift + P` por defecto) y buscan `Python: Select Interpreter` y les da la opción de crear uno y activarlo.


# `pip`

Volviendo al tema de instalar paquetes. Como hemos visto anteriormente en la sección 1.5, podemos usar paquetes con:
```python 
import math                 # importar módulo de matemáticas
import pickle as p          # importar módulo usando apodo
from time import sleep      # importar una función del paquete
from os import system as s  # Importar una función del paquete usando un apodo
```

Esto funciona de la misma forma si son paquetes que nosotros creamos, paquetes preinstalados o paquetes que instalamos.

Pero ¿cómo instalamos paquetes?

Una de las formas más comunes es mediante `pip`. Esta es la herramienta estándar para instalar paquetes desde el Python Package Index (PyPI). La cual se instala por defecto al descargar Python.

Para instalar un paquete, simplemente debemos colocar, por ejemplo:
```shell
pip install numpy
```

Lo cual, instalará `numpy`.

Algo que resulta muy útil es el uso de `requirements.txt`, que es una forma de instalar muchas dependencias necesarias. Como su nombre sugiere, se usa para instalar los requisitos para ejecutar un programa (uno que usa ciertas dependencias).

Podemos guardar qué descargamos para nuestro proyecto (usualmente usando un entorno virtual) con:
```shell
pip freeze > requirements.txt
```
Lo cual guardará en `requirements.txt` todo lo que instalamos. Y si queremos instalarlo, simplemente usamos:
```shell
pip install -r requirements.txt
```
E instalará todas las dependencias que colocamos en el `requirements.txt`.


# `conda` y anaconda

`conda` es un gestor de paquetes (similar a `pip`) y de entornos (similar a `venv`). La ventaja que tiene sobre `pip` es que permite instalar paquetes incluso de otros lenguajes (necesario en ciertas ocaciones) y resulta mucho más útil en entornos científicos (como ciencia de datos, machine learning, inteligencia artificial, etc.).

Algunos comandos básicos de `conda`, similares a los vistos antes:
```shell
conda create -n nombre_del_entorno python=3.10  # crea un entorno virtual con una versión específica de python
conda activate nombre_del_entorno               # activa el entorno virtual
conda deactivate                                # desactiva el entorno virtual
conda install numpy                             # instala un paquete, numpy en este caso
```

Anaconda, por otro lado, es una distribución de Python que incluye todo lo que instalamos al principio con Python, más cosas extra como `conda`, librerías científicas, etc.

Podemos descargar anaconda desde el [sitio oficial](https://www.anaconda.com/download/success).
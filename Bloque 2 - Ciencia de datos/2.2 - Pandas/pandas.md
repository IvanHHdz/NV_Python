# Pandas

Pandas es una poderosa herramienta para el análisis de datos utilizando Python como base.

Ahora bien ¿Cómo utilizamos Pandas? Primero que nada, debemos instalarlo (si no lo tenemos instalado) e importarlo.

Para instalarlo, podemos usar:
```shell
pip install pandas
conda install -c conda-forge pandas
```
El primero es con `pip`, el segundo con `conda`. Cualquiera de los dos funcionará.

Y para importarlo dentro de nuestro archivo o nuestro Jupyter Noteboot:
```python
import pandas as pd
```

Por conveniencia, se suele utilizar el álias `pd` para Pandas.

# Data Frames y Series

Pandas trabaja con lo que se denomina `DataFrame`, que son estructuras de datos en 2 dimensiones que almacena distintos tipos de datos en columnas. Similares a tablas de datos (de _Excel_, por ejemplo) o a tablas de datos _SQL_.

Por ejemplo, imaginemos que tenemos los empleados de una empresa, con su nombre, edad y respectivo salario y puesto.

| ID    | Nombre    | Edad  | Salario   | Puesto        |
--------|-----------|-------|-----------|---------------|
| 0     | Juan      | 20    | 20,000    | Programador   |
| 1     | Luis      | 40    | 50,000    | Gerente       |
| 2     | José      | 30    | 35,000    | Supervisor    |

Ahora vamos a representarla dentro de un DataFrame de Pandas, de la siguiente manera:
```python
df = pd.DataFrame(
    {
        'ID'        : [0, 1, 2],
        'Nombre'    : ['Juan', 'Luis', 'José'],
        'Edad'      : [20, 40, 30],
        'Salario'   : [20000, 50000, 35000],
        'Puesto'    : ['Programador', 'Gerente', 'Supervisor']
    }
)
```

Esto creará la tabla que teníamos antes, la cual al imprimirla obtendríamos:
```
   ID Nombre  Edad  Salario       Puesto
0   0   Juan    20    20000  Programador
1   1   Luis    40    50000      Gerente
2   2   José    30    35000   Supervisor
```

Pero, tenemos un problemita aquí: El `ID` se está repitiendo. Esto se debe a que no hemos dicho que `ID` es el índex de la tabla. Esto lo hacemos con:
```python
df = df.set_index('ID')
```
Y ahora sí:
```
   Nombre  Edad  Salario       Puesto
ID                                   
0    Juan    20    20000  Programador
1    Luis    40    50000      Gerente
2    José    30    35000   Supervisor
```

Además, esta tabla la podemos dividir por sus columnas, de la siguiente forma:
```python
df['Nombre']
```
Obteniendo:
```
ID
0    Juan
1    Luis
2    José
Name: Nombre, dtype: object
```
A estas columnas se les suele llamar `Series`. 

Y como podemos ver, funciona similar a la forma en que accedemos a los valores de un diccionario, pues sigue la misma sintaxis.

Ahora bien, también podemos crear Series por separado. Esto se logra de la suguiente forma:
```python
s = pd.Series([1, 2, 3, 10])
```
Con lo que obtendremos:
```
0     1
1     2
2     3
3    10
dtype: int64
```

# Importar y exportar

Ahora, antes de empezar a ver a detalle cómo trabajamos con los datos de un DataFrame, veremos cómo podemos importarlos y exportarlos, en caso que necesitemos hacerlo.

## Importación

Primero, para importarlos. Esto dependerá hasta cierto punto del formato en que tengamos los datos. A continuación, una tabla con los datos más comunes (que mencionamos en la [sección 2.0](../2.0%20-%20Introducción%20a%20la%20ciencia%20de%20datos/Introduccion_a_la_ciencia_de_datos.md)):
| Formato    | Lectura                                                  | Extra   
| ---------- | ---------------------------------------------------------|------
| `.csv`     | `df = pd.read_csv('datos.csv')`                          | Podemos especificar el delimitador con el parámetro `delimiter=`
| `.xlsx`    | `df = pd.read_excel('archivo.xlsx', sheet_name='Hoja1')` | Requiere tener instalado `openpyxl` o `xlrd` según la versión de Excel.
| `.json`    | `df = pd.read_json('datos.json')`                        | ---
| `SQL`      | `conexion = sqlite3.connect('mi_base_de_datos.db')` y `df = pd.read_sql('SELECT * FROM tabla', conexion)`                                | ---
| `URL`     | `df = pd.read_csv('https://example.com/datos.csv')`| ---

## Exportación

En cuento a cómo exportamos datos, es similar. Exportar datos nos sirve para guardar los datos de un DataFrame en un archivo. Esto lo logramos de la siguiente forma:
| Formato    | Exportación                              
| ---------- | ---------------------------------------------|
| `.csv`     | `df.to_csv('salida.csv', index=False)`       |
| `.xlsx`    | `df.to_excel('salida.xlsx', index=False)`    |
| `.json`    | `df.to_json('salida.json', orient='records', lines=True)`|
| `SQL`      | `df.to_sql('nombre_tabla', conexion, if_exists='replace', index=False)`|

Por ejemplo, dado el DataFrame de empleados que hicimos arriba, podemos exportarlo con:
```python
df.to_csv('Empleados.csv', index=False)
```
Y ahora, podemos leerlo desde otros proyectos con:
```python
df = pd.read_csv('Empleados.csv')
```

# Exploración y manipulación

Ahora sí, vamos a ver cómo podemos trabajar con los datos. Para ejemplificar de manera sencilla vamos a seguir utilizando el DataFrame `df` de empleados que tenemos.

A continuación, una pequeña explicación de los métodos y atributos más útiles y usados.

## `.head()` y `.tail()`

Estas funciones nos muestran los primeros y últimos valores de un DataFrame.
```python
df.head()   # por defecto mostrará 5
df.tail(2)  # podemos también especificar la cantidad
```

## `.index` y `.columns`

Nos mostrarán los índices y las columnas:
```python
df.index    # [0, 1, 2]
df.columns  # ['Nombre', 'Edad', 'Salario', 'Puesto']
```

## `.max()` y `.min()`

Supongamos que deseamos saber cuál es el empleado más joven, o el que más gana, de los datos que tenemos. Bueno, eso lo logramos con:
```python
df['Edad'].min()    # el menor tiene 20
df['Salario'].max() # el que gana más gana 50000
```
## `.mean()`

Podemos también la media de los datos numéricos:
```python
df[['Edad', 'Salario']].mean()
# Edad          30.0
# Salario    35000.0
# dtype: float64
```

Esta también se puede aplicar a las filas, con el parámetro `axis=1`.

## `.describe()`

Si deseamos tener algunos datos estadísticos útiles de todo el DataFrame en general, podemos usar este método. Este dará una tabla con algunos datos útiles de las columnas a las que pueda aplicarselas:
```python
df.describe()
```
Obtendremos la siguiente tabla:
```
       Edad  Salario
count   3.0      3.0
mean   30.0  35000.0
std    10.0  15000.0
min    20.0  20000.0
25%    25.0  27500.0
50%    30.0  35000.0
75%    35.0  42500.0
max    40.0  50000.0
```

## `.T`
Transpone el DataFrame completo:
```python
df.T
```
Obtenemos:
```
ID                 0        1           2
Nombre          Juan     Luis        José
Edad              20       40          30
Salario        20000    50000       35000
Puesto   Programador  Gerente  Supervisor
```

## Ordenar

Ordenar las columnas:
```python
df.sort_index(axis=1, ascending=False)
```
```
    Salario       Puesto Nombre  Edad
ID                                   
0     20000  Programador   Juan    20
1     50000      Gerente   Luis    40
2     35000   Supervisor   José    30
```
U ordenar las filas
```python
df.sort_values(by="Nombre")
```
```
   Nombre  Edad  Salario       Puesto
ID                                   
2    José    30    35000   Supervisor
0    Juan    20    20000  Programador
1    Luis    40    50000      Gerente
```

# Selección de datos

> Nota, en esta sección vamos a utilizar el siguiente DataFrame:
```python
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Elena', 'Jorge', 'Lucía', 'Pedro', 'Sofía', 'Andrés',
                'Valeria', 'Tomás', 'Daniela', 'Raúl', 'Natalia'],
    'Edad': [23, 35, 45, 29, 31, 38, 26, 42, 34, 28, 30, 40, 27, 37, 33],
    'Ciudad': ['Madrid', 'Sevilla', 'Barcelona', 'Valencia', 'Bilbao', 'Zaragoza', 'Granada', 'Madrid',
                'Sevilla', 'Málaga', 'Toledo', 'Vigo', 'Murcia', 'Salamanca', 'León'],
    'Profesión': ['Ingeniera', 'Doctor', 'Profesor', 'Abogada', 'Contadora', 'Arquitecto', 'Diseñadora', 'Técnico',
                    'Psicóloga', 'Enfermero', 'Periodista', 'Chef', 'Veterinaria', 'Administrador', 'Analista'],
    'Salario': [2400, 3000, 2800, 2600, 2500, 3200, 2300, 2700, 2600, 2550, 2400, 2750, 2450, 2900, 2650]
}
df = pd.DataFrame(datos, index=range(1, 16))
df
#      Nombre  Edad     Ciudad      Profesión  Salario
# 1       Ana    23     Madrid      Ingeniera     2400
# 2      Luis    35    Sevilla         Doctor     3000
# 3    Carlos    45  Barcelona       Profesor     2800
# 4     Marta    29   Valencia        Abogada     2600
# 5     Elena    31     Bilbao      Contadora     2500
# 6     Jorge    38   Zaragoza     Arquitecto     3200
# 7     Lucía    26    Granada     Diseñadora     2300
# 8     Pedro    42     Madrid        Técnico     2700
# 9     Sofía    34    Sevilla      Psicóloga     2600
# 10   Andrés    28     Málaga      Enfermero     2550
# 11  Valeria    30     Toledo     Periodista     2400
# 12    Tomás    40       Vigo           Chef     2750
# 13  Daniela    27     Murcia    Veterinaria     2450
# 14     Raúl    37  Salamanca  Administrador     2900
# 15  Natalia    33       León       Analista     2650
```

Existen muchas formas de acceder a los datos, todo depende del propósito que tenemos con esos datos.

Podemos usar los `[]` para seleccionar una columna (como vimos anteriormente) o podemos también seleccionar las columnas en cierto intervalo:
```python
df['Nombre']
# Como habíamos mencionado, esto es un Series
# 1         Ana
# 2        Luis
# 3      Carlos
# 4       Marta
# 5       Elena
# 6       Jorge
# 7       Lucía
# 8       Pedro
# 9       Sofía
# 10     Andrés
# 11    Valeria
# 12      Tomás
# 13    Daniela
# 14       Raúl
# 15    Natalia
# Name: Nombre, dtype: object

# También podemos poner varias filas, agrupandolas, por ejemplo df[['Nombre', 'Edad']]

df[3:7]
#   Nombre  Edad    Ciudad   Profesión  Salario
# 4  Marta    29  Valencia     Abogada     2600
# 5  Elena    31    Bilbao   Contadora     2500
# 6  Jorge    38  Zaragoza  Arquitecto     3200
# 7  Lucía    26   Granada  Diseñadora     2300
```

También podemos acceder a partes entradas exactas por medio de `.loc`:
```python
df.loc[6]
# Nombre            Jorge
# Edad                 38
# Ciudad         Zaragoza
# Profesión    Arquitecto
# Salario            3200
# Name: 6, dtype: object

df.loc[:, ['Nombre', 'Edad']]
# equivalente a df[['Nombre', 'Edad']]

df.loc[3:5, ['Nombre', 'Edad']]
#    Nombre  Edad
# 3  Carlos    45
# 4   Marta    29
# 5   Elena    31

# También un valor específico, de un dato específico
df.loc[4, 'Nombre']
# 'Marta'
```

Como podemos ver, en el ejemplo anterior hemos seleccionado los datos de acuerdo a sus etiquetas. Por ejemplo, la columa `'Nombre'` y demás. Pero también podemos hacerlo por medio de su posición, es decir, acceder como si el DataFrame fuera una matriz de NumPy. Esto por medio de `.iloc`:
```python
df.iloc[:, 0]
# df['Nombre']

df.iloc[2:7, :]
# df.iloc[3:7]

df.iloc[5]
# df.loc[6]

df.iloc[:, 0:2]
# df.loc[:, ['Nombre', 'Edad']]

df.iloc[2:5, 0:2]
# df.loc[3:5, ['Nombre', 'Edad']]

df.iloc[3, 0]
# df.loc[4, 'Nombre']
```

Otra forma muy útil para acceder o selecionar datos es por medio de condiciones. Esto funciona de manera similar a como accedemos a por medio de condiciones a los `np.array()`.
```python
df[df['Edad'] < 30]
#      Nombre  Edad    Ciudad    Profesión  Salario
# 1       Ana    23    Madrid    Ingeniera     2400
# 4     Marta    29  Valencia      Abogada     2600
# 7     Lucía    26   Granada   Diseñadora     2300
# 10   Andrés    28    Málaga    Enfermero     2550
# 13  Daniela    27    Murcia  Veterinaria     2450

# También funciona con str
print(df[df['Profesión'].isin(['Analista', 'Arquitecto', 'Doctor'])])
#      Nombre  Edad    Ciudad   Profesión  Salario
# 2      Luis    35   Sevilla      Doctor     3000
# 6     Jorge    38  Zaragoza  Arquitecto     3200
# 15  Natalia    33      León    Analista     2650
```

Una de las aplicaciones con las que podemos aplicar esto es por medio de la reasignación. Es decir, por ejemplo, cambiar los valores de algo en cierto rango.
```python
df0 = df.copy()
df0.loc[(df0['Edad'] >= 40), 'Salario'] = 10000
df0
#      Nombre  Edad     Ciudad      Profesión  Salario
# 1       Ana    23     Madrid      Ingeniera     2400
# 2      Luis    35    Sevilla         Doctor     3000
# 3    Carlos    45  Barcelona       Profesor    10000
# 4     Marta    29   Valencia        Abogada     2600
# 5     Elena    31     Bilbao      Contadora     2500
# 6     Jorge    38   Zaragoza     Arquitecto     3200
# 7     Lucía    26    Granada     Diseñadora     2300
# 8     Pedro    42     Madrid        Técnico    10000
# 9     Sofía    34    Sevilla      Psicóloga     2600
# 10   Andrés    28     Málaga      Enfermero     2550
# 11  Valeria    30     Toledo     Periodista     2400
# 12    Tomás    40       Vigo           Chef    10000
# 13  Daniela    27     Murcia    Veterinaria     2450
# 14     Raúl    37  Salamanca  Administrador     2900
# 15  Natalia    33       León       Analista     2650
```

# Limpieza de datos

En muchas ocasiones se puede llegar a dar la situación que hagan falta datos y sean reemplazados con `NaN`, `None` o `np.nan`. Este tipo de datos no nos sirven, y lo mejor sería deshacernos de ellos, reemplazarlos o al menos encontrarlos con facilidad.

Bueno, existen muchas formas para eso. Supongamos que tenemos el siguiente DataFrame:
```python
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro'],
    'Edad': [25, np.nan, 35, 40, np.nan],
    'Salario': [3000, 4500, np.nan, 5000, 4200],
    'Ciudad': ['Tegucigalpa', 'San Pedro Sula', 'La Ceiba', np.nan, 'Choluteca']
}

df = pd.DataFrame(datos)

#    Nombre  Edad  Salario          Ciudad
# 0     Ana  25.0   3000.0     Tegucigalpa
# 1    Luis   NaN   4500.0  San Pedro Sula
# 2  Carlos  35.0      NaN        La Ceiba
# 3   Marta  40.0   5000.0             NaN
# 4   Pedro   NaN   4200.0       Choluteca
```

Podemos ver como hay valores `NaN`, lo que significa que están nulos. Una forma de deshacernos de ellos en simplemente eliminar la entrada que tiene esa clase de datos. Lo podemos lograr usando `.dropna()`:
```python
df.dropna(how='any')
#   Nombre  Edad  Salario       Ciudad
# 0    Ana  25.0   3000.0  Tegucigalpa
```

Es una forma, pero así se pierde información. Una mejor manera es reemplazándolos con `.fillna()`:
```python
 df.fillna(value=0)
#    Nombre  Edad  Salario          Ciudad
# 0     Ana  25.0   3000.0     Tegucigalpa
# 1    Luis   0.0   4500.0  San Pedro Sula
# 2  Carlos  35.0      0.0        La Ceiba
# 3   Marta  40.0   5000.0               0
# 4   Pedro   0.0   4200.0       Choluteca
``` 

Mejor, aunque con `Ciudad` no tiene mucho sentido. Una alternativa es irlo haciendo por columas:
```python
# Hacemos que los valores nulos numericos sean 0
df[['Edad', 'Salario']] = df[['Edad', 'Salario']].fillna(value=0)
# Y los valores nulos de Ciudades sean 'No Aplica'
df['Ciudad'] = df['Ciudad'].fillna(value='No Aplica')
#    Nombre  Edad  Salario          Ciudad
# 0     Ana  25.0   3000.0     Tegucigalpa
# 1    Luis   0.0   4500.0  San Pedro Sula
# 2  Carlos  35.0      0.0        La Ceiba
# 3   Marta  40.0   5000.0       No Aplica
# 4   Pedro   0.0   4200.0       Choluteca
```

Y otra forma de hacerlo es analizar si todos los valores son, o no, nulos. Esto por medio de `.isna()`:
```python
df.isna()
#    Nombre   Edad  Salario  Ciudad
# 0   False  False    False   False
# 1   False   True    False   False
# 2   False  False     True   False
# 3   False  False    False    True
# 4   False   True    False   False
```
De esta forma obtenemos el valor boolenao correspondiente. `True` si es `NaN` y `False` si no.

# Transformación de datos

Vamos a usar este DataFrame:
```python
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'María', 'Pedro'],
    'Edad': [23, 35, 45, 29, 31],
    'Salario': [2500, 3200, 4000, 2800, 3500]
}

df = pd.DataFrame(datos)

#    Nombre  Edad  Salario
# 0     Ana    23     2500
# 1    Luis    35     3200
# 2  Carlos    45     4000
# 3   María    29     2800
# 4   Pedro    31     3500
```

Podemos usar funciones que nosotros definimos para poder manipular o entender mejor nuestros datos. Por ejemplo, habíamos visto anteriormente como calcular la media aritmética de los datos numéricos con `.mean()`, pero, ¿Y si queremos la desviación estándar? ¿O algo distinto? Podemos lograrlo con `.agg()`:
```python
df[['Edad', 'Salario']].agg(lambda x: np.mean(x))
# equivalente a df[['Edad', 'Salario']].mean()

df[['Edad', 'Salario']].agg(lambda x: np.std(x))
# desviación estándar
```

De esta forma, podemos pasar como argumento una función (normalmente una `lambda`) que nos ayude a calcular cualquier dato que deseemos.

Al igual que podemos aplicar cierta función a los datos que tenemos haciendo uso de `.transform()`. Por ejemplo:
```python
# podemos pasar todos los nombres a mayusculas
df['Nombre'] = df['Nombre'].transform(lambda x: x.upper())

# cambiar el salario a la mitad
df['Salario'] = df['Salario'].transform(lambda x: x * (.5))
```
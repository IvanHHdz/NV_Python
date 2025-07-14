# Ciencia de datos (_Data Science_)
La ciencia de datos es el proceso mediante el cual se recolectan, limpian, analizan e interpretan datos para extraer de ellos información útil. Este campo se sustenta en tres pilares fundamentales: la programación, las matemáticas y el conocimiento de un área específica.

¿Qué significa esto? Que la ciencia de datos busca aplicar herramientas de programación y técnicas matemáticas (como la estadística, el álgebra lineal o el aprendizaje automático) para llegar a conclusiones relevantes basadas en grandes cantidades de información. Siendo también parte del proceso el recolectar y limpiar estos datos.

¿Para qué puede servir? Tiene muchas utilidades, todo depende del tercer componente: el conocimiento de un área específica. Por ejemplo, podemos aplicarlo a la economía y tenemos formas de analizar el mercado para mejorar las ganancias o analizar un negocio para tomar las mejores decisiones posibles; o en meteorología, para poder hacer pronósticos climáticos; o incluso esos tan sonados _"algoritmos"_ de las redes sociales, no son más que formas aplicadas y complejas de ciencia de datos.

# Librerías

Como habíamos mencionado, uno de los pilares de la ciencia de datos es precisamente la programación. Usualmente se utiliza Python o R. En cualquier caso, Python suele ser el más usado por su facilidad y versatilidad.

En Python, algunas de las librerías más usadas en este ámbito son:
- `numpy` permitiendo mayor eficiencia y facilidad de operaciones de álgebra lineal.
- `pandas` facilitando la limpieza, transformación y exploración de los datos.
- `matplotlib` ayudando a la creación de gráficos.
- `seaborn` mejorando y facilitando el uso de gráficas.
- `scikit-learn` para machine learning.
- `polars` similar a `pandas` pero más eficiente.
- `scipy` mayor profundidad matemática.

Nosotros nos centraremos por ahora en las primeras tres.

# Jupyter Notebooks

Jupyter permite escribir código, texto, fórmulas y gráficos en el mismo documento. Siendo ideal para ciencia de datos.

Si lo tenemos intalado, podemos iniciarlo usando:
```shell
jupyter notebook
```

Para instalarlo, podemos hacerlo con `pip` o `conda`:
```shell
pip install jupyter     # con pip
conda install jupyter   # con conda
```

Al iniciarlo, nos abrirá nuestro navegador, a la interfaz de Jupyter.

Si instalamos Anaconda, ya lo tendremos instalado pues lo instala por defecto. Si usamos VS Code podemos usar los Jupyter Notebooks al abrirlos directamente instalando la extensión oficial.

Estos resultan muy útiles por incluir la posibilidad de escribir código (en Python) y también escribir texto (con [MarkDown](../2.4%20-%20Extra/extra.md)).

# Flujo de trabajo
Normalmente, seguiremos un esquema simple para analizar datos:
1. Recolectar los datos
2. Limpiar los datos 
3. Analizar los datos
4. Vizualizar los datos
5. Sacar conclusiones

# Formatos comunes

Formatos de datos más usados:

| Formato    | Uso                              
| ---------- | -------------------------------- |
| `.csv`     | Texto separado por comas         |
| `.xlsx`    | Excel                            |
| `.json`    | Datos estructurados web/API      |
| `.parquet` | Datos comprimidos eficientemente |
| `SQL`      | Bases de datos SQL               |
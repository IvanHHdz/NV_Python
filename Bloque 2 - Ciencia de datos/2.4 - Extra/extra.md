# Markdown
Markdown es un lenguaje de marcado ligero diseñado para poder escribir texto con formato de forma sencilla y legible en texto plano.

Su propósito es que puedas crear documentos con estilos básicos (como encabezados, listas, negritas, enlaces, etc.) sin necesidad de usar herramientas complejas o escribir código HTML.

Resulta muy útil por su facilidad de uso, pues no posee reglas complejas como otros lenguajes para escritura de texto como $\LaTeX$ o <b>HTML</b>. Incluso permitiendo escribir en estos dentro del propio Markdown.

Es más, todo este curso está escrito haciendo uso de Markdown, por su facilidad.

De manera resumida, estas son las reglas de Markdown:


### Títulos

```markdown
# Título 1
## Título 2
### Título 3
#### Título 4
```

### Estilos de texto

```markdown
**negrita**
*itálica*
~~tachado~~
`código en línea`
```

### Listas

* Lista no enumerada:

```markdown
Lista 1:
- Elemento 1
- Elemento 2
  - Sub-elemento

Lista 2:
* Elemento 
    * Sub-elemento
```

* Lista numerada:

```markdown
1. Elemento uno
2. Elemento dos
```

### Enlaces e imágenes

* Enlace:

```markdown
[Texto del enlace](https://ejemplo.com)
```

* Imagen:

```markdown
![Texto alternativo](https://ejemplo.com/imagen.jpg)
```

### Citas

```markdown
> Esto es una cita.
>> Cita anidada.
```

### Código

* En línea:

```markdown
`código`
```

* Bloque de código:

<pre>
```python
def hola():
    print("Hola mundo")
```
</pre>



### Tablas

```markdown
| Columna 1 | Columna 2 |
|-----------|-----------|
| Dato 1    | Dato 2    |
| Dato 3    | Dato 4    |
```

### Separadores

```markdown
---
```

### HTML

Se puede insertar directamente en Markdown para formato avanzado:

```html
<div style="color:blue;">
  Texto azul con HTML
</div>

<table>
  <tr><th>Col1</th><th>Col2</th></tr>
  <tr><td>Dato1</td><td>Dato2</td></tr>
</table>
```

### $LaTeX$ 

Se puede usar directamente también, para insertar fórmulas y demás:

* Fórmulas en línea:

  ```latex
  $E=mc^2$
  ```
* Fórmulas en bloque:

  ```latex
  $$  
  \int_a^b f(x) dx = F(b) - F(a)  
  $$
  ```
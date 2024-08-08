# Django Editor

### SVG Panel

- ["Documentación"](https://panel.holoviz.org/reference/panes/SVG.html)

- ["Integración con Pyscript"](https://panel.holoviz.org/how_to/wasm/standalone.html)

- ["Configuración"](https://github.com/holoviz/panel/issues/4572)

- ["Panel SVG"](https://panel.holoviz.org/reference/panes/SVG.html)

- ["Revisar propiedades del SVG"](https://nikitahl.github.io/svg-2-code/)

- ["Agregar htlm al SVG"](https://jsfiddle.net/or6yt1L2/)

- ["Propiedades SVG"](https://www.w3schools.com/graphics/svg_text.asp)

- ["Iconos de panel"](https://tabler.io/icons)

- ["Información de atributos de widgets 1.3.8"](https://github.com/holoviz/panel/tree/v1.3.8/panel/widgets)

- ["Información de Componentes 1.4.4"](https://panel.holoviz.org/reference/index.html#component-gallery)

- ["Estilos panel"](https://panel.holoviz.org/explanation/styling/design.html)

- ["Panel templates"](https://panel.holoviz.org/reference/templates/Bootstrap.html)

### Agregar Elemntos de html a SVG

```
    <foreignObject x="0" y="0"  width="{width}" height="{height}">
        <body xmlns="http://www.w3.org/1999/xhtml">
            <div xmlns="http://www.w3.org/1999/xhtml" class="container-text">
                <p class="text">{text}<p>
             </div>
        </body>
    </foreignObject>
    
.container-text {
    display: table;
    font-size: 12px;
    width: 500px;
    height: 200px;
}

.text {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}

```

# Versiones Compatibles de PyScript con Panel

- 2024.7.1

Esta versión se siente mas lenta al cargar la interfaz. Ademas de incorporar una serie
de validaciones mas en cuanto a codigo pycript que anteriores versiones

- 2024.2.1

Esta es la versión mas rapida que las nuevas. Panel no funciona con las versiones 2023 de pyscript

# Versiones No funcionables en PyScript

- Panel 1.4.4 & Bokeh 3.4.1
- Panel 1.4.3 & Bokeh 3.4.1
- Panel 1.4.2 & Bokeh 3.4.1
- Panel 1.4.1 & Bokeh 3.4.0
- Panel 1.4.0 & Bokeh 3.4.0

["Url de pruebas"](https://cdn.holoviz.org/panel/1.4.4/dist/wheels/bokeh-3.4.1-py3-none-any.whl)
Mediante la url probaremos las versiones compatibles cambiando los numeros de versión. Si se descarga
es una version utilizable.

# Versiones funcionables en pyscript

["Documentación Versiones Panel"](https://panel.holoviz.org/about/releases.html)
["Documentación Versiones Kokeh"](https://docs.bokeh.org/en/latest/docs/releases.html)

### Panel 1.3.8

["Repositorio"](https://github.com/holoviz/panel/releases/tag/v1.3.8)

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.3.3.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.3.3.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.3.3.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.3.8/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.3.8/dist/wheels/bokeh-3.3.3-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.3.8/dist/wheels/panel-1.3.8-py3-none-any.whl",
    ]
```

### Panel 1.3.7

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.3.3.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.3.3.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.3.3.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.3.7/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.3.7/dist/wheels/bokeh-3.3.3-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.3.7/dist/wheels/panel-1.3.7-py3-none-any.whl",
    ]
```

### Panel 1.3.5

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.3.2.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.3.2.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.3.2.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.3.5/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.3.5/dist/wheels/bokeh-3.3.2-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.3.5/dist/wheels/panel-1.3.5-py3-none-any.whl",
    ]
```

### Panel 1.3.4

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.3.1.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.3.1.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.3.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.3.4/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.3.4/dist/wheels/bokeh-3.3.1-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.3.4/dist/wheels/panel-1.3.4-py3-none-any.whl",
    ]
```

### Panel 1.3.2

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.3.1.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.3.1.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.3.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.3.2/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.3.2/dist/wheels/bokeh-3.3.1-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.3.2/dist/wheels/panel-1.3.2-py3-none-any.whl",
    ]
```

### Panel 1.3.1

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.3.0.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.3.0.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.3.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.3.1/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.3.1/dist/wheels/bokeh-3.3.0-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.3.1/dist/wheels/panel-1.3.1-py3-none-any.whl",
    ]
```

### Panel 1.3.0

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.3.0.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.3.0.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.3.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.3.0/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.3.0/dist/wheels/bokeh-3.3.0-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.3.0/dist/wheels/panel-1.3.0-py3-none-any.whl",
    ]
```

### Panel 1.2.3

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.2.2.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.2.2.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.2.2.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.2.3/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.2.3/dist/wheels/bokeh-3.2.2-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.2.3/dist/wheels/panel-1.2.3-py3-none-any.whl",
    ]
```

### Panel 1.2.2

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.2.2.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.2.2.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.2.2.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.2.2/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.2.2/dist/wheels/bokeh-3.2.2-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.2.2/dist/wheels/panel-1.2.2-py3-none-any.whl",
    ]
```

### Panel 1.2.1

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.2.1.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.2.1.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.2.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.2.1/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.2.1/dist/wheels/bokeh-3.2.1-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.2.1/dist/wheels/panel-1.2.1-py3-none-any.whl",
    ]
```

### Panel 1.2.0

Esta versión cuando se crean elementos de interfaz, agrega clases y usa solo los div necesarios
facilitando mas personalizar los elementos. Ademas de ser una versión de panel intermedia.

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-3.2.0.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.2.0.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.2.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@holoviz/panel@1.2.0/dist/panel.min.js"></script>
```

- pyscript.toml

``` 
    packages = [
        "https://cdn.holoviz.org/panel/1.2.0/dist/wheels/bokeh-3.2.0-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/1.2.0/dist/wheels/panel-1.2.0-py3-none-any.whl",
    ]
```

### Panel 0.14.4

Esta versión cuando se crean elementos de interfaz, agrega css en linea ademas de muchos div que
dificultan personalizar los elementos. Ademas de ser una versión de panel muy antigua.

- head, index.html

```
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.3.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-2.4.3.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-2.4.3.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@holoviz/panel@0.14.4/dist/panel.min.js"></script>
```

- pyscript.toml

```
    #packages = [
        "https://cdn.holoviz.org/panel/0.14.4/dist/wheels/bokeh-2.4.3-py3-none-any.whl",
        "https://cdn.holoviz.org/panel/0.14.4/dist/wheels/panel-0.14.4-py3-none-any.whl",
    ]
```

### Elementos utilizados en Editor

- ["Iconos"](https://tabler.io/icons)
- ["Tabs"](https://panel.holoviz.org/reference/layouts/Tabs.html)
- ["FileDownload"](https://panel.holoviz.org/reference/widgets/FileDownload.html)
- ["Pane SVG"](https://panel.holoviz.org/reference/panes/SVG.html)
- ["ColorPicker"](https://panel.holoviz.org/reference/widgets/ColorPicker.html)
- ["IntSlider"](https://panel.holoviz.org/reference/widgets/IntSlider.html)
- ["TextInput"](https://panel.holoviz.org/reference/widgets/TextInput.html)
- ["Row"](https://panel.holoviz.org/reference/layouts/Row.html)
- ["Column"](https://panel.holoviz.org/reference/layouts/Column.html)
- ["Pane HTML"](https://panel.holoviz.org/reference/panes/HTML.html)

```
    <polygon points="100,10 150,190 50,190" fill="red" stroke="green" stroke-width="3" opacity="0.5" />
    <rect width="150" height="150" x="10" y="10" rx="20" ry="20" fill="red" stroke="green" stroke-width="3" opacity="0.5" />
    <circle r="45" cx="50" cy="50" fill="red" stroke="green" stroke-width="3" opacity="0.5" />
    <ellipse  rx="100" ry="50" cx="120" cy="80" fill="red" stroke="green" stroke-width="3" opacity="0.5" />
    
    #  Nota!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #  opcion para selecionar una figura, crear un boton cada que agrego una figura
    # luego agregar los botones al layout
    # debe funcionar de forma dinamica ya que al inicio no hay figuras
    # es decir cada que agrego una figura se crea un boton con ese boton
    # agrego la figura a current_shapes el boton tiene el nombre del id de la figura
    # cuando doy click en el boton cargo un subpael con las entradas de la figura

    
    def select_svg_element_by_id(element_id):
    try:
        element = document.getElementById(element_id)
        if element is not None:
            console.log(f"Element with id {element_id} selected.")
        else:
            console.error(f"No element found with id {element_id}.")
    except Exception as e:
        console.error(f"Error selecting element: {e}")

select_button = pn.widgets.Button(name='Select SVG Element', button_type='primary')
def on_select_click(event):
    #select_svg_element_by_id("app")
    #select_svg_element_by_id("f_0")
    select_svg_element_by_id("f_0")

select_button.on_click(on_select_click)

# agregar id
# problema atributos -
#
#
#
# 
```

#### Modos de dimensionamiento disponibles:
La propiedad sizing_mode en Panel controla cómo se dimensiona un componente en función del espacio disponible en su contenedor. El valor stretch_width es uno de los modos de dimensionamiento disponibles. Aquí está una explicación detallada:

- sizing_mode

Cuando se establece sizing_mode="stretch_width", el componente ajusta su ancho para llenar todo el espacio horizontal disponible en su contenedor padre, mientras que la altura se mantiene fija o determinada por el contenido del componente.

```
sizing_mode="stretch_width"
```

```
fixed: El componente mantiene un tamaño fijo en ambos ejes.
stretch_width: El componente se expande para llenar todo el ancho disponible, pero su altura se mantiene fija.
stretch_height: El componente se expande para llenar toda la altura disponible, pero su ancho se mantiene fijo.
stretch_both: El componente se expande para llenar tanto el ancho como la altura disponibles.
scale_width: El componente escala su ancho proporcionalmente al espacio disponible, manteniendo una relación de aspecto fija.
scale_height: El componente escala su altura proporcionalmente al espacio disponible, manteniendo una relación de aspecto fija.
scale_both: El componente escala tanto su ancho como su altura proporcionalmente al espacio disponible, manteniendo una relación de aspecto fija.
```
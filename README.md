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


###  Panel 1.3.8

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

###  Panel 1.3.7

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

###  Panel 1.3.5

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

###  Panel 1.3.4

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

###  Panel 1.3.2

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

###  Panel 1.3.1

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

###  Panel 1.3.0

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

###  Panel 1.2.3

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

###  Panel 1.2.2

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

###  Panel 1.2.1

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

###  Panel 1.2.0
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

###  Panel 0.14.4
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

import panel as pn

pn.extension()

button = pn.widgets.Button(icon="heart")


# Definir sliders para controlar el ancho y la altura
width_slider = pn.widgets.IntSlider(name='Width', start=100, end=500, step=10, value=500)
height_slider = pn.widgets.IntSlider(name='Height', start=100, end=500, step=10, value=500)
# Selección de color de fondo
color_picker = pn.widgets.ColorPicker(name='Background color', value='#ffffff', css_classes=['picker'])
# Campo de entrada para agregar texto al SVG
text_input = pn.widgets.TextInput(name='Text to Add', value='I love SVG!', max_length=250)

# Botón para actualizar el SVG con el texto
text_size = pn.widgets.IntSlider(name='Font size', start=8, end=24, step=1, value=12)
text_color = pn.widgets.ColorPicker(name='Text color', value='#000000', css_classes=['picker'])

# Nombres de los botones en un arreglo
button_data = [
    ["square", "square"],
    ["circle", "circle"],
    ["triangle", "triangle"],
    ["ellipse", "oval-vertical"],
]


# Función para ajustar el texto en múltiples líneas
def wrap_text(text, max_width, font_size):
    lines = []
    words = text.split(' ')
    current_line = ''

    for word in words:
        test_line = f'{current_line} {word}'.strip()
        # cualcular el tamaño de la linea con la fuente y el tamaño de la letra
        estimated_width = len(test_line) * font_size * 0.6
        if estimated_width > max_width:
            lines.append(current_line)
            current_line = word
        else:
            current_line = test_line

    if current_line:
        lines.append(current_line)

    return lines


# SVG base en blanco
def create_svg_base(width, height, color, text, font_size, text_color):
    # width - 10 es el margen a la derecha
    wrapped_text = wrap_text(text, width - 10, font_size)
    text_elements = ''.join(
        f'<tspan x="5" dy="{font_size + 5}" fill="{text_color}">{line}</tspan>'
        if i != 0 else f'<tspan x="5" dy="0" fill="{text_color}">{line}</tspan>'
        for i, line in enumerate(wrapped_text)
    )
    print(text)

    return f'''
        <svg id="drawing-svg" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
            <rect width="{width}" height="{height}" fill="{color}"/>
            <text x="5" y="15" font-size="{font_size}" fill="{text_color}">
                {text_elements}
            </text>
        </svg>
    '''


# Panel de dibujo que se actualiza con los sliders
@pn.depends(
    width_slider.param.value,
    height_slider.param.value,
    color_picker.param.value,
    text_input.param.value,
    text_size.param.value,
    text_color.param.value,
)
def create_drawing_panel(width, height, color, text, font_size, text_color):
    svg_content = create_svg_base(width, height, color, text, font_size, text_color)
    return pn.pane.HTML(f'<div class="panel">{svg_content}</div>', width=width, height=height, target="drawing-panel")


# Funciónes de botones
# def rectangle_click(event):
#     print("Botón rectangle presionado")
#
#
# def circle_click(event):
#     print("Botón circle presionado")
#
#
# def triangle_click(event):
#     print("Botón triangle presionado")


# Crear botones con dimensiones definidas
buttons = []
# for name, icon_html in button_data:
#     button = pn.pane.HTML(f'<button class="btn-figure btn btn-sm btn-primary" style="width:30px; height:30px;" id="{name}">{icon_html}</button>')
#     buttons.append(button)
# for name, icon in button_data:
#     button = pn.widgets.ButtonIcon(icon={icon}, size="1em", description={name})
#     buttons.append(button)

# Asignar funciones de clic a cada botón
# buttons[0].on_click(rectangle_click)
# buttons[1].on_click(circle_click)
# buttons[2].on_click(triangle_click)

# Crear una caja flexible para los botones
#box_buttons = pn.FlexBox(*buttons, flex_direction='row', height=50, css_classes=['button-row'])

# Configurar el sidebar
sidebar = pn.Column(
    width_slider,
    height_slider,
    color_picker,
    text_input,
    text_size,
    text_color,
    button,
    css_classes=['sidebar'],
)

panel = pn.Column(create_drawing_panel, css_classes=['panel'])


# sidebar.servable(target='sidebar-panel')
panel.servable(target='drawing-panel')


layout_sidebar = pn.Row(sidebar)
layout_panel = pn.Row(panel)


# panel = pn.Column(create_drawing_panel)

# Configurar layout principal
# layout_sidebar = pn.GridBox(sidebar, ncols=3)
# layout_panel = pn.GridBox(panel, ncols=9)

# Servir el layout
layout = pn.Row(layout_sidebar, layout_panel, css_classes=['layout'])
layout.servable(target='output')





# Crear el area de dibujo SVG base, editable
@pn.depends(
    width_slider.param.value,
    height_slider.param.value,
    color_picker.param.value,
    text_input.param.value,
    text_size.param.value,
    text_color.param.value,
)
def create_drawing_panel(width, height, color, text, font_size, text_color):
    svg_content = create_svg_base(width, height, color, text, font_size, text_color)
    return pn.pane.HTML(f'<div id="panel">{svg_content}</div>', width=width, height=height, styles=styles_panel)


```
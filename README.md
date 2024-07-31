# Django Editor

### SVG Panel

- ["Documentación"](https://panel.holoviz.org/reference/panes/SVG.html)

-["Integración con Pyscript"](https://panel.holoviz.org/how_to/wasm/standalone.html)

- ["Configuración"](https://github.com/holoviz/panel/issues/4572)

- ["Panel SVG"](https://panel.holoviz.org/reference/panes/SVG.html)

- ["Revisar propiedades del SVG"](https://nikitahl.github.io/svg-2-code/)

- ["Agregar htlm al SVG"](https://jsfiddle.net/or6yt1L2/)

- ["Propiedades SVG"](https://www.w3schools.com/graphics/svg_text.asp)

- ["Iconos de panel"](https://tabler.io/icons)

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
# Versiones Compatibles de pyscript con panel

- 2024.2.1

Esta es la version mas rapida que las nuevas. Panel no funciona con las versiones 2023 de pyscript

# Versiones No funcionables en pyscript

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
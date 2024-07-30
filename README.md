# Django Editor

### SVG Panel

- ["Documentación"](https://panel.holoviz.org/reference/panes/SVG.html)
- 
- ["Configuración"](https://github.com/holoviz/panel/issues/4572)

- ["Panel SVG"](https://panel.holoviz.org/reference/panes/SVG.html)

- ["Revisar propiedades del SVG"](https://nikitahl.github.io/svg-2-code/)

- ["Agregar htlm al SVG"](https://jsfiddle.net/or6yt1L2/)

- ["Propiedades SVG"](https://www.w3schools.com/graphics/svg_text.asp)

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
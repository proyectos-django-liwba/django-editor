import panel as pn

pn.extension()

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
def update_drawing_panel(width, height, color, text, font_size, text_color):
    svg_content = create_svg_base(width, height, color, text, font_size, text_color)
    return pn.pane.HTML(f'<div class="panel">{svg_content}</div>', width=width, height=height)


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
    css_classes=['sidebar']
)

# Configurar layout principal
layout = pn.Row(
    sidebar,
    update_drawing_panel
)

# Servir el layout
layout.servable(target='control-panel')

import panel as pn
from pyscript import display

pn.extension()

# Definir sliders para controlar el ancho y la altura
width_slider = pn.widgets.IntSlider(name='Width', start=100, end=500, step=10, value=500)
height_slider = pn.widgets.IntSlider(name='Height', start=100, end=500, step=10, value=500)

# SVG base en blanco
def create_svg_base(width, height):
    return f'''
    <svg id="drawing-svg" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
      <rect width="100%" height="{height}" fill="white"/>
    </svg>
    '''

# Panel de dibujo que se actualiza con los sliders
@pn.depends(width_slider.param.value, height_slider.param.value)
def update_drawing_panel(width, height):
    svg_content = create_svg_base(width, height)
    return pn.pane.HTML(f'<div class="panel">{svg_content}</div>', width=width, height=height)


# Configurar el sidebar
sidebar = pn.Column(
    width_slider,
    height_slider,
    css_classes=['sidebar']
)

# Configurar layout principal
layout = pn.Row(
    sidebar,
    update_drawing_panel
)

# Servir el layout
layout.servable(target='control-panel')

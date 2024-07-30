from pyscript import display
import panel as pn
import numpy as np

pn.extension()

# Definir sliders para controlar el ancho y la altura
width_slider = pn.widgets.IntSlider(name='Width', start=100, end=500, step=10, value=500)
height_slider = pn.widgets.IntSlider(name='Height', start=100, end=500, step=10, value=500)


# Panel de dibujo
@pn.depends(width_slider.param.value, height_slider.param.value)
def update_drawing_panel(width, height):
    # Crear el panel de dibujo con el tamaño especificado
    return pn.pane.HTML(f'<div style="width:{width}px; height:{height}px;" class="panel"></div>')


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
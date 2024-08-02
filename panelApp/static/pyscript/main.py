# ...................................................................
# Clases para agregar figuras y texto al SVG
# ...................................................................
from abc import ABC, abstractmethod

class FigureFactory:
    @staticmethod
    def create_element(element_type, *args, **kwargs):
        if element_type == 'rect':
            return FigureRect(*args, **kwargs)
        elif element_type == 'circle':
            return FigureCircle(*args, **kwargs)
        elif element_type == 'triangle':
            return FigureTriangle(*args, **kwargs)
        elif element_type == 'ellipse':
            return FigureEllipse(*args, **kwargs)
        else:
            raise ValueError(f"Unknown element type: {element_type}")


class FigureInterface(ABC):
    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def get_svg(self):
        pass


class FigureRect(FigureInterface):
    def __init__(self, width=150, height=150, x=10, y=10, rx=20, ry=20, fill='red', stroke='green', stroke_width=3, opacity=0.5):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.opacity = opacity

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_svg(self):
        return f'<rect width="{self.width}" height="{self.height}" x="{self.x}" y="{self.y}" rx="{self.rx}" ry="{self.ry}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" opacity="{self.opacity}" />'


class FigureCircle(FigureInterface):
    def __init__(self, r=45, cx=50, cy=50, fill='red', stroke='green', stroke_width=3, opacity=0.5):
        self.r = r
        self.cx = cx
        self.cy = cy
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.opacity = opacity

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_svg(self):
        return f'<circle r="{self.r}" cx="{self.cx}" cy="{self.cy}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" opacity="{self.opacity}" />'


class FigureTriangle(FigureInterface):
    def __init__(self, points="100,10 150,190 50,190", fill='red', stroke='green', stroke_width=3, opacity=0.5):
        self.points = points
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.opacity = opacity

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_svg(self):
        return f'<polygon points="{self.points}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" opacity="{self.opacity}" />'


class FigureEllipse(FigureInterface):
    def __init__(self, rx=100, ry=50, cx=120, cy=80, fill='red', stroke='green', stroke_width=3, opacity=0.5):
        self.rx = rx
        self.ry = ry
        self.cx = cx
        self.cy = cy
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.opacity = opacity

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def get_svg(self):
        return f'<ellipse rx="{self.rx}" ry="{self.ry}" cx="{self.cx}" cy="{self.cy}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" opacity="{self.opacity}" />'

# ...................................................................
# Clase para controlar los parámetros adicionales del SVG
# ...................................................................
import param
class SVGParams(param.Parameterized):
    additional_shapes = param.List(default=[], item_type=FigureInterface)


# ========================================================================================
# Main
# ========================================================================================

from io import StringIO
import panel as pn


#from figures import FigureFactory
#from figures import FigureFactory
# Factories para crear figuras


# Crear un rectángulo con valores por defecto
# rect = factory.create_element('rect')
# print(rect.get_svg())

# Crear un círculo con valores por defecto
# circle = factory.create_element('circle')
# print(circle.get_svg())

# Crear un triángulo con valores por defecto
# triangle = factory.create_element('triangle')
# print(triangle.get_svg())

pn.extension()

# ========================================================================================
# Estilos elementos de interfaz
# ========================================================================================
styles_panel = {
    "border": "1px solid  #a6acaf",
    "background": "#f2f3f4",
    "border-radius": "5px",
    "box-shadow": "rgba(0, 0, 0, 0.35) 0px 5px 15px",
    "display": "flex",
    "justify-content": "center",
    "align-self": "center",
    "box-sizing": "border-box"
}

styles_sidebar = {
    "background-color": "#f0f0f0",
    "padding": "10px",
    "border-radius": "8px",
    "max-width": "300px",
    "box-shadow": "rgba(0, 0, 0, 0.35) 0px 5px 15px",
    "box-sizing": "border-box"
}


# Nombres de los botones figuras
button_data = [
    ["square", "square"],
    ["circle", "circle"],
    ["triangle", "triangle"],
    ["ellipse", "oval-vertical"],
]

# additional_shapes = [
#     '<rect width="150" height="150" x="10" y="10" rx="20" ry="20" fill="red" stroke="green" stroke-width="3" opacity="0.5" />',
#     '<circle r="45" cx="50" cy="50" fill="red" stroke="green" stroke-width="3" opacity="0.5" />',
#     '<polygon points="100,10 150,190 50,190" fill="red" stroke="green" stroke-width="3" opacity="0.5" />',
#     '<ellipse  rx="100" ry="50" cx="120" cy="80" fill="red" stroke="green" stroke-width="3" opacity="0.5" />'
# ]

# ========================================================================================
# Elementos de contenido
# ========================================================================================

# Definir sliders para controlar el ancho y la altura
width_slider = pn.widgets.IntSlider(name='Width', start=100, end=500, step=10, value=500, width=240)
height_slider = pn.widgets.IntSlider(name='Height', start=100, end=500, step=10, value=500, width=240)
# Selección de color de fondo
color_picker = pn.widgets.ColorPicker(name='Background color', value='#ffffff')
# Campo de entrada para agregar texto al SVG
text_input = pn.widgets.TextInput(name='Text to Add', value='I love SVG!', max_length=250, width=240)
# Botón para actualizar el SVG con el texto
text_size = pn.widgets.IntSlider(name='Font size', start=8, end=24, step=1, value=12, width=240)
text_color_picker = pn.widgets.ColorPicker(name='Text color', value='#000000')

# ========================================================================================
# Variable Globales
# ========================================================================================

# contenido del SVG
svg_content = ""

# Elementos adicionales del SVG
svg_params = SVGParams()

# ========================================================================================
# Funciones
# ========================================================================================

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
def create_svg_base(width, height, color, text, font_size, text_color, shape):
    # width - 10 es el margen a la derecha
    wrapped_text = wrap_text(text, width - 10, font_size)
    text_elements = ''.join(
        f'<tspan x="5" dy="{font_size + 5}" fill="{text_color}">{line}</tspan>'
        if i != 0 else f'<tspan x="5" dy="0" fill="{text_color}">{line}</tspan>'
        for i, line in enumerate(wrapped_text)
    )

    # Crear un string con las figuras adicionales
    figures_svg = ""
    for figure in shape:
        figures_svg += figure.get_svg() + "\n"

    print(figures_svg)

    return f'''<svg id="drawing-svg" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
                    <rect width="{width}" height="{height}" fill="{color}"/>
                    <text x="5" y="15" font-size="{font_size}" fill="{text_color}">
                        {text_elements}
                    </text>
                    {figures_svg}
                </svg>'''

# Funcion que crea el panel y actualiza el SVG
@pn.depends(
    width_slider.param.value,
    height_slider.param.value,
    color_picker.param.value,
    text_input.param.value,
    text_size.param.value,
    text_color_picker.param.value,
    svg_params.param.additional_shapes
)
def create_panel(width, height, color, text, font_size, text_color, shape):
    global svg_content
    svg_content = create_svg_base(width, height, color, text, font_size, text_color, shape)
    return pn.pane.SVG(
        svg_content,
        width=width,
        height=height,
    )


# Función para descargar el SVG
def get_svg_download():
    global svg_content
    sio = StringIO()
    sio.write(svg_content)
    sio.seek(0)
    return sio

# Función para agregar figuras al SVG
def add_figure(event):
    button = event.obj
    factory = FigureFactory()

    # Crear la figura según el botón pulsado
    if button.icon == "square":
        figure = factory.create_element('rect')
    elif button.icon == "circle":
        figure = factory.create_element('circle')
    elif button.icon == "triangle":
        figure = factory.create_element('triangle')
    elif button.icon == "oval-vertical":
        figure = factory.create_element('ellipse')
    else:
        return

    # Agregar la figura a la lista y forzar actualización del parámetro
    svg_params.additional_shapes.append(figure)
    svg_params.param.trigger('additional_shapes')


# Crear menu de botones para agregar figuras
def create_button_panel(buttons):
    # crear botones
    button_widgets = [
        pn.widgets.Button(icon=icon, icon_size="14px", button_type="primary", width=35)
        for name, icon in buttons
    ]

    # agregar funciones
    for button in button_widgets:
        button.on_click(add_figure)

    # Returnar panel con botones
    return pn.Row(*button_widgets)






# ========================================================================================
# Configuraciones elementos de interfaz
# ========================================================================================

# Boton de descarga del SVG
download_svg = pn.widgets.FileDownload(
    callback=get_svg_download,
    icon='download',
    filename='Design.svg',
    button_type='success',
    embed=False, auto=True)

# Tab con las configuraciones del panel
settings_tab = pn.Column(
    width_slider,
    height_slider,
    color_picker,
    download_svg,
    name='Setting'
)

# Tab con las configuraciones del texto
text_tab = pn.Column(
    text_input,
    text_size,
    text_color_picker,
    name='Text'
)

# Tab con las configuraciones de las figuras
figures_tab = pn.Column(
create_button_panel(button_data),
    name='Figure')

# Tab con las configuraciones de los pictogramas
pictogram_tab = pn.Column(name='Pictogram')

# Panel principal con el SVG
panel = pn.Column(create_panel, styles=styles_panel)

# Panel con la barra lateral "Sidebar contiene los tabs"
sidebar = pn.Tabs(
    settings_tab,
    text_tab,
    figures_tab,
    pictogram_tab,
    styles=styles_sidebar,
)

# ========================================================================================
# Cargar el contenido en el HTML
# ========================================================================================

sidebar.servable(target='sidebar-panel')
panel.servable(target='drawing-panel')



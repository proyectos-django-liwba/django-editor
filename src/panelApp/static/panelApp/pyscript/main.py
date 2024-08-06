# dependencias
import xml.etree.ElementTree as ET
from io import StringIO

import panel as pn
import param

# archivos
import figures
import utils


# ...................................................................
# Clase para controlar los parámetros adicionales del SVG
# ...................................................................

# import param
class SVGParams(param.Parameterized):
    additional_shapes = param.List(default=[], item_type=figures.FigureInterface)
    current_shape = param.ObjectSelector(default=None, objects=[])
    svg_content = param.String(default="")

    def update_current_shape(self, shape_id):
        print(f'Updating current shape to {shape_id}')
        shape = next((shape for shape in self.additional_shapes if shape.id == shape_id), None)

        if shape:
            self.current_shape = shape
            self.param.current_shape.objects = self.additional_shapes
            print(f'Current shape: {self.current_shape.get_svg()}')

    def parse_svg_content(self, file_content):
        # Crear un árbol XML del contenido SVG
        tree = ET.ElementTree(ET.fromstring(file_content))
        root = tree.getroot()

        # Limpiar la lista de figuras adicionales
        self.additional_shapes = []

        print('Parsing SVG content...')
        print(root)

        # Iterar sobre los elementos SVG y recrear las figuras
        for elem in root:
            tag = elem.tag.split('}')[-1]  # Obtener la etiqueta sin el namespace
            print(tag)
            if tag == 'rect':

                figure = figures.FigureFactory.create_element('rect')
            elif tag == 'circle':

                figure = figures.FigureFactory.create_element('circle')
            elif tag == 'polygon':

                figure = figures.FigureFactory.create_element('triangle')
            elif tag == 'ellipse':

                figure = figures.FigureFactory.create_element('ellipse')
            else:
                continue

            print(figure.get_svg())
            self.additional_shapes.append(figure)

            print("Figuras ")
            for f in self.additional_shapes:
                print(f.get_svg())


# ========================================================================================
# Main
# ========================================================================================

pn.extension()

# ========================================================================================
# Elementos de contenido
# ========================================================================================

# Definir sliders para controlar el ancho y la altura
width_slider = pn.widgets.IntSlider(name='Width', start=100, end=500, step=10, value=500, width=240)
height_slider = pn.widgets.IntSlider(name='Height', start=100, end=500, step=10, value=500, width=240)
# Selección de color de fondo
color_picker = pn.widgets.ColorPicker(name='Background color', value='#ffffff')
# Campo de entrada para agregar texto al SVG
#text_input = pn.widgets.TextInput(name='Text to Add', value='I love SVG!', max_length=250, width=240)
text_input = pn.widgets.TextInput(name='Text to Add', value='', max_length=250, width=240)
# Botón para actualizar el SVG con el texto
text_size = pn.widgets.IntSlider(name='Font size', start=8, end=24, step=1, value=12, width=240)
text_color_picker = pn.widgets.ColorPicker(name='Text color', value='#000000')

file_input = pn.widgets.FileInput(accept='.svg', multiple=False, width=240)

# ========================================================================================
# Variable Globales
# ========================================================================================

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


# Función para añadir figuras al contenido SVG cargado
# def add_shapes_to_svg(svg_content, shapes):
#     figures_svg = "".join([figure.get_svg() for figure in shapes])
#     svg_content = svg_content.replace("</svg>", f"{figures_svg}\n</svg>")
#     return svg_content

# SVG base en blanco
def create_svg_base(width, height, color, text, font_size, text_color, shapes):
    # width - 10 es el margen a la derecha
    wrapped_text = wrap_text(text, width - 10, font_size)
    text_elements = ''.join(
        f'<tspan x="5" dy="{font_size + 5}" fill="{text_color}">{line}</tspan>'
        if i != 0 else f'<tspan x="5" dy="0" fill="{text_color}">{line}</tspan>'
        for i, line in enumerate(wrapped_text)
    )

    # factory = figures.FigureFactory()
    # if len(shapes) >= 0:
    #     figure_layout = factory.create_element("rect", id="f_0", x=0, y=0, width=width, height=height, fill=color, stroke='none', stroke_width=0)
    #     shapes.append(figure_layout)
    # Crear un string con las figuras adicionales
    figures_svg = ""
    for figure in shapes:
        figures_svg += figure.get_svg() + "\n"

    # print(figures_svg) <rect width="{width}" height="{height}" fill="{color}"/>

    return f'''<svg id="drawing-svg" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
                     {figures_svg}
                    <text x="5" y="15" font-size="{font_size}" fill="{text_color}">
                        {text_elements}
                    </text>
                   
                </svg>'''


# Funcion que crea el panel y actualiza el SVG
@pn.depends(
    width_slider.param.value,
    height_slider.param.value,
    color_picker.param.value,
    text_input.param.value,
    text_size.param.value,
    text_color_picker.param.value,
    svg_params.param.additional_shapes,
    svg_params.param.svg_content
)
def create_panel(width, height, color, text, font_size, text_color, shapes, svg_content):


    if not any(figure.id == "f_0" for figure in shapes):
        factory = figures.FigureFactory()
        figure_layout = factory.create_element("rect", id="f_0", x=0, y=0, width=width, height=height, fill=color, stroke='none', stroke_width=0)
        shapes.insert(0, figure_layout)

    # if not svg_content:
    #     svg_content = create_svg_base(width, height, color, text, font_size, text_color, shapes)
    # else:
    #     print('Updating SVG content...')
    #     svg_content = add_shapes_to_svg(svg_content, shapes)
    svg_content = create_svg_base(width, height, color, text, font_size, text_color, shapes)
    # return pn.pane.SVG(
    #     svg_content,
    #     width=width,
    #     height=height,
    # )
    return pn.pane.HTML(svg_content, width=width, height=height)


# Función para descargar el SVG
def get_svg_download():
    sio = StringIO()
    sio.write(svg_params.svg_content)
    sio.seek(0)
    return sio


def select_figure(event):
    shape_id = event.obj['id']
    svg_params.update_current_shape(shape_id)
    print(f'Selected shape ID: {shape_id}')


# Función para agregar figuras al SVG
def add_figure(event):
    button = event.obj
    factory = figures.FigureFactory()
    type_figure = ""

    # Crear la figura según el botón pulsado
    if button.icon == "square":
        type_figure = 'rect'
    elif button.icon == "circle":
        type_figure = 'circle'
    elif button.icon == "triangle":
        type_figure = 'triangle'
    elif button.icon == "oval-vertical":
        type_figure = 'ellipse'
    else:
        return

    id_figure = f'f_{len(svg_params.additional_shapes)}'
    figure = factory.create_element(type_figure, id=id_figure)
    print(id_figure)
    print(figure.get_svg())
    # Agregar la figura a la lista y forzar actualización del parámetro
    svg_params.additional_shapes.append(figure)
    svg_params.param.trigger('additional_shapes')
    svg_params.param.trigger('svg_content')

    svg_params.update_current_shape(id_figure)


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


def handle_file_upload(event):
    file_data = event.new
    # file_name = file_data.filename
    file_bytes = file_input.value
    # svg_params.svg_content = file_bytes.decode('utf-8')
    # svg_params.param.trigger('svg_content')
    # print(f"Nombre del archivo: {file_name}")
    svg_params.parse_svg_content(file_bytes.decode('utf-8'))
    svg_params.param.trigger('additional_shapes')
    print(f"Contenido del archivo (bytes): {file_bytes.decode('utf-8')}")


# Conectar la función de manejo de archivos al widget
file_input.param.watch(handle_file_upload, 'value')

# ========================================================================================
# Configuraciones elementos de interfaz
# ========================================================================================

# Boton de descarga del SVG
download_svg = pn.widgets.FileDownload(
    callback=get_svg_download,
    icon='download',
    filename='Design.svg',
    button_type='success',
    embed=False, auto=True,
    height=30,
    width=240,
)

# Tab con las configuraciones del panel
settings_tab = pn.Column(
    width_slider,
    height_slider,
    color_picker,
    download_svg,
    file_input,
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
    create_button_panel(utils.button_data),
    name='Figure')

# Tab con las configuraciones de los pictogramas
pictogram_tab = pn.Column(name='Pictogram')

# Panel principal con el SVG
panel = pn.Column(create_panel, styles=utils.styles_panel)

# Panel con la barra lateral "Sidebar contiene los tabs"
sidebar = pn.Tabs(
    settings_tab,
    text_tab,
    figures_tab,
    pictogram_tab,
    styles=utils.styles_sidebar,
)

# ========================================================================================
# Cargar el contenido en el HTML
# ========================================================================================

sidebar.servable(target='sidebar-panel')
panel.servable(target='drawing-panel')

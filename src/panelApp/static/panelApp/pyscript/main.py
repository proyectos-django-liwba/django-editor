# dependencias
import xml.etree.ElementTree as ET
from io import StringIO

# from panel.reactive import ReactiveHTML
import panel as pn
import param
from js import document, console

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
    is_load_svg = (param.Boolean(default=False))

    def clear_svg(self):
        self.svg_content = ""
        self.additional_shapes = []
        self.current_shape = None
        self.is_load_svg = False
        self.param.trigger("svg_content")
        self.param.trigger("additional_shapes")
        self.param.trigger("current_shape")
        self.param.trigger("is_load_svg")

    def get_all_shapes(self):
        all_shapes = ""
        for shape in self.additional_shapes:
            all_shapes += shape.get_svg() + "\n"

        return all_shapes

    # def update_current_shape(self, shape_id):
    #     print(f'Updating current shape to {shape_id}')
    #     shape = next((shape for shape in self.additional_shapes if shape.id == shape_id), None)
    #
    #     if shape:
    #         self.current_shape = shape
    #         self.param.current_shape.objects = self.additional_shapes
    #         print(f'Current shape: {self.current_shape.get_svg()}')

    def parse_svg_content(self, file_content):
        # Crear un árbol XML del contenido SVG
        tree = ET.ElementTree(ET.fromstring(file_content))
        root = tree.getroot()
        # Limpiar la lista de figuras adicionales
        self.additional_shapes = []

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

            print("atributos!!!!!!!!!")
            attributes = {key: value for key, value in elem.attrib.items()}
            print("atributos", attributes)
            figure.update(**attributes)

            print(figure.get_svg())
            self.additional_shapes.append(figure)

        print("Figuras ")
        for f in self.additional_shapes:
            print(f.get_svg())


# import param
# from panel.reactive import ReactiveHTML
# class ReactiveFigures(ReactiveHTML):
#     index = param.Integer(default=0)
#
#     _template = '<img id="slideshow_el" src="https://picsum.photos/800/300?image=${index}" onclick="${_img_click}"></img>'
#
#     def _img_click(self, event):
#         self.index += 1

# class ReactiveFigures(ReactiveHTML):
#     _template = """<div id="svg-container" onclick="${_prueba}">
#                         <p>SVG content:</p>
#                   </div>
#                 """
#     def _prueba(self, event):
#         print("Prueba")

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
# text_input = pn.widgets.TextInput(name='Text to Add', value='I love SVG!', max_length=250, width=240)
text_input = pn.widgets.TextInput(name='Text to Add', value='', max_length=250, width=240)
# Botón para actualizar el SVG con el texto
text_size = pn.widgets.IntSlider(name='Font size', start=8, end=24, step=1, value=12, width=240)
text_color_picker = pn.widgets.ColorPicker(name='Text color', value='#000000')

file_input = pn.widgets.FileInput(accept='.svg', multiple=False, width=240)

# Boton para limpiar el contenido del SVG
clear_svg_button = pn.widgets.Button(name='Clear SVG', icon='trash', button_type='danger', height=30, width=240)

temp_button = pn.widgets.Button(name='Prueba', button_type='warning', width=240)
# ========================================================================================
# Variable Globales
# ========================================================================================

# Elementos adicionales del SVG
svg_params = SVGParams()


def select_svg_element_by_id(element_id):
    try:
        element = document.getElementById(element_id)
        if element is not None:
            console.log(f"Element with id {element_id} selected.")
        else:
            console.error(f"No element found with id {element_id}.")
    except Exception as e:
        console.error(f"Error selecting element: {e}")


# ========================================================================================
# ShadowRoot
# ========================================================================================
def unlock_shadowroot(element_id, shadow_root=None):
    # Access the outer shadow root host
    outer_host = document.querySelector(element_id)

    if shadow_root is not None:
        outer_host = shadow_root.querySelector(element_id)

    # Create the outer shadow root if it doesn't already exist
    if not outer_host.shadowRoot:
        outer_host.attachShadow({'mode': 'open'})

    # Get the outer shadow root
    return outer_host.shadowRoot

def prueba_xd(event):
    console.log('Prueba')

#def unlock_panel(event):
def unlock_panel(event):
    try:
        # arreglo de los shadow roots a deshabilitar
        shadow_roots = ['.bk-panel-models-layout-Column', '.bk-panel-models-layout-Column', '.bk-panel-models-markup-HTML']

        tem_shadow_root = None

        for shadow_root in shadow_roots:
            tem_shadow_root = unlock_shadowroot(shadow_root, tem_shadow_root)

        # llegar a la figura objetivo
        figure = tem_shadow_root.querySelector('#background')
        figure.onclick = lambda event: prueba_xd(event)
        figure.setAttribute('stroke', 'blue')
        figure.setAttribute('stroke-width', 1)

        #figure.style.border = '2px solid red'

        # iterar el arreglo de figuras
        # obtener su id y setearla en una variable global
        # agregarle una funcion
        # resaltar la figura    "agregar stylos por medio de un atributo nuevo en la figura"

        print(figure)
        console.log(figure)
    except Exception as e:
        console.error(f"Error unlocking panel: {e}")




temp_button.on_click(unlock_panel)


# ========================================================================================
# Funciones
# ========================================================================================

# Función para ajustar el texto en múltiples líneas
def wrap_text(text, max_width, font_size, text_color):
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

    text_elements = ''.join(
        f'<tspan x="5" dy="{font_size + 5}" fill="{text_color}">{line}</tspan>'
        if i != 0 else f'<tspan x="5" dy="0" fill="{text_color}">{line}</tspan>'
        for i, line in enumerate(lines)
    )

    return text_elements


# SVG base en blanco
def create_svg_base(width, height, color, text, font_size, text_color, shapes, is_load_svg):
    # Ajustar las lineas del texto al ancho del SVG
    wrapped_text = wrap_text(text, width - 10, font_size, text_color)

    if not is_load_svg and (len(shapes) == 0 or shapes[0].id != 'background'):
        factory = figures.FigureFactory()
        background = factory.create_element("rect", id="background", x=0, y=0, width=width, height=height, fill=color,
                                            stroke='none', stroke_width=0)
        shapes.insert(0, background)

    # Crear un string con las figuras adicionales
    figures_svg = svg_params.get_all_shapes()

    return f'''<svg id="drawing-svg" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
                     {figures_svg}
                    <text x="5" y="15" font-size="{font_size}" fill="{text_color}">
                        {wrapped_text}
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
    svg_params.param.is_load_svg,
)
def create_panel(width, height, color, text, font_size, text_color, shapes, is_load_svg, ):
    svg_params.svg_content = create_svg_base(width, height, color, text, font_size, text_color, shapes, is_load_svg)
    svg_content = create_svg_base(width, height, color, text, font_size, text_color, shapes, is_load_svg)
    # return pn.pane.SVG(
    #     svg_params.svg_content,
    #     width=width,
    #     height=height,
    # )
    return pn.pane.HTML(svg_params.svg_content, width=width, height=height)


# Función para descargar el SVG
def get_svg_download():
    global svg_params
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
    #unlock_panel(event)
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
    # Agregar la figura a la lista y forzar actualización del parámetro
    svg_params.additional_shapes.append(figure)
    svg_params.param.trigger('additional_shapes')
    svg_params.param.trigger('svg_content')
    unlock_panel(event)
    # svg_params.update_current_shape(id_figure)


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


# @pn.depends(file_input.param.value, watch=True)
def handle_file_upload(event):
    color_picker.value = '#FFFFFF'
    file_data = event.new

    if file_data is not None:
        try:
            # Limpiar el contenido anterior
            svg_params.clear_svg()
            # No agregar figura de fondo
            svg_params.is_load_svg = True
            # reconstruir el SVG con el contenido del archivo
            svg_params.parse_svg_content(file_data.decode('utf-8'))
            # forzar actualización del parámetro
            svg_params.param.trigger('is_load_svg')
            svg_params.param.trigger('additional_shapes')

        except Exception as e:
            print(f"Error al decodificar el archivo: {e}")
    else:
        print("Archivo subido es None")


# Funcion para actualizar el color de fondo del SVG
def update_background_color(event):
    if len(svg_params.additional_shapes) > 0:
        svg_params.additional_shapes[0].update(fill=color_picker.value)


# Conectar la función de manejo de archivos al widget
file_input.param.watch(handle_file_upload, 'value')
color_picker.param.watch(update_background_color, 'value')

# ========================================================================================
# Configuraciones elementos de interfaz
# ========================================================================================

# Boton de descarga del SVG
download_svg = pn.widgets.FileDownload(
    callback=get_svg_download,
    icon='download',
    filename='Design.svg',
    button_type='success',
    embed=False,
    auto=True,
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
    clear_svg_button,
    temp_button,
    name='Setting'
)


def clear_svg_and_file_input(event):
    svg_params.clear_svg()
    file_input.value = None
    settings_tab[4] = pn.widgets.FileInput(accept='.svg', multiple=False, width=240)
    settings_tab[4].param.watch(handle_file_upload, 'value')
    color_picker.value = "#ffffff"


# Evento para limpiar el contenido del SVG
clear_svg_button.on_click(clear_svg_and_file_input)

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
# xd = ReactiveFigures()
# Panel principal con el SVG
# panel = pn.Column(xd, styles=utils.styles_panel)
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

# x = pn.Row(
#     ReactiveFigures(width=800, height=300)
# )
# x.servable(target='app')

sidebar.servable(target='sidebar-panel')
panel.servable(target='drawing-panel')

# Ejecutar unlock_panel cuando la página esté cargada
#pn.state.onload(unlock_panel)
#pn.state.onload(lambda: unlock_panel())
#unlock_panel()
# cargar de forma predeterminada no es posible
# opcion: activar la funcion unlock_panel cada vez que se modifica el contenido del SVG
#svg_params.param.watch(unlock_panel, 'svg_content')
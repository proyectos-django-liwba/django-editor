
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
    def __init__(self):
        self.selected = False

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def get_svg(self):
        pass

    def toggle_selection(self):
        self.selected = not self.selected

    def get_selection_style(self):
        return 'stroke="blue" stroke-width="5"' if self.selected else ''


class FigureRect(FigureInterface):
    def __init__(self, id="f_", width=100, height=100, x=0, y=0, rx=0, ry=0, fill='none', stroke='black',
                 stroke_width=1, opacity=1):
        super().__init__()
        self.id = id
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
        return f'<rect id="{self.id}" width="{self.width}" height="{self.height}" x="{self.x}" y="{self.y}" rx="{self.rx}" ry="{self.ry}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" opacity="{self.opacity}" />'


class FigureCircle(FigureInterface):
    def __init__(self, id="f_", r=45, cx=50, cy=50, fill='none', stroke='black', stroke_width=1, opacity=1):
        super().__init__()
        self.id = id
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
        return f'<circle id="{self.id}" r="{self.r}" cx="{self.cx}" cy="{self.cy}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" opacity="{self.opacity}" />'


class FigureTriangle(FigureInterface):
    def __init__(self, id="f_", points="100,10 150,100 50,100", fill='none', stroke='black', stroke_width=1, opacity=1):
        super().__init__()
        self.id = id
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
        return f'<polygon id="{self.id}" points="{self.points}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" opacity="{self.opacity}" />'


class FigureEllipse(FigureInterface):
    def __init__(self, id="f_", rx=60, ry=30, cx=100, cy=50, fill='none', stroke='black', stroke_width=1, opacity=1):
        super().__init__()
        self.id = id
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
        return f'<ellipse id="{self.id}" rx="{self.rx}" ry="{self.ry}" cx="{self.cx}" cy="{self.cy}" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.stroke_width}" opacity="{self.opacity}" />'


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

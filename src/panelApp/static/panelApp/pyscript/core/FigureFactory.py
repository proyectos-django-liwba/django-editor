from FigureRect import FigureRect
from FigureCircle import FigureCircle
from FigureTriangle import FigureTriangle
from FigureEllipse import FigureEllipse
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

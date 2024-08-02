from FigureInterface import FigureInterface

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

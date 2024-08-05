from FigureInterface import FigureInterface

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

from FigureInterface import FigureInterface

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

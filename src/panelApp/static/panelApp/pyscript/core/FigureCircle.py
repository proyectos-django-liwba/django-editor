from FigureInterface import FigureInterface

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

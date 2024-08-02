from abc import ABC, abstractmethod

class FigureInterface(ABC):

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def get_svg(self):
        pass
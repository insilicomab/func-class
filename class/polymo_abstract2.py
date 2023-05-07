# リスト10.32
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def get_area(self):
        pass

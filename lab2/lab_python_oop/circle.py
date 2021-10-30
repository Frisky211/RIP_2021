from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
import math


class Circle(Figure):
    
    FIGURE_TYPE = "Круг"
    
    @classmethod
    def get_fig_type(cls):
        return cls.FIGURE_TYPE
    
    def __init__(self, c, r):
        self.r = r
        self.c = FigureColor()
        self.c.color = c
    
    def square(self):
        return math.pi * (self.r * 2)
        
    def __repr__(self):
        return '{} {} цвета, радиусом {}, площадью {}.'.format(
            Circle.get_fig_type(),
            self.c.color,
            self.r,
            self.square()
        )
    
    
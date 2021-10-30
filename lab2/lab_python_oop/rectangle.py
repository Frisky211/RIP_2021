from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure):
    
    FIGURE_TYPE = "Прямоугольник"
    
    @classmethod
    def get_fig_type(cls):
        return cls.FIGURE_TYPE
    
    def __init__(self, c, wid, hei):
        self.w = wid
        self.h = hei
        self.c = FigureColor()
        self.c.color = c
    
    def square(self):
        return self.w * self.h
        
    def __repr__(self):
        return '{} {} цвета, высоты {}, ширины {}, площадью {}.'.format(
            Rectangle.get_fig_type(),
            self.c.color,
            self.h,
            self.w,
            self.square()
        )
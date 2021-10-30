from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE
        
    def __init__(self, c, l):
        self.l = l
        super().__init__(c, self.l, self.l)
    
    def __repr(self):
        return '{} {} цвета со стороной {}, площадью {}.'.format(
            Square.get_fig_type(),
            self.c.color,
            self.l,
            self.square()
        )
        
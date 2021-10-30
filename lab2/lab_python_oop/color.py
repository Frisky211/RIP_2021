class FigureColor:
    def __init__(self):
        _color = None
    
    @property
    def color(self):
        return self._color
        
    @color.setter
    def color(self, c):
        self._color = c
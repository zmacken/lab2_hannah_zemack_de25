from shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        if not isinstance(w, (int,float)) or not isinstance(h, (int, float)):
            raise TypeError ('height and widht must be a numeric value')
        self._w = w
        self._h= h
    
    @property
    def w(self):
        return self._w
    
    @property
    def h(self):
        return self._h
    
    @property
    def area(self) -> float:
        return self._w * self._h
    
    @property
    def perimeter(self) -> float:
        return (2* self._w) + (2* self._h)
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        
        if self.area == other.area and self.perimeter == other.perimeter:
            return True
        else:
            return False
        
    def __repr__(self):
        base = super().__repr__()
        return f'{base[:-1]}, width = {self._w}, height = {self._h})'
    


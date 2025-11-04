from shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        if not isinstance(width, (int,float)) or not isinstance(height, (int, float)):
            raise TypeError ('height and widht must be a numeric value')
        self._width = width
        self._height= height
    
    @property
    def w(self):
        return self._width
    
    @property
    def h(self):
        return self._height
    
    @property
    def area(self) -> float:
        return self._width * self._height
    
    @property
    def perimeter(self) -> float:
        return (2* self._width) + (2* self._height)
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        
        if self.area == other.area and self.perimeter == other.perimeter:
            return True
        else:
            return False
        
    def is_square(self):
        if self._width == self._height:
            return True
        else:
            return False
        
    def __repr__(self):
        base = super().__repr__()
        return f'{base[:-1]}, width = {self._width}, height = {self._height})'
    
    def __str__(self) -> str:
        return f"Rectangle with center at ({self._x}, {self._y}), width {self._width}, and height {self._height}"

    


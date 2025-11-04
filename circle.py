from shape import Shape
import math

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a numerical value')
        self._radius = radius
    
    @property
    def r(self):
        return self._radius
    
    @property
    def area(self) -> float:
        return math.pi * self._radius**2 
    
    @property
    def perimeter(self) -> float:
        return 2 * self._radius *math.pi
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        
        if self.area == other.area:
            return True
        else:
            return False
    
    def is_unit_circle(self):
        if self._x==0 and self._y==0 and self._radius==1:
            return True
        else:
            return False
    
    def __repr__(self):
        base = super().__repr__()
        return f'{base[:-1]}, radius = {self._radius})'
    
    def __str__(self) -> str:
        return f"Circle with center at ({self._x}, {self._y}) and radius {self._radius}"
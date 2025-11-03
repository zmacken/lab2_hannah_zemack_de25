from shape import Shape
import math

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        if not isinstance(r, (int, float)):
            raise TypeError('radius must be a numerical value')
        self._r = r
    
    @property
    def r(self):
        return self._r
    
    @property
    def area(self) -> float:
        return math.pi * self._r**2 
    
    @property
    def perimeter(self) -> float:
        return 2 * self._r *math.pi
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        
        if self.area == other.area:
            return True
        else:
            return False
    
    
    
    def __repr__(self):
        base = super().__repr__()
        return f'{base[:-1]}, radius = {self._r})'
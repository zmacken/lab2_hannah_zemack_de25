from shape import Shape
import math

class Sphere(Shape):
    def __init__(self, x = 0, y = 0, radius: float = 1):
        super().__init__(x, y)
        if not isinstance(radius, (int,float)): #error handling to check if side is number
            raise TypeError ('side must be a numeric value')
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @property
    def volume(self):
        return (4/3) * math.pi * (self._radius **3)
    
    @property
    def surface(self):
        return 4 * math.pi * (self._radius **3)
    
    def __eq__(self, other):
        if not isinstance(other, Sphere): #check if other object is cube
            return False
        
        if self.volume == other.volume: #check if volume are the same
            return True
        else:
            return False
        
    def __lt__(self, other): #less than
        if self.volume < other.volume:
            return True
        else:
            return False
    
    def __le__(self, other): #less than or equal
        if self.volume <= other.volume:
            return True
        else:
            return False

    def __gt__(self, other): #greater than
        if self.volume > other.volume:
            return True
        else:
            return False
    
    def __ge__(self, other): #greater than or equal 
        if self.volume >= other.volume:
            return True
        else:
            return False
        
    def __repr__(self): #override repr
        base = super().__repr__()
        return f'(Sphere) {base[6:-1]}, radius: {self._radius})'
    
    def __str__(self) -> str: #override str
        return f"Sphere with center at ({self._x}, {self._y}), and radius: {self._radius}"
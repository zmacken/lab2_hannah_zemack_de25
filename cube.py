from shape import Shape

class Cube(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        if not isinstance(side, (int,float)): #error handling to check if side is number
            raise TypeError ('side must be a numeric value')
        self._side = side

    @property
    def side(self):
        return self._side
    
    @property
    def volume(self):
        return self._side **3
    
    def __eq__(self, other):
        if not isinstance(other, Cube): #check if other object is cube
            return False
        
        if self.volume == other.volume: #check if volume are the same
            return True
        else:
            return False
        
    def __repr__(self): #override repr
        base = super().__repr__()
        return f'{base[:-1]}, side: {self._side})'
    
    def __str__(self) -> str: #override str
        return f"Cube with center at ({self._x}, {self._y}), and side: {self._side}"
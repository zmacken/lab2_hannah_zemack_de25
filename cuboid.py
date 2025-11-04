from shape import Shape
from rectangle import Rectangle

class Cuboid(Rectangle):
    def __init__(self, x, y, width, height, depth):
        super().__init__(x, y, width, height)
        if not isinstance(depth, (int,float)): #error handling to check id w and h is numbers
            raise TypeError ('height and widht must be a numeric value')
        self._depth = depth

    @property
    def depth(self):
        return self._depth #read-only attribute
    
    @property
    def volume(self):
        return self._width * self._height * self._depth

    @property
    def surface(self):
        return 

    #check if cube
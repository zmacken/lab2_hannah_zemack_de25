from shape import Shape
import math
import matplotlib.patches as patches

class Circle(Shape): #define a circle class that inherits from shape
    def __init__(self, x = 0, y = 0, radius: float = 1): 
        super().__init__(x, y) #inherit x and y attributes
        if not isinstance(radius, (int, float)): #error handling for radius
            raise TypeError('radius must be a numerical value')
        self._radius = radius #store radius as a private attribute
    
    @property
    def radius(self):
        return self._radius #provide read only acces to the radius
    
    @property
    def area(self) -> float:
        return math.pi * self._radius**2  #calculate and return the area of the circle
    
    @property
    def perimeter(self) -> float:
        return 2 * self._radius *math.pi #calculate and return the perimeter of the circle
    
    def __eq__(self, other): #operator overload to check if shape is the same
        if not isinstance(other, Circle): #check if the other object is circle
            return False
        
        if self.area == other.area: #check if area is equal
            return True
        else:
            return False
    
    def is_unit_circle(self):
        if self._x==0 and self._y==0 and self._radius==1: #check if circle har x and y of 0 and radius of 1
            return True
        else:
            return False
        
    def draw(self, ax):
        circle_patch = patches.Circle(
            (self._x, self._y),
            self._radius
        )
        ax.add_patch(circle_patch)
    
    def __repr__(self): #override __repr__
        base = super().__repr__()
        return f'{base[:-1]}, radius = {self._radius})'
    
    def __str__(self) -> str: #override __str__
        return f"Circle with center at ({self._x}, {self._y}) and radius {self._radius}"
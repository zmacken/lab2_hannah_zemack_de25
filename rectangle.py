from shape import Shape
import matplotlib.patches as patches

class Rectangle(Shape): #define a rectangle class that inherits from shape
    def __init__(self, x, y, width, height):
        super().__init__(x, y) #inherit x and y attributes
        if not isinstance(width, (int,float)) or not isinstance(height, (int, float)): #error handling to check id w and h is numbers
            raise TypeError ('height and widht must be a numeric value')
        self._width = width #store width a private attribute
        self._height= height #store height a private attribute
    
    @property
    def width(self):
        return self._width #read-only access to width
    
    @property
    def height(self):
        return self._height #read-only access to height
    
    @property
    def area(self) -> float:
        return self._width * self._height #calculate and return area of rectangle
    
    @property
    def perimeter(self) -> float:
        return (2* self._width) + (2* self._height) #calculate and return perimeter of rectangle
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle): #check if other object is rectangle
            return False
        
        if self.area == other.area and self.perimeter == other.perimeter: #check if area and perimeter are the same = same rectangle
            return True
        else:
            return False
        
    def is_square(self): #check if rectangles height and width are the same = square
        if self._width == self._height:
            return True
        else:
            return False
        
    def draw(self, ax):
        lower_left_x = self.x - self.width / 2
        lower_left_y = self.y - self.height / 2
        rect_patch = patches.Rectangle(
            (lower_left_x, lower_left_y),
            self.width,
            self.height
        )
        ax.add_patch(rect_patch)
        
    def __repr__(self): #override repr
        base = super().__repr__()
        return f'{base[:-1]}, width = {self._width}, height = {self._height})'
    
    def __str__(self) -> str: #override str
        return f"Rectangle with center at ({self._x}, {self._y}), width {self._width}, and height {self._height}"

    


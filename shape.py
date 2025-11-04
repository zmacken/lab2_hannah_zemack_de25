class Shape(): #define an base class calles shapes
    def __init__(self, x, y): 
        if not isinstance(x, (int, float)) or not isinstance (y, (int, float)):  #error handling check that x and y are numbers
            raise TypeError ('x and y must be numeric values')
        self._x = x #store x-coordinate as private attribute
        self._y = y #store y-coordinate as private attribute

    @property 
    def x(self) -> float:
        return self._x  #read-only access to x
    
    @property
    def y(self) -> float:
        return self._y #read-only access to y
    
    @property
    def area(self):
        pass # must be implemented by subclasses to return area

    @property
    def perimeter(self):
        pass # must be implemented by subclasses to return perimeter
    

    def translate(self, dx: float, dy: float) -> None: 
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)): #validate that dx and dy are numbers
            raise TypeError ('Translation must be numeric values')
        self._x += dx #store dy as private attribute
        self._y += dy #store dx as private attribute
 
    #comaprison operators based on area
    def __lt__(self, other): #less than
        if self.area < other.area:
            return True
        else:
            return False
    
    def __le__(self, other): #less than or equal
        if self.area <= other.area:
            return True
        else:
            return False

    def __gt__(self, other): #greater than
        if self.area > other.area:
            return True
        else:
            return False
    
    def __ge__(self, other): #greater than or equal 
        if self.area >= other.area:
            return True
        else:
            return False


    def __repr__(self): #override repr
        return f'Shape(x = {self._x}, y = {self._y})'
    

    def __str__(self): #override str
        return f'Shape is centered at x:{self._x} and y:{self._y}'

    

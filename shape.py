from circle import Circle

class Shape: #this class is to define x and y to set the center of the object for both circle and rectangle
    def __init__(self, x, y): 
        if not isinstance(x, (int, float)) or not isinstance (y, (int, float)): #error handling, making sure only numeriva values
            raise TypeError ('x and y must be numeric values')
        self._x = x 
        self._y = y

    @property #making them only read only
    def x(self) -> float:
        return self._x 
    
    @property
    def y(self) -> float:
        return self._y
    
    #måste testa när plotta
    def translate(self, dx: float, dy: float) -> None: #this function is for translating the x and y points so that you can move the center
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError ('Translation must be numeric values')
        self._x += dx #add old value to new point
        self._y += dy 

    #Lägga till någon operator overload som kan jämföra area (eller ska denna kanske vara i de andra klasserna)

    def __repr__(self):
        return f'Shape(x = {self._x}, y = {self._y})'
    
    #lägga till __Str__

    

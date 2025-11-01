class Shape:
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
    
    
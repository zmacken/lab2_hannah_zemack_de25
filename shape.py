class Shape:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance (y, (int, float)):
            raise TypeError ('x and y must be numeric values')
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        
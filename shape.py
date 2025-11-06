class Shape(): #define an base class calles shapes
    def __init__(self, x:float , y: float): 
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
        raise NotImplementedError ('subclass must have implemented area')

    @property
    def perimeter(self):
        raise NotImplementedError ('subclass must have implemented perimeter')
    
    def translate(self, dx: float, dy: float) -> None: 
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)): #validate that dx and dy are numbers
            raise TypeError ('Translation must be numeric values')
        self._x = dx #store dy as private attribute
        self._y = dy #store dx as private attribute
 
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
            self._radius,
            edgecolor = 'red',
            fill = False
        )
        ax.add_patch(circle_patch)
    
    def __repr__(self): #override __repr__
        base = super().__repr__()
        return f'(Circle) {base[6:-1]}, radius = {self._radius}'
    
    def __str__(self) -> str: #override __str__
        return f"Circle with center at ({self._x}, {self._y}) and radius {self._radius}"
    

from shape import Shape
import matplotlib.patches as patches

class Rectangle(Shape): #define a rectangle class that inherits from shape
    def __init__(self, x = 0, y = 0 , width: float = 1, height: float= 1):
        super().__init__(x, y) #inherit x and y attributes
        if not isinstance(width, (int,float)) or not isinstance(height, (int, float)): #error handling to check id w and h is numbers
            raise TypeError ('height and width must be a numeric value')
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
        lower_left_x = self._x - self._width / 2
        lower_left_y = self._y - self._height / 2
        rect_patch = patches.Rectangle(
            (lower_left_x, lower_left_y),
            self._width,
            self._height,
            edgecolor = 'red',
            fill = False
        )
        ax.add_patch(rect_patch)

    
    def __repr__(self): #override repr
        base = super().__repr__()
        return f'(Rectangle) {base[6:-1]}, width = {self._width}, height = {self._height})'
    
    def __str__(self) -> str: #override str
        return f"Rectangle with center at ({self._x}, {self._y}), width {self._width}, and height {self._height}"

    

import matplotlib.pyplot as plt
from shape import Shape

class Shape2Dplotter: #define a class to use for 2d plotting
    def __init__(self):
        self.shapes = []  # list to store added shapes

    def add_shape(self, shape: Shape): #function to add to list shapes
        if not isinstance(shape, Shape):
            raise TypeError("Only Shape instances can be added")
        self.shapes.append(shape)

    def plot(self):
        fig, ax = plt.subplots() #create subplots, fig needs to be there to access ax
        for shape in self.shapes: 
            try:
                shape.draw(ax)  # every figure knows how to write it self
            except AttributeError:
                print ('only 2d objects can be plotted')
        ax.set_aspect('equal') #equal scaling for x and y
        ax.autoscale_view() #automatically adjust view to fit all shapes
        plt.grid(True, color='green', linewidth = .1)
        plt.show() #display the plot window

from shape import Shape

class Cube(Shape):
    def __init__(self, x = 0 , y = 0, side: float = 1):
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
    
    @property
    def surface(self):
        return (self._side * 2) * 6
    
    def __eq__(self, other):
        if not isinstance(other, Cube): #check if other object is cube
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
        return f'(Cube) {base[6:-1]}, side: {self._side})'
    
    def __str__(self) -> str: #override str
        return f"Cube with center at ({self._x}, {self._y}), and side: {self._side}"

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

import pytest
from circle import Circle
import math

def test_circle_area():
    r = 1
    c = Circle(0, 0, r)
    assert round(c.area) == round(math.pi * r**2)

def test_perimeter_circle():
    r = 1
    c = Circle(0, 0, r)
    assert round(c.perimeter) == round(2 * r *math.pi)

def test_greater_than_circle():
    r = 1
    c1 = Circle(0,0,r*2)
    c2 = Circle(0, 0, r)
    assert c1 > c2

def test_less_than_circle():
    r = 1
    c1 = Circle(0,0,r)
    c2 = Circle(0, 0, r*2)
    assert c1 < c2

def test_equal_circle():
    r=1
    c1 = Circle (0,0,r)
    c2 = Circle (0,0,r)
    assert c1 == c2

def test_less_or_equal_circlel():
    r=1
    c1 = Circle(0,0,r)
    c2 = Circle(0,0,r)
    assert c1<=c2

def test_greater_or_equal_circle():
    r=1
    c1 = Circle(0,0,r)
    c2 = Circle(0,0,r)
    assert c1>=c2

def test_translate_circle():
    r= 1
    c1 = Circle(0,0,r)
    c1.translate(1, 1)
    assert c1.x == 1 and c1.y == 1

import pytest
from cube import Cube

def test_cube_volume():
    s = 1
    c = Cube(0, 0, s)
    assert c.volume == s **3

def test_cube_surface():
    s =1 
    c = Cube(0,0,s)
    assert c.surface == (s*2)*6

def test_greater_than_cube():
    s = 1
    c1 = Cube(0,0,s*2)
    c2 = Cube(0, 0, s)
    assert c1 > c2

def test_less_than_cube():
    s = 1
    c1 = Cube(0,0,s)
    c2 = Cube(0, 0, s*2)
    assert c1 < c2

def test_equal_cube():
    s=1
    c1 = Cube (0,0,s)
    c2 = Cube (0,0,s)
    assert c1 == c2

def test_less_or_equal_cubel():
    s=1
    c1 = Cube(0,0,s)
    c2 = Cube(0,0,s)
    assert c1<=c2

def test_greater_or_equal_cube():
    s=1
    c1 = Cube(0,0,s)
    c2 = Cube(0,0,s)
    assert c1>=c2

def test_translate_cube():
    s= 1
    c1 = Cube(0,0,s)
    c1.translate(1, 1)
    assert c1.x == 1 and c1.y == 1

import pytest
from rectangle import Rectangle

def test_rectangle_area():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, w, h)
    assert r1.area == 1

def test_perimeter_rectangle():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, w, h)
    assert r1.perimeter == 4

def test_greater_than_rectangle():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, 2*w, 2*h)
    r2 = Rectangle(0, 0, w, h)
    assert r1 > r2

def test_less_than_rectangle():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, w, h)
    r2 = Rectangle(0, 0, 2*w, 2*h)
    assert r1 < r2

def test_equal_rectangle():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, w, h)
    r2 = Rectangle(0, 0, w, h)
    assert r1 == r2

def test_less_or_equal_rectangle():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, w, h)
    r2 = Rectangle(0, 0, w, h)
    assert r1 <= r2

def test_greater_or_equal_rectangle():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, w, h)
    r2 = Rectangle(0, 0, w, h)
    assert r1 >= r2

def test_translate_rectangle():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, w, h)
    r1.translate(1, 1)
    assert r1.x == 1 and r1.y == 1

import pytest
from sphere import Sphere
import math

def test_sphere_volume():
    r = 1
    s = Sphere(0, 0, r)
    assert round(s.volume) == round((4/3) * math.pi * (r **3))

def test_surface_sphere():
    r = 1
    s = Sphere(0, 0, r)
    assert round(s.surface) == round(4 * math.pi * (r **3))

def test_greater_than_sphere():
    r = 1
    s1 = Sphere(0,0,r*2)
    s2 = Sphere(0, 0, r)
    assert s1 > s2

def test_less_than_sphere():
    r = 1
    s1 = Sphere(0,0,r)
    s2 = Sphere(0, 0, r*2)
    assert s1 < s2

def test_equal_sphere():
    r=1
    s1 = Sphere (0,0,r)
    s2 = Sphere (0,0,r)
    assert s1 == s2

def test_less_or_equal_spherel():
    r=1
    s1 = Sphere(0,0,r)
    s2 = Sphere(0,0,r)
    assert s1<=s2

def test_greater_or_equal_sphere():
    r=1
    s1 = Sphere(0,0,r)
    s2 = Sphere(0,0,r)
    assert s1>=s2

def test_translate_sphere():
    r= 1
    s1 = Sphere(0,0,r)
    s1.translate(1, 1)
    assert s1.x == 1 and s1.y == 1

import pytest
from circle import Circle
import math

def test_circle_area():
    r = 1
    c = Circle(0, 0, r)
    assert round(c.area) == round(math.pi * r**2)

def test_greater_than():
    r = 1
    c1 = Circle(0,0,r*2)
    c2 = Circle(0, 0, r)
    assert c1 > c2

def test_less_than():
    r = 1
    c1 = Circle(0,0,r)
    c2 = Circle(0, 0, r*2)
    assert c1 < c2

def test_equal():
    r=1
    c1 = Circle (0,0,r)
    c2 = Circle (0,0,r)
    assert c1 == c2

def test_less_or_equal():
    r=1
    c1 = Circle(0,0,r)
    c2 = Circle(0,0,r)
    assert c1<=c2

def test_greater_or_equal():
    r=1
    c1 = Circle(0,0,r)
    c2 = Circle(0,0,r)
    assert c1>=c2

def test_translate():
    r= 1
    c1 = Circle(0,0,r)
    



# print(circle1 == circle2)  # True
# print(circle2 == rectangle)  # False
# circle1.translate(5, 3) # moves its center 5 points in x and 3 points in y
# #circle1.translate("THREE", 5)  # raise TypeError with an appropriate message
# circle3 = Circle(radius=3) # a circle with center 0,0 with radius 3
# circle3 >= circle1 # True
# rectangle2 = Rectangle(width=3, height="5") # raise TypeError
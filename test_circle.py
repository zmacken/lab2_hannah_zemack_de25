import pytest
from circle import Circle
import math

def test_circle_area():
    r = 1
    c = Circle(0, 0, r)
    assert round(c.area) == round(math.pi * r**2)

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

def test_less_or_equa_circlel():
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
    assert c1.translate(1, 1)


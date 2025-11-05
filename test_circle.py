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


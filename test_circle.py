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

def test_equal_circle_false():
    r=1
    c1 = Circle (0,0,r)
    c2 = Circle (0,0,2*r)
    assert c1 != c2

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

def test_translate_circle_invalid():
    c = Circle(0, 0, 1)
    with pytest.raises(TypeError):
        c.translate("hej", 4)

def test_circle_invalid_radius():
    with pytest.raises(TypeError):
        Circle(0, 0, "hej")

def test_circle_str_and_repr():
    c = Circle(0,0,1)
    assert "Circle" in str(c)
    assert "Circle" in repr(c)


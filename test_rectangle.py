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

def test_rectangle_is_square():
    w = 2
    h = 2
    r1 = Rectangle(0, 0, w, h)
    assert r1.is_square() == True

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

def test_not_equal_rectangle():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, w, h)
    r2 = Rectangle(0, 0, 2*w, 2*h)
    assert r1 != r2

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

def test_invalid_width():
    with pytest.raises(TypeError):
        Rectangle(0,0,"hej",2)

def test_invalid_height():
    with pytest.raises(TypeError):
        Rectangle(0,0,2,"hej")

def test_rectangle_str_and_repr():
    r = Rectangle(0,0,1,1)
    assert "Rectangle" in str(r)
    assert "Rectangle" in repr(r)


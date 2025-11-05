import pytest
from rectangle import Rectangle

def test_rectangle_area():
    w = 1
    h = 1
    r1 = Rectangle(0, 0, w, h)
    assert r1.area == 1

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
    assert r1.translate(1, 1)
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
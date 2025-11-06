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
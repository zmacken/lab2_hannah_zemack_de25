import pytest
from circle import Circle
import math

def test_circle_area():
    r = 1
    c = Circle(0, 0, r)
    assert round(c.area) == round(math.pi * r**2)
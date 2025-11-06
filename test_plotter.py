import pytest
from plotter import Shape2Dplotter
from circle import Circle
from rectangle import Rectangle
from cube import Cube

def test_add_shape():
    p = Shape2Dplotter()
    c = Circle(0,0,1)
    p.add_shape(c)
    assert len(p.shapes) == 1

def test_add_shape_invalid():
    p = Shape2Dplotter()
    with pytest.raises(TypeError):
        p.add_shape("hej")

def test_plot_no_crash():
    p = Shape2Dplotter()
    p.add_shape(Circle(0,0,1))
    p.add_shape(Rectangle(0,0,2,3))
    p.plot() 

def test_plot_3d_object_no_crash():
    p = Shape2Dplotter()
    c = Cube(0,0,1)
    p.add_shape(c)
    p.plot()     
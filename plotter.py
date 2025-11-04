import matplotlib.pyplot as plt
from matplotlib.patches import Circle as mplCircle, Rectangle as mplRectangle

class Shape2Dplotter: #define a class to use for 2d plotting
    def __init__(self): #initialize an empty list to store shapes
        self.shapes = [] #list to hold all shapes
    
    def add_shapes(self, shape): #function to add to list shapes
        self.shapes.append(shape) #add to list shapes
    

import matplotlib.pyplot as plt
from shape import Shape

class Shape2Dplotter: #define a class to use for 2d plotting
    def __init__(self):
        self.shapes = []  # list to store added shapes

    def add_shape(self, shape: Shape): #function to add to list shapes
        if not isinstance(shape, Shape):
            raise TypeError("Only Shape instances can be added")
        self.shapes.append(shape)

    def plot(self):
        fig, ax = plt.subplots() #create subplots, fig needs to be there to access ax
        for shape in self.shapes: 
            shape.draw(ax)  # every figure knows how to write it self
        ax.set_aspect('equal') #equal scaling for x and y
        ax.autoscale_view() #automatically adjust view to fit all shapes
        plt.show() #display the plot window

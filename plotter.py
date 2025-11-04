import matplotlib.pyplot as plt
from shape import Shape

class Shape2Dplotter: #define a class to use for 2d plotting
    def __init__(self):
        self.shapes = []  # Lista för figurer

    def add_shape(self, shape: Shape):
        if not isinstance(shape, Shape):
            raise TypeError("Only Shape instances can be added.")
        self.shapes.append(shape)

    def plot(self):
        fig, ax = plt.subplots()
        for shape in self.shapes:
            shape.draw(ax)  # Varje figur vet själv hur den ska ritas
        ax.set_aspect('equal')
        ax.autoscale_view()
        plt.show()
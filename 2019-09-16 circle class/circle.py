import math

class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return "Circle({})".format(self.radius)

    @property
    def radius(self):
        return self.__radius
    @property
    def diameter(self):
        return self.radius * 2
    @property
    def area(self):
        return math.pi * self.radius * self.radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self.__radius = radius
    @diameter.setter
    def diameter(self, diameter):
        self.__radius = diameter / 2


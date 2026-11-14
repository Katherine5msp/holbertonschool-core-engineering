#!/usr/bin/env python3
"""Define shapes using abstract classes and duck typing."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Define the required behavior for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represent a circle with a radius."""

    def __init__(self, radius):
        """Initialize the circle with its radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculate the circumference of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle dimensions."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

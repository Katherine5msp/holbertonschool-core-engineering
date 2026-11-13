#!/usr/bin/env python3
"""Define a Square class with string representation."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size after validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the square position after validation."""
        if (type(value) is not tuple or len(value) != 2
                or any(type(n) is not int or n < 0 for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square."""
        print(self)

    def __str__(self):
        """Return the square representation."""
        if self.__size == 0:
            return ""
        rows = []
        for _ in range(self.__size):
            rows.append(
                " " * self.__position[0] + "#" * self.__size)
        return "\n" * self.__position[1] + "\n".join(rows)

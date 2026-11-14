#!/usr/bin/env python3
"""Define a square with its own string representation."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Represent a square with a readable description."""

    def __str__(self):
        """Return the square's dimensions."""
        return "[Square] {}/{}".format(
            self._Square__size, self._Square__size
        )

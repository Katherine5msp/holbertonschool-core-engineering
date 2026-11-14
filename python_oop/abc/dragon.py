#!/usr/bin/env python3
"""Demonstrate reusable behaviors using mixins."""


class SwimMixin:
    """Provide swimming behavior to other classes."""

    def swim(self):
        """Display the creature's swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior to other classes."""

    def fly(self):
        """Display the creature's flying behavior."""
        print("The creature flies!")



class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can swim, fly, and roar."""

    def roar(self):
        """Display the dragon's roaring behavior."""
        print("The dragon roars!")

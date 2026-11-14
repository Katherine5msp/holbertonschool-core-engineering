#!/usr/bin/env python3
"""Demonstrate multiple inheritance using a flying fish."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Describe swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Describe the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Describe flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Describe the bird's habitat."""
        print("The bird lives in the sky")



class FlyingFish(Fish, Bird):
    """Represent a flying fish with swimming and flying abilities."""

    def fly(self):
        """Describe the flying fish's flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Describe the flying fish's swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Describe the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")

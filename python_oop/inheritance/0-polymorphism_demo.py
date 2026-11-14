#!/usr/bin/env python3
"""Demonstrate inheritance and polymorphism."""


class Animal:
    """Represent an animal with a basic sound."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog."""

    def speak(self):
        """Return the dog's sound."""
        return "Woof"


class Cat(Animal):
    """Represent a cat."""

    def speak(self):
        """Return the cat's sound."""
        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))

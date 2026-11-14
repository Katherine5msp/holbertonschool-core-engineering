# Python - Abstract Classes & Interfaces

This directory contains exercises exploring abstract base
classes, interfaces, duck typing, multiple inheritance,
mixins, and extending built-in Python classes.

## Task 0: Abstract Animal Class and its Subclasses

The `animals.py` module defines an abstract `Animal`
class with a required `sound()` method.

The `Dog` and `Cat` subclasses implement this method,
returning "Bark" and "Meow", respectively.



## Task 1: Shapes, Interfaces, and Duck Typing

The `shapes.py` module defines an abstract `Shape`
class requiring `area()` and `perimeter()` methods.

The `Circle` and `Rectangle` subclasses implement
these methods using their respective geometric formulas.

The `shape_info()` function demonstrates duck typing
by calling the required methods without checking
the object's class.



## Task 2: The Enigmatic FlyingFish

The `flyingfish.py` module demonstrates multiple
inheritance using the `Fish`, `Bird`, and `FlyingFish`
classes.

`FlyingFish` inherits from both parent classes and
overrides their methods to define its own swimming,
flying, and habitat behaviors.

The task also demonstrates Python's Method Resolution
Order (MRO), which determines the order in which
inherited methods are searched.



## Task 3: The Mystical Dragon - Mastering Mixins

The `dragon.py` module demonstrates reusable behavior
through mixin classes.

`SwimMixin` provides the `swim()` method, while
`FlyMixin` provides the `fly()` method.

The `Dragon` class inherits from both mixins and
defines its own `roar()` method.

This demonstrates how mixins can combine independent
capabilities without creating complex class hierarchies.

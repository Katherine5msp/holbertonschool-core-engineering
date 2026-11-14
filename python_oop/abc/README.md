
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

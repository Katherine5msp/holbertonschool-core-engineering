# Python – Inheritance & Polymorphism

## Overview

This project explores inheritance, method overriding, and
polymorphism in Python using parent and child classes.

## Task 0: Inheritance and Polymorphism Practice

File: `0-polymorphism_demo.py`

### Concepts Practiced

1. Parent classes
   - Created an Animal class with a speak() method.

2. Child classes
   - Created Dog and Cat classes inheriting from Animal.

3. Inherited methods
   - Observed how child classes reuse parent methods.

4. Method overriding
   - Overrode speak() in Dog and Cat to return different sounds.

5. Polymorphism
   - Used a list of different animal objects and called
     the same method on each object.

6. Class relationships
   - Used isinstance() to check object relationships.
   - Used issubclass() to check inheritance relationships.

## Expected Output

    Woof
    Meow
    Woof
    True
    True
    True

## Environment

- Ubuntu 20.04
- Python 3.8 (target environment)
- Python 3.9.5 (practice sandbox)

## Key Takeaway

Inheritance allows classes to reuse existing behavior.

Method overriding allows subclasses to customize inherited methods.

Polymorphism allows different objects to respond to the same
method call according to their class.

## Task 1: Base Geometry
File: `base_geometry.py`

Defines BaseGeometry with an area method that raises an exception
and a validator that accepts only positive integers.

## Task 2: Rectangle
File: `1-rectangle.py`

Defines Rectangle as a subclass of BaseGeometry.
Validates and stores private width and height attributes.

## Task 3: Full Rectangle
File: `2-rectangle.py`

Implements rectangle area calculation and string representation.

## Task 4: Square #1
File: `1-square.py`

Defines Square as a subclass of Rectangle, using one size value
for both dimensions.

## Task 5: Square #2
File: `2-square.py`

Customizes the square's string representation.

## Concepts Learned

- Inheritance and class hierarchies
- Method overriding and polymorphism
- Private attributes and name mangling
- Input validation and exception handling

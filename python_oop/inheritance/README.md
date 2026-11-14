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

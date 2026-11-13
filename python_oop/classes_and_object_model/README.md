# Python - Classes & Object Model

## Description

This project introduces Object-Oriented Programming (OOP)
in Python, focusing on classes, instances, attributes,
methods, encapsulation, and object representation.

## Learning Objectives

- Understand classes and instances.
- Create and initialize objects.
- Manage instance attributes.
- Implement instance methods.
- Apply encapsulation.
- Use getters and setters.
- Implement special methods.
- Understand object representation.

## Tasks

| Task | Description | Status |
|------|-------------|--------|
| 0 | Exploring Objects | Completed |
| 1 | My First Square | Locally validated |
| 2 | Square with Size | Locally validated |
| 3 | Size Validation | Locally validated |
| 4 | Area of a Square | Locally validated |
| 5 | Access and Update Private Attribute | Locally validated |
| 6 | Printing a Square | Locally validated |
| 7 | Print Square Instance | Locally validated |
| 8 | Rectangle Class | Locally validated |
| 9 | Area and Perimeter | Locally validated |

## Files

### Square
- 0-square.py
- 1-square.py
- 2-square.py
- 3-square.py
- 4-square.py
- 5-square.py
- 6-square.py

### Rectangle
- 1-rectangle.py
- 2-rectangle.py

## Environment

- Python 3.8 compatibility
- Ubuntu 20.04
- pycodestyle 2.7.0

## Validation

Tasks 1-9 have been implemented and locally tested.
Task 0 exploration completed.

Official Holberton grading is pending.
GitHub push is pending.

## Quiz Review: Python OOP Fundamentals

Object-Oriented Programming (OOP) organizes code around classes and
objects. A class is a blueprint that defines the structure and behavior
of objects, while an instance is an individual object created from
that class. Instances contain attributes, which store data, and
methods, which define behavior. Encapsulation controls access to
internal data through private attributes, properties, getters, setters,
and validation. Special methods such as `__str__()` define how an
object is represented as a readable string when passed to `print()`.

### Key Concepts

- **Class:** Blueprint used to create objects.
- **Instance:** An individual object created from a class.
- **Attributes:** Variables that store an object's data.
- **Methods:** Functions defined inside a class.
- **self:** Reference to the current instance.
- **__init__():** Initializes a newly created instance.
- **Encapsulation:** Organizes and controls access to internal data.
- **Private attributes:** Attributes using double-underscore naming,
  such as `self.__size`.
- **@property:** Provides controlled attribute access (getter).
- **Setter:** Validates and controls attribute updates.
- **__str__():** Returns a readable string representation of an object.

### Practical Examples

- `Square(5)` creates an instance of the Square class.
- `self.__size` stores an instance attribute.
- `area()` calculates the square's area.
- `perimeter()` calculates a rectangle's perimeter.
- `print(my_square)` invokes the object's `__str__()` method.

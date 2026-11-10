# Python - Exception Handling

This directory contains exercises on Python exception handling.

## Task 0: Safe list printing

The `safe_print_list` function prints a specified number of list elements,
handles IndexError when the requested number exceeds the list length,
and returns the number of elements successfully printed.

## Task 1: Safe integer printing

The `safe_print_integer` function attempts to print a value using
integer formatting. It returns True if printing succeeds and False
if the value cannot be formatted as an integer.

## Task 2: Safe integer list printing

The `safe_print_list_integers` function prints the first `x` elements
of a list, displaying only integers and skipping other data types.
It handles `IndexError`, `TypeError`, and `ValueError` exceptions
and returns the number of integers successfully printed.

## Task 3: Safe division

The `safe_print_division` function divides two numbers using
try and except to handle division by zero.
The finally block always prints the result, whether the division
succeeds or fails.
The function returns the division result or None if division fails.

## Task 4: Raise exception

The `raise_exception` function explicitly raises a TypeError
using Python's raise statement.
This task demonstrates how to trigger an exception intentionally.

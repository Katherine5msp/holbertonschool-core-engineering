# Task 8 – Reflection: Core Data Structures

## 1. Lists vs. Sets

I prefer lists when order matters, duplicates are allowed, or I need to access elements by index. Sets are useful when I need unique elements.

## 2. When to Use Tuples

A tuple is useful for storing fixed values that should not change, such as coordinates `(x, y)`. It makes the intention of keeping values unchanged clearer.

## 3. Updating Dictionaries

When a key already exists, assigning a new value replaces its previous value. When the key does not exist, Python adds a new key-value pair.

## 4. Edge Cases

The project functions handle several edge cases:

- Negative and out-of-range indexes.
- Tuples containing fewer than two elements.
- Empty sets with no common elements.
- Empty or `None` dictionaries.
- Existing and new dictionary keys.

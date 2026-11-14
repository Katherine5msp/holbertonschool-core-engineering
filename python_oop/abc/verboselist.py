#!/usr/bin/env python3
"""Extend the built-in list class with operation notifications."""


class VerboseList(list):
    """A list that announces when items are added or removed."""

    def append(self, item):
        """Append an item and display a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extend the list and display the number of items added."""
        items = list(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Announce and remove an item from the list."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Announce, remove, and return an item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

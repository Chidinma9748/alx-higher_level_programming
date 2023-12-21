#!/usr/bin/python3

""" Function that defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Create a new square.

        Args:
            size (int): The size of the new square.
        """
        if not is instance(size, int):
            raise TypeError("size must be an integer")
        else if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

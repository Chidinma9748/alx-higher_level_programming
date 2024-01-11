#!/usr/bin/python3
"""This function returns the list available attributes and methods."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))

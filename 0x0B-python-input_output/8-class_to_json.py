#!/usr/bin/python3
"This function returns dictionary description with simple data structures for JSON serialization of an object."


def class_to_json(obj):
    "Return the dictionary represntation of a simple data structure."
    return obj.__dict__

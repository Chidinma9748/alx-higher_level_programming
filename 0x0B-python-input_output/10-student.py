#!/usr/bin/python3
"This function defines a student based on 9-student.py."


class Student:
    "Represent a student."

    def __init__(self, first_name, last_name, age):
        "Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        "Get a dictionary representation of the Student.

        If attr is a list of strings, represents only those attributes
        included in the list.

        Args:
            attr (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

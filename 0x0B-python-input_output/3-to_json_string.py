#!/usr/bin/python3
"This functin returns the JSON representation of an object(string)"
import json


def to_json_string(my_obj):
    "Return the JSON representation of a string object."
    return json.dumps(my_obj)

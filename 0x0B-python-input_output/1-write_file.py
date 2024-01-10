#!/usr/bin/python3
"This function writes a string to text file(UTF8) and return the number of characters written"


def write_file(filename="", text=""):
    

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    ""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """
    Formats text by adding two newlines 
    after every occurrence of '?', ':', and '.'.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text is not a string.

    Returns:
        str: Formatted text with two newlines
        after each occurrence of '?', ':', and '.'.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        words = (delimeter + "\n\n").join([index.strip(" ") for index in words.split(delimeter)])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    print(append_write())

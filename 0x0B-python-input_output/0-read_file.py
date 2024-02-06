#!/usr/bin/python3
"""
Module to read files
"""


def read_file(filename=""):
    """Read files """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


if __name__ == "__main__":
    read_file()

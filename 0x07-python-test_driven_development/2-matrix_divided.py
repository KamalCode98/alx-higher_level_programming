#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): Matrix containing integers or floats.
        div (int or float): Divisor to divide the matrix by.

    Returns:
        list of lists: Matrix representing the result of the division.

    Raises:
        TypeError: If the matrix is not a list of lists containing integers
                   or floats.
        TypeError: If sublists in the matrix are not of the same size.
        TypeError: If the divisor is not an integer or float.
        ZeroDivisionError: If the divisor is zero.
    """
    matrixError = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(matrixError)
    if not isinstance(matrix, list):
        raise TypeError(matrixError)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(matrixError)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(matrixError)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(matrixError)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in lists] for lists in matrix]

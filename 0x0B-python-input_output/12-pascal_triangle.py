#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]  # Start with 1 at the beginning
        for j in range(1, i):
            # Calculate the value based on the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End with 1 at the end
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """Print the Pascal's triangle."""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []  # Return an empty list if n is not positive

    triangle = [[1]]  # Initialize triangle with the first row

    for i in range(1, n):
        row = [1]  # Start the row with 1
        for j in range(1, i):
            # Calculate the value based on the sum of the two values above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End the row with 1
        triangle.append(row)  # Add the completed row to the triangle

    return triangle

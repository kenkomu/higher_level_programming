#!/usr/bin/python3
""" pascal_triangle module """


def pascal_triangle(n):
    """
        Function that define a Pascal triangle
        Args:
            n: size of the triangle
    """

    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(n):
            if (j > i):
                break
            if i > 0 and len(triangle) == i and len(triangle[i - 1]) > j:
                y = triangle[i - 1][j]
            elif len(triangle) >= i:
                y = 0
            if (
                i > 0 and len(triangle) > i - 1 and
                j > 0 and len(triangle[i - 1]) > j - 1
            ):
                x = triangle[i - 1][j - 1]
            else:
                x = 0
            if x == 0 and y == 0:
                row.append(1)
            else:
                row.append(x + y)
        triangle.append(row)

    return triangle

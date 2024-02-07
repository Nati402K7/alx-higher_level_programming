#!usr/bin/python3
"""defining fuction"""
def pascal_triangle(s):
    """Represent pascal's Triangle of sizen.
    Return list of integers
    """
    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangle) != n:
        tri = tringles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i]  = tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangle

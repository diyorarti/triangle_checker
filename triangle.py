def is_triangle(a, b, c):
    """Returns True if a, b, c can form a triangle, else False."""
    return a + b > c and b + c > a and a + c > b

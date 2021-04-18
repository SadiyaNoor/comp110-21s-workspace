"""Examples of object-oriented programming concepts."""
"""Lesson notes."""

class Point:

    # Defining attributes (related variable)
    # of our class
     x: float 
     y: float

     def __init__(self, x: float, y: float):
        """Constructs a point by giving x and y arguments."""
         self.x = x
         self.y = y

a: Point = Point(4.0 , 5.0)
print(a)

b: Point = Point(0.0, 0.0)
# Assign to attributes of an object:
b.x = 2.0
b.y = -1.0
print(b)
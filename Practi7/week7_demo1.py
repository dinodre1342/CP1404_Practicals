"""
Each class starts with the keyword of "class"
We define a meaningful name for the class we are designing.
class name convention: Capitalise first letter.
eg. Point, Student, Car
class definition ends with a colon.
"""
class Point:
    """
    Each class starts with the keyword of "class"
    We define a meaningful name for the class we are designing.
    class name convention: Capitalise first letter.
    eg. Point, Student, Car
    class definition ends with a colon.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.size = 1
        print("Point is initialising.")

    def __str__(self):
        return "Point ({},{})".format(self.x,self.y)

pointA = Point(9, 80) # pointA is an instance of Point
#pointB = Point()
print(pointA)
pointB = Point()
print(pointB)

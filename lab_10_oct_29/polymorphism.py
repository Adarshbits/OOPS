"""
Multiple Inheritance and Method Resolution Order (MRO)
This program demonstrates multiple inheritance and how Python resolves method calls.
Square class inherits from both Shape and Color classes, and its own method takes precedence.
The Method Resolution Order determines which method is called when multiple classes define the same method.
"""

class shape:
    def sides(self):
        print("not defined")
class color:
    def sides(self):
        print("red")
class square(shape, color):
    def sides(self):
        print("4 sides")

obj = square()
obj.sides()
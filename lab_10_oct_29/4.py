"""
Operator Overloading Demonstration
This program demonstrates operator overloading by customizing the "+" operator.
The Score class uses the __add__() special method to define how two Score objects
should be combined. When you use + between two Score objects, it adds their marks.
"""

class Score:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        return Score(self.marks + other.marks)

    def display(self):
        print("Total Marks:", self.marks)

s1 = Score(75)
s2 = Score(85)
s3 = s1 + s2
s3.display()

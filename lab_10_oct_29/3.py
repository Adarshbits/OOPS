"""
Method Overloading using Default Arguments
This program demonstrates method overloading in Python using default parameters.
The calculate() method can handle different numbers of arguments (1, 2, or 3 marks)
by using default values. This allows the same method to work with varying input.
"""

class grade:
    def calculate(self, m1=50, m2=0, m3=0):
        print("total marks =", m1+m2+m3)

s1 = grade()
s1.calculate(90)
s1.calculate()
s1.calculate(20, 90)
s1.calculate(60, 70, 80)
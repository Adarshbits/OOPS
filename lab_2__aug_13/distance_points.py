"""
Euclidean Distance Calculator
This program calculates the distance between two points in a 2D coordinate system.
Uses the formula: distance = sqrt((x2-x1)² + (y2-y1)²)
"""

x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))

dist = ((x2-x1)**2 + (y2-y1)**2)**(0.5)
print("distance b/w points =", dist)
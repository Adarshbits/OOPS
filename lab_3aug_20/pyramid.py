"""
Number Pyramid Pattern
This program prints a descending number pyramid pattern.
Pattern: 54321, 5432, 543, 54, 5
Uses nested loops to create the decreasing sequence.
"""

for i in range(1, 6, 1):
    for j in range(5, i-1, -1):
        print(j,"  ", end="")
    print()
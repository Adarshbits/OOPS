"""
Multiplication Table Generator
This program generates and displays the multiplication table for a given number.
The table shows products from 1 to 10 using a for loop.
"""

n = int(input("enter n : "))
print("\ntable of", n, ":")
for i in range(1, 11, 1):
    print(n, "x", i, "=", n*i)
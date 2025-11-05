"""
Largest and Smallest Number Finder
This program accepts 10 integers from the user and stores them in a list.
It then finds and displays the largest and smallest numbers using built-in functions.
"""

l=[]
for i in range(0, 10):
    n = int(input("enter int : "))
    l.append(n)
print("largest = ", max(l))
print("smallest = ", min(l))


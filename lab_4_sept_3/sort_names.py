"""
Name Sorting Program
This program accepts 5 names from the user and stores them in a list.
The names are then sorted alphabetically using the sort() method.
"""

l=[]
for i in range(0, 5):
    name = input("enter name : ")
    l.append(name)
l.sort()
print(l)
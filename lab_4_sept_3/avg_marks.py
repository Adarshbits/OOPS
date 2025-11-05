"""
Average Marks Calculator
This program calculates the average of marks entered by the user.
The user specifies the number of subjects and enters marks for each.
The average is calculated by dividing the sum by the count.
"""

import math as m
l=[]
n = int(input("enter no of subjects : "))
for i in range(0, n):
    m = int(input("enter marks : "))
    l.append(m)
print("Average marks = ", sum(l)/len(l))

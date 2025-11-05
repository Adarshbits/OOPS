"""
Sum of Digits Calculator
This program calculates the sum of all digits in a given number.
Uses a while loop to extract digits using modulo and division operations.
"""

n=int(input("enter n : "))
sum=0
while n>0:
    rem=n%10
    n=n//10
    sum+=rem
print("sum of digits =", sum)
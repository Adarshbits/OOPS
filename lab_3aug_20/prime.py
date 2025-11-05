"""
Prime Number Checker
This program determines whether a given number is prime or not.
A prime number is only divisible by 1 and itself.
The algorithm checks divisibility from 2 to n-1.
"""

n = int(input("enter n : "))
count=0
for i in range(2, n, 1):
    if n%i==0:
        count+=1
    else: pass
if count==0:
    print("prime")
else:
    print("not prime")
    
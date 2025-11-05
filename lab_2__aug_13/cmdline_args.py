"""
Command Line Arguments Calculator
This program takes two numbers as command line arguments and calculates their sum.
Uses sys.argv to access command line arguments passed to the script.
"""

import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
sum = x+y
print(sum)

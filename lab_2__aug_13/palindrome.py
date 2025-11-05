"""
Palindrome Checker
This program checks if a given string reads the same forwards and backwards.
A palindrome is a word, phrase, or sequence that reads the same backward as forward.
"""

s = input("enter string : ")
rev = s[::-1]
if (s==rev):
    print("palindrome")
else:
    print("not palindrome")
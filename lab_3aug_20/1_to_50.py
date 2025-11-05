"""
FizzBuzz Game Implementation
This program prints numbers from 1 to 50 with special replacements:
- Numbers divisible by 3: print "figg"
- Numbers divisible by 5: print "buzz"
- Numbers divisible by both 3 and 5: print "figgbuzz"
This is a variation of the classic FizzBuzz programming problem.
"""

for i in range(1, 51, 1):
    if i%3==0 and i%5==0:
        print(i,"- figgbuzz")
    elif i%3==0:
        print(i,"- figg")
    elif i%5==0:
        print(i,"- buzz")
    else: pass
"""
Student Average Marks Calculator
This function calculates the average of marks across three subjects.
Default parameters (set to 0) handle cases where a student missed a test.
If a subject mark is not provided, it defaults to 0 for the average calculation.
"""

def avg(sub1=0, sub2=0, sub3=0):
    total_marks = sub1 + sub2 + sub3
    average = total_marks / 3
    return average

print("Average marks of student 1:", avg(50, 60, 70))
print("Average marks of student 2 (missed one test):", avg(50, 70))
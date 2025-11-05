"""
Student Record Function
This function demonstrates the use of:
- Regular parameter (course)
- Variable-length positional arguments (*subjects) for multiple subjects
- Keyword arguments (**details) for student information like name, age, grade
All three types of parameters are used in a single function call
"""

def stuRecord(course, *subjects, **details):
    print("Course:", course)
    print("Subjects:", subjects)
    print("Student Details:", details)
    
stuRecord("btech", "math", "oops", "dsa", name="bhavishya", age=19)
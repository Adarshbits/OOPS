"""
Student Grade Management System
This class manages student information including:
- Student name
- Roll number
- Marks (out of 100)
The grade() method determines pass/fail status:
- Pass: marks >= 40
- Fail: marks < 40
- Invalid: marks outside 0-100 range
"""

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def Display(self):
        print("name :", self.name)
        print("roll no :", self.roll_no)
        print("marks :", self.marks)
        print()
    
    def grade(self):
        if self.marks > 100 or self.marks < 0:
            print("Invalid marks")
        elif self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

student1 = Student("bhavishya", 123, 90)
student1.grade()
student1.Display()
student2 = Student("aryan", 456, 555)
student2.grade()
student2.Display()
student3 = Student("rahul", 789, 39)
student3.grade()
student3.Display()

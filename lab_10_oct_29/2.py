"""
Method Overriding Demonstration
This program demonstrates method overriding in inheritance:
- Base class Person has a getrole() method
- Derived classes Student and Staff override getrole() with their own implementations
Each class provides its own version of the method, showing polymorphism at work.
"""
class person:
    def getrole(self):
        print("I am a person")

class student(person):
    def getrole(self):
        print("I am a student")
        
class staff(person):
    def getrole(self):
        print("I am a staff member")

p = person()
p.getrole()
stu = student()
stu.getrole()
staf = staff()
staf.getrole()
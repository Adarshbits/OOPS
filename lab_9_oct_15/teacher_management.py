"""
School Management System using Inheritance
Three-tier hierarchy:
1. Person (base class): name and age
2. Teacher (inherits Person): teaches multiple classes
3. Class Teacher (inherits Teacher): manages a specific class
Each level adds its own attributes and methods while inheriting from parent classes.
"""

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_person(self):
        print(self.name)
        print(self.age)

class teacher(person):
    def __init__(self, name, age, teaches_classes):
        super().__init__(name, age)
        self.teaches_classes = teaches_classes
    def print_teacher(self):
        super().print_person()
        print(self.teaches_classes)

class class_teacher(teacher):
    def __init__(self, name, age, teaches_classes, class_teacher_of):
        super().__init__(name, age, teaches_classes)
        self.class_teacher_of = class_teacher_of
    def print_class_teacher(self):
        super().print_teacher()
        print(self.class_teacher_of)

class_teacher1 = class_teacher("bhavishya", 25, ["A", "C", "K"], "K")
class_teacher1.print_class_teacher()
print()
class_teacher1.print_person()
print()
regular_teacher = teacher("aryan", 40, ["G"])
regular_teacher.print_teacher()
"""
Employee Management System using Inheritance
- Base class: Person (name, age)
- Employee class extends Person with employee_id and salary
- Manager class uses multi-level inheritance from Employee, adds department
- Trainer class uses multiple inheritance from Employee and Certification
- All classes have display methods to show complete information
"""

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_person(self):
        print(self.name)
        print(self.age)

class emp(person):
    def __init__(self, name, age, emp_id, sal):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.sal = sal
    def print_emp(self):
        super().print_person()
        print(self.emp_id)
        print(self.sal)

class manager(emp):
    def __init__(self, name, age, emp_id, sal, dept):
        super().__init__(name, age, emp_id, sal)
        self.dept = dept
    def print_manager(self):
        super().print_emp()
        print(self.dept)

class certification:
    def __init__(self, cert):
        self.cert = cert
    def print_cert(self):
        print(self.cert)
class trainer(emp, certification):
    def __init__(self, name, age, emp_id, sal, cert):
        emp.__init__(self, name, age, emp_id, sal)
        certification.__init__(self, cert)
    def print_trainer(self):
        emp.print_emp(self)
        certification.print_cert(self)

manager_obj = manager("Bhavishya", 19, 12345, 1000000, "CSE")
manager_obj.print_manager()
print()
trainer_obj = trainer("Aryan", 25, 67890, 50000, "IT")
print("Trainer Details:")
trainer_obj.print_trainer()
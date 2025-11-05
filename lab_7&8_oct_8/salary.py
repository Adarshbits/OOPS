"""
Employee Salary Slip Generator
This program creates employee salary slips with the following calculations:
- Base salary is the starting amount
- Daily Allowance (DA): 20% of base salary
- House Rent Allowance (HRA): 15% of base salary
- Total salary = Base + DA + HRA
The display method shows all employee information and calculated totals.
"""

class salary_slip:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_salary(self):
        daily_allowance = self.salary * 0.20
        house_rent = self.salary * 0.15
        total_sal = self.salary + daily_allowance + house_rent
        return total_sal

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Base Salary:", self.salary)
        print("Total Salary (with allowances):", self.calculate_salary())
        print()

emp1 = salary_slip("bhavishya", 12345, 100000)
emp2 = salary_slip("aryan", 67890, 12000)
emp1.display()
emp2.display()
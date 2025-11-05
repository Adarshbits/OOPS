"""
Bonus Calculation Function
This function computes the final salary after applying a bonus percentage.
Demonstrates both positional and keyword argument usage.
Default bonus rate is 10% if not specified.
"""

def bonus(salary, rate=0.10):
    calculated_bonus = salary * rate
    total_salary = salary + calculated_bonus
    return total_salary

# Example 1: Positional arguments
result1 = bonus(50000, 0.15)
print("Salary with bonus (positional):", result1)

# Example 2: Keyword arguments
result2 = bonus(rate=0.12, salary=60000)
print("Salary with bonus (keyword):", result2)

"""
Error demonstration - incorrect argument order:
print(bonus(rate=0.10, 10000))
This results in SyntaxError because positional argument cannot follow keyword argument
"""
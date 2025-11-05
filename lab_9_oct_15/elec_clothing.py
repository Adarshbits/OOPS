"""
Online Store Product Management System
This program demonstrates inheritance with a base Product class and two derived classes:
- Electronics: inherits from Product, adds brand and warranty attributes
- Clothing: inherits from Product, adds size and fabric_type attributes
Each derived class has its own display method to show product-specific information.
"""

class product:
    def __init__(self, p_id):
        self.p_id = p_id

class electronics(product):
    def __init__(self, p_id, brand, warrenty):
        self.brand = brand
        self.warrenty = warrenty
        super().__init__(p_id)
    def print_elec(self):
        print(self.p_id)
        print(self.brand)
        print(self.warrenty)

class clothing(product):
    def __init__(self, p_id, size, fabric_type):
        self.size = size
        self.fabric_type = fabric_type
        super().__init__(p_id)
    def print_clo(self):
        print(self.p_id)
        print(self.size)
        print(self.fabric_type)

obj1 = electronics(12345, "samsung", "2 yrs")
obj1.print_elec()
print()
obj2 = clothing(67890, "large", "silk")
obj2.print_clo()
"""
Cafe Bill Calculator
This function processes multiple ordered items using variable-length arguments.
Each item is a tuple containing (item_name, item_price).
The function sums all item prices and returns the total bill amount.
"""

def totalBill(*items):
    total = 0
    for item in items:
        total += item[1]
    print("Total bill:", total)
    return total

totalBill(("bread", 20), ("brush", 10), ("apple", 40))

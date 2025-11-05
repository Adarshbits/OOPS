"""
E-Commerce Discount Calculator
For frequently used discount calculations, a lambda function is used
instead of defining a regular function. This reduces code repetition.
The function calculates the final price after applying discount percentage.
"""

price = 100
discount_percent = 23
applyDiscount = lambda price, discount: price * (1 - discount / 100)
final_price = applyDiscount(price, discount_percent)
print("Final price after discount:", final_price)
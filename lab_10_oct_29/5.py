"""
Comprehensive Polymorphism Demonstration
This program demonstrates all three types of polymorphism:
1. Method Overriding: Animal, Dog, Cat classes with speak() method
2. Method Overloading: Calculator class with add() method using default parameters
3. Operator Overloading: Score class with __add__() and __repr__() special methods
Each type is demonstrated with practical examples and output.
"""

class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

class Score:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Score(self.value + other.value)
    
    def __repr__(self):
        return f"Score(value={self.value})"

print("Method Overriding")
my_dog = Dog()
my_cat = Cat()
my_dog.speak()
my_cat.speak()

print("\nMethod Overloading")
calc = Calculator()
print(f"Two args: {calc.add(5, 10)}")
print(f"Three args: {calc.add(5, 10, 20)}")

print("\nOperator Overloading")
s1 = Score(80)
s2 = Score(90)
s3 = s1 + s2
print(f"{s1} + {s2} = {s3}")

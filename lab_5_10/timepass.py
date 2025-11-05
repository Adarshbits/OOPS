"""
Tuple with Mutable Elements Demonstration
This program demonstrates that while tuples are immutable, they can contain mutable elements
like dictionaries and lists. The mutable elements within the tuple can be modified.
"""

t=(1, 2, {"name":"bhavishya", "age":19}, [1, 2, 3, 4])
print(t)
t[2]["name"]="bhavishya pawar"
print(t)
t[3][0]=0
print(t)
"""
Area Calculation Function
This function calculates the area of a shape:
- If only length is provided: calculates square area (length × length)
- If both length and width are provided: calculates rectangle area (length × width)
Uses default parameter to distinguish between square and rectangle calculations.
"""

def area(length, width=None):
    if width is None:
        # When width is not provided, shape is a square
        calculated_area = length * length
        print("Area of square =", calculated_area)
        return calculated_area
    else:
        # When both dimensions provided, shape is a rectangle
        calculated_area = length * width
        print("Area of rectangle =", calculated_area)
        return calculated_area

area(5, 10)
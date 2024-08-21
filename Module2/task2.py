# Second Question Write a program that asks the user for the radius
# of a circle and the prints out the area of the circle.

import math

radius = int(input("Enter a radius: "))
area = math.pi * radius**2
print(f"The area of the circle is {area: .5f}")
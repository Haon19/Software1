#Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza
#in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the
#user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money
#(which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.
import math

def pizza_value(diameter,price):
    area = math.pi * (diameter/2) ** 2
    value = price / area
    return value

p1_price = float(input("Enter the price of pizza1: "))
p1_diameter = float(input("Enter the diameter of pizza1 in meters: "))
p2_price = float(input("Enter the price of pizza2: "))
p2_diameter = float(input("Enter the diameter of pizza2 in meters: "))

if pizza_value(p1_diameter, p1_price) > pizza_value(p2_diameter, p2_price):
    print("The pizza2 is better value")
else:
    print("pizza1 is better value")
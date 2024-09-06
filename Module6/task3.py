#Write a function that gets the quantity of gasoline in American gallons and returns the
#number converted to litres. Write a main program that asks for a volume in gallons from the
#user and converts the value to liters. The conversion must be done by using the function.
#Conversions continue until the user inputs a negative value.

def gallons_to_litters():
    gallons = float(input("enter gallons:"))
    while gallons >= 0:
        litters = gallons * 3.9
        print(litters)
        gallons = float(input("enter gallons:"))
gallons_to_litters()
#Write a program that converts inches to centimeters until the user inputs a negative value.
#Then the program ends.
x = float(input("enter inches:"))
while x >= 0:
    print(f"{x*2.54}cm")
    x = float(input("enter inches:"))

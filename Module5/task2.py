#Write a program that asks the user to enter numbers until they input an empty string to quit.
#At the end, the program prints out the five greatest numbers sorted in descending order.
#Hint: You can reverse the order of sorted list items by using the sort method with the
#reverse=True argument.

import math

largest_number = -math.inf
smallest_number = math.inf


line = input("enter number:")
x = float(line)
list_of_numbers = []

while line != "":
    x = float(line)
    line = input("enter number:")
    list_of_numbers = list_of_numbers + [x]

    if len(list_of_numbers) < 6:
        list_of_numbers.sort(reverse=True)

    if len(list_of_numbers) >= 6:
        list_of_numbers.sort(reverse=True)
        list_of_numbers.pop(5)


print(list_of_numbers)
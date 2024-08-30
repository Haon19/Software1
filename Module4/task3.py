#Write a program that asks the user to enter numbers until they enter an empty string to quit.
#Finally, the program prints out the smallest and largest number from the numbers it received.
import infinity

largest_number = -2147483648
smallest_number = 2147483647

line = input("enter number:")
list_of_numbers = line
x = float(line)

while line != "":
    x = float(line)

    line = input("enter number:")

    list_of_numbers = list_of_numbers + ", " + line

    if x > largest_number:
        largest_number = x

    if x < smallest_number:
        smallest_number = x

print(list_of_numbers)
print("the largest number imputed was", largest_number)
print("the smallest number imputed was", smallest_number)
# Fourth Question. Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
z = int(input("Enter your third number: "))

sum = x + y + z
product = x * y * z
average = sum / 3


print("The sum of your numbers is",sum)
print("The product of your numbers is",product)
print("The average is",average)
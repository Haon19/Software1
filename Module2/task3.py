# Third Question. Write a program that asks the user for the length
# and width of a rectangle. The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.

length = int(input("Enter a length: "))
width = int(input("Enter a width: "))

perimeter = 2 * length * width

print("The perimeter is ", perimeter)
#Write a program that asks the user how many dice to roll. The program rolls all the dice
#once and prints out the sum of the numbers. Use a for loop.

import random

dice = int(input("enter a number of dice to role: "))
x = random.randint(1, 6)
y = 0
for i in range(dice):
    x = random.randint(1,6)
    print("dice",i+1, "=", x )
    y = y + x
    i += 1
print("sum", y)
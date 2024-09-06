#Write a program that asks the user for an integer and tells if the number is a prime number.
#Prime numbers are number that are only divisible by one or the number itself.

#For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
#On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

number = int(input("enter a number you wish to know if it is prime:"))

if number <= 1:
    print("Not prime")
    exit()

if number == 2:
    print("Prime")
    exit()

i = number - 1

while i >= 2:
    if number % i == 0:
        is_prime = False
        break
    else:
        is_prime = True
    i -= 1

if is_prime == False:
    print("Not prime")
if is_prime == True:
    print("Prime")
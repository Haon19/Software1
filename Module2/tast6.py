# Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.

from random import randint

random1 = randint(100, 999)
random2 = randint(1, 6) + 10 * randint(1, 6) + 100 * randint(1, 6) + 1000 * randint(1, 6)
print(random1)
print(random2)

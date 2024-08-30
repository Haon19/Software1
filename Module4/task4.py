#Write a game where the computer draws a random integer between 1 and 10. The user tries to
#guess the number until they guess the right number. After each guess the program prints
#out a text: Too high, Too low or Correct. Notice that the computer must not change the number
#between guesses.

import random

answer = random.randint(1, 10)
guess = int(input("guess:"))
if guess == answer:
    print("Correct!")
if guess > answer:
    print("Too high!")
if guess < answer:
    print("Too low!")

while guess != answer:
    guess = int(input("guess:"))
    if guess == answer:
        print("Correct!")
    if guess > answer:
        print("Too high!")
    if guess < answer:
        print("Too low!")
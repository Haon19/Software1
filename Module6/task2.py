#Modify the function above so that it gets the number of sides on the dice as a parameter.
#With the modified function you can for example roll a 21-sided role-playing dice. The difference
#to the last exercise is that the dice rolling in the main program continues until the program
#gets the maximum number on the dice, which is asked from the user at the beginning.

def roll_weird_dice(j):

    import random

    x = random.randint(1, j)

    while x != j:
        print(x)
        x = random.randint(1, j)

    print(x)

i = int(input("Enter how many sides your dice has: "))
roll_weird_dice(i)
#    Write a program that asks the user to enter the cabin class of a cruise ship and then
#    prints out a written description according to the list below. You must use an if/elif/else
#    structure in your solution.
#
#    LUX: upper-deck cabin with a balcony.
#    A: above the car deck, equipped with a window.
#    B: windowless cabin above the car deck.
#    C: windowless cabin below the car deck.
#
#    If the user enters an invalid cabin class, the program outputs an error message
#    Invalid cabin class.

cabin_class = input("What is the cabin class of your cruise ship?")

if cabin_class == "LUX":
    print("upper-deck cabin with a balcony.")
    exit()
elif cabin_class == "A":
    print("above the car deck, equipped with a window.")
    exit()
elif cabin_class == "B":
    print("windowless cabin above the car deck.")
    exit()
elif cabin_class == "C":
    print("windowless cabin below the car deck.")
    exit()

print("Invalid cabin class.")
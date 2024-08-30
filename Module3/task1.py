#Write a program that asks a fisher the length of a zander in centimeters.
#If the zander does not fulfill the size limit, the program instructs to
#release the fish back into the lake and notifies the user of how many centimeters
#below the size limit the caught fish was. A zander must be 42 centimeters or longer
#to meet the size limit.

zander_lenght = float(input("How long is you zander in centimeters:"))

if zander_lenght < 42:
    print("You must return the fish")
    x = 42 - zander_lenght
    print("The fish is", x , "cm too short")
#Fifth Question. Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input
# to full kilograms and grams and outputs the result to the user:

talents = float(input("Enter how many talents: "))
pounds = float(input("Enter how many pounds: "))
lots = float(input("Enter how many lots: "))

pounds1 = talents * 20

lots1 = pounds * 32
lots2 = pounds1 * 32

grams1 = lots1 * 13.3
grams2 = lots2 * 13.3
grams3 = lots * 13.3

total_kilos = grams1 + grams2 + grams3
grams = total_kilos % 1000
kilograms = int((total_kilos - grams)/1000)
print("The weight in modern units:", kilograms,f"kg and{grams: .2f} g")
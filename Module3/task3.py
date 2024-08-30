#Write a program that asks for the biological gender and hemoglobin value (g/l).
#The program the notifies the user if the hemoglobin value is low, normal or high.

#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.

gender = input("Enter your gender M/F: ")
hemoglobin = float(input("Enter your hemoglobin in units (g/l): "))

if gender == "M":
    if 167 >= hemoglobin >= 134:
        print("Hemoglobin is good")
    else:
        print("Hemoglobin is bad")

if gender == "F":
    if 155 >= hemoglobin >= 117:
        print("Hemoglobin is good")
    else:
        print("Hemoglobin is bad")
#Write a program that asks the user for a number of a month and then prints out the corresponding season
#(spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each
#season to last three months, December being the first month of winter.

seasons = ("winter", "spring", "summer", "autumn")

month = int(input("What month of the year is it expressed as a number: "))

if month == 12:
    print(seasons[0])
else:
    s = int(month//3)
    print(seasons[s])
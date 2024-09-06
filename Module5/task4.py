#Write a program that asks the user to enter the names of five cities one by one
#(use a for loop for reading the names) and stores them into a list structure.
#Finally, the program prints out the names of the cities one by one, one city per line,
#in the same order they were read as input. Use a for loop for asking the names and a for/in
#loop to iterate through the list.

cities = []
for i in range (1,6):
    city = input("enter city name:")
    cities.append(city)
for j in range (0,5):
    print(cities[j])
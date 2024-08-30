#Write a program that asks the user for a username and password. If either or both are incorrect,
#the program ask the user to enter the username and password again. This continues until the login
#information is correct or wrong credentials have been entered five times. If the information is
#correct, the program prints out Welcome. After five failed attempts the program prints out Access
#denied. The correct username is python and password rules.

username = "python"
password = "rules"
i = 1

while i <= 5:
    i += 1

    x = input("username:")
    y = input("password:")

    if x == username and y == password:
        print("Welcome.")
        exit()
print("Access denied.")
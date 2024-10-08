#Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
#fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks
#the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead,
#the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit,
#the program execution ends. The user can choose a new option as many times they want until they choose to quit.
#(The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport
#is EFHK. You can easily find the ICAO codes of different airports online.)

print("write 'info' for fetching information of an existing airport\n 'new' for  entering a new airport\n 'quit' to stop the script")
ICAO = {"EFHK":"Helsinki-Vantaa Airport"}


choice=input("Enter your choice: ")

def info():
    icao_info=input("enter the ICAO code: ")
    print(ICAO[icao_info])
    return 0

def new():
    icao_new=input("enter the ICAO code: ")
    name_new=input("enter the name of the airport: ")
    ICAO[icao_new]=name_new
    return 0

while choice!="quit":

    if choice=="info":
        info()
    elif choice=="new":
        new()
    else:
        print("you can use only quit, info, new commands")

    #print(choice)
    choice = input("Enter your choice: ")

print("quit command entered, script stopped")
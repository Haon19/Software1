#Write a function that gets a list of integers as a parameter. The function returns a second
#list that is otherwise the same as the original list except that all uneven numbers have been
#removed. For testing, write a main program where you create a list, call the function, and then
#print out both the original as well as the cut-down list.

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

def remove_odds(list_of_numbers):
    i = 0
    even_list = []
    while i < len(list_of_numbers):

        if list_of_numbers[i] % 2 == 0:
            even_list.append(list_of_numbers[i])

        i += 1

    return even_list

print(remove_odds(list_of_numbers))

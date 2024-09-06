#Write a function that gets a list of integers as a parameter. The function returns the sum
#of all the numbers in the list. For testing, write a main program where you create a list,
#call the function, and print out the value it returned.

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

def sum_of_your_mom(list_of_numbers):
    i = 0
    sum_1 = 0
    while i < len(list_of_numbers):
        sum_1 = list_of_numbers[i] + sum_1
        i += 1
    return sum_1

print(sum_of_your_mom(list_of_numbers))

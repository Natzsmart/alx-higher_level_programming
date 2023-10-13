#!/usr/bin/python3
def print_list_integer(my_list=[]): #Define a function called print_list_integer that takes a list as an argument. The default value for the list is set to None.
    for i in range(len(my_list)): # Iterate over the indices of the list.
        print("{:d}".format(my_list[i])) # Print the value at each index of the list as an integer.

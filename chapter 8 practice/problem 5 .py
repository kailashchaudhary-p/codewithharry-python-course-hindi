# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *
def print_pattern(n):#define function to print pattern
    if  n==0:#base case
        return
    else:#recursive case 
        print('*'*n)#print stars
        print_pattern(n-1)#call function recursively with n -1
num = int(input("Enter a natural number:"))#take input from user
print_pattern(num)#call function to print pattern
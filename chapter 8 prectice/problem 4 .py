#Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_natural_numbers(n):#define function to calculate sum of first n natural numbers
    if n == 1:#base case
        return 1
    else:#recursive case
        return n + sum_of_natural_numbers(n -1)#return sum of first ntural numbers
num = int(input("Enter a natural number:"))#take input from user


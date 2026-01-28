#Write a program to print multiplication table of a given number using for loop.
num= int(input("Enter the number to print tht multiplication table:"))#Take input from the user
for i in range(1,11):#use for loop to iterate from 1 to 10
    print((f"{num} x {i} = {num*i}"))#print the multiplication table

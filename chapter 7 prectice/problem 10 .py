#Write a program to print multiplication table of n using for loops in reversed order
n = int(input("Enter the number "))
for i in range(10, 0, -1):#use for loop to iterate from 10 to 1
    print(f"{n} x {i} = {n*i}")#print multiplication table in formatted string
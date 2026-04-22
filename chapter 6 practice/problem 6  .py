#Write a program to calculate the factorial of a given number using for loop.
num=int(input("Enter a nuber whuch you find factorial of:"))#use unput function
f=1
for i in range(1,num+1):#use for loop to iterate through numbers
    f=f*i
print(f"The factorial of {num} is {f}")#print the factorial value   

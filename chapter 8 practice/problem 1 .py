#Write a program using functions to find greatest of three numbers.
def greatest_of_three(num1,num2,num3):#use function to find greatest of three numbers
    num1=int(input("Enter first number: "))#take input from user for first number
    num2=int(input("Enter second number: "))#take input from user for second number
    num3=int(input("Enter third number: "))#take input from user for third number
    if (num1 >= num2) and (num1 >= num3):#use if statement to compare three numbers
        return num1
    elif (num2 >= num1) and (num2 >= num3):#use elif statement to compare three numbers
        return num2
    else:#use else statement to return the greatest number
        return num3
    greatest_of_three(num1,num2,num3)
print("The greatest number is:",greatest_of_three(0,0,0))#
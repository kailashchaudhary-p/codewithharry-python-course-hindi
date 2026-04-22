#Write a program to find whether a given number is prime or not.
num=int(input("Enter the number:"))
i=2
while 1<num:
    if num%i==0:
        print("The number is not prime")
        break
    i=i+1
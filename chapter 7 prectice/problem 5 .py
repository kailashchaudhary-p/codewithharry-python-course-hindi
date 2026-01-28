#Write a program to find whether a given number is prime or not.
num= int(input('Enter a number:'))
i=2
while i<num:#use while loop to check for prime number 
    if num%i==0:
        print("The number is not prime")#print statement if the number is not prime
        break#break statement to exit the loop
    i=i+1
else:
    print("The number is prime")#print statement if the number is prime
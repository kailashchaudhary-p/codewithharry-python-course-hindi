#Write a program to find the greatest of four numbers entered by the user.
a = int(input("Enter the first No.:"))#use input function with int to take it in t=integer form 
b = int(input("Enter the second No.:"))#use input function with int to take it in t=integer form 
c = int(input("Enter the third No.:"))#use input function with int to take it in t=integer form 
d = int(input("Enter the fourth No.:"))#use input function with int to take it in t=integer form 

#compare thre number using a IF statements
#start the if block for a
if a>b and a>c and a>d:
    print("The greatest No. is:",a) #end of the if block
#start the if blockfor b
if b>a and b>c and b>d:
    print("The greatest No. is:",b)  #end of the if block
#start the if block for c
if c>b and c>a and c>d:
    print("The greatest No. is:",c) #end of the if block
#start the if block for d
if d>b and d>c and d>a:
    print("The greatest No. is:",d) #end of the if block
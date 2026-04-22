#Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3
num=3
for i in range(1,num+1):#Use for loop to iterate through rows
    for j in range(1,2*i):#Use nested for loop to iterate through columns
        print("*",end="")#Print star without new line
    print()#Print new line after each row
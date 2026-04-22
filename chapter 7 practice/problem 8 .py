# Write a program to print the following star pattern: 
# *
# **
# *** for n = 3
num = 3
for i in range(1, num+1): # use loop for rows 
    for j in range(1, i+1):#use nested loop for columns
        print("*",end="")#print star without new line 
    print()#print new line after each row

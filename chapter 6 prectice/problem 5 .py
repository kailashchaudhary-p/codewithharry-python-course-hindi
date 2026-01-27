#Write a program which finds out whether a given name is present in a list or not.
name=["ali","ram","harish","lakshit"]#create the list which contain the names
a = input("Enter the name to be serched:")#take input from user
if  a in name:#use if statement to check the name is present in the list or not
    print("the name is present in the list")
elif a not in name:#use elif statement to check the name is present in the list or not
    print("the name is not present in the list")
#Write a program to find whether a given username contains less than 10 characters or not.
username= input("Enter the user username:")#input function for enter the username 
if len(username)<10:#ise if satatement to check the length of username
    print("the user name is less than 10 characters")
elif len(username)==10:#use elif statement to check the length of username
    print("the user name is equal to 10 characters")

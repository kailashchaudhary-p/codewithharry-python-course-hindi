#Write a program to find out whether a given post is talking about “Harry” or not.
post=input("Enter the post:")#take input from user
if "harry".lower() in post.lower():#use if statement to check whether the post is regarding harry or not
    print("the post is regarding harry")
else:
    print("the post is not regarding harry")
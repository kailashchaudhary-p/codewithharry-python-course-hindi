#A spam comment is defined as a text containing following keywords:
#“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
t=input("Enter the text:")
if("Make a lot of money" in t)or("buy now" in t)or("subscribe this" in t)or("click this" in t):
    print("this is smap comments")
else:
    print("This is not spam comment")
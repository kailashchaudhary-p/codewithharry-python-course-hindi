#2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
name=input("Enter the name of the student:")
marks=int(input("Enter the marks of the student:"))
phone=int(input("Enter the phone number of the student :"))
s="The name of the student is {} and his markas {} and his phone number is {}".format(name,marks,phone)
print(s)
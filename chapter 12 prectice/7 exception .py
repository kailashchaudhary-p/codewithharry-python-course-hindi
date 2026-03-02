#the excepation  is use to handdle the error in the program and it is use to prevent the program from crashing and it is use to provide a user friendly message to the user when an error occurs
try:
    a = int(input("Enter the Number:"))
    print(a)
except Exception as e:
    print(e)#when we not add the int the program will give msg that we can not convert the string to int but when we add the int it will give us the number that we entered and it will not give us an error message and it will not crash the 
print("this is the end of the program")
#Rasing exection 
#it use to raise an exeption when we want to raise an exeption we use the raise keyword and we can raise an exeption with a message that we want to show to the user when the exeption occurs
def check_age(age):
   
    if age < 18:
        raise Exception ("you are below 18 you can not vote ")
    else:
        print("your vote is Done successfully")
age = int(input("Enter your age:"))
check_age(age)

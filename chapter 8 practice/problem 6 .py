#Write a python function which converts inches to cms.
def inches_to_cms(inches):#define function to convert inches to cms
    if inches==0:#base case 
        return 0
    else:#recursive case 
        return 2.54 + inches_to_cms(inches -1)#return conversion value
num= int(input("Enter lenth in inches:"))#take input from user
print(f"{num} converted to cms is {inches_to_cms(num)}")#print conversion value

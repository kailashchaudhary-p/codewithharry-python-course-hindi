#If languages of two friends are same; what will happen to the program in problem 6?
fan_lan={}#create empty dict
name=input("Enter your name:")
language=input("Enter your favrite language:")
fan_lan.update({name:language})#add name and language to dict
#copy the above thre lines 
name=input("Enter your name:")
language=input("Enter your favrite language:")
fan_lan.update({name:language})

name=input("Enter your name:")
language=input("Enter your favrite language:")
fan_lan.update({name:language})

name=input("Enter your name:")
language=input("Enter your favrite language:")
fan_lan.update({name:language})
print(fan_lan)#print the dict
#if the keys are diffrent the values are same it will print both values because keys are diffrent in dictionary.
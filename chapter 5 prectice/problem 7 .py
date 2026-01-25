#If the names of 2 friends are same; what will happen to the program in problem 6?
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
#in this program the two friends name is same when we write the name again the old name or languge will update not print both because keys are not samein dictionary.
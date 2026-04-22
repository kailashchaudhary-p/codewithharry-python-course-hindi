#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
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

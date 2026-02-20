#Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
class myclass():
    a = 10
    
obj = myclass()
obj.a=0
print(obj.a)#This is not class atributes
print(myclass.a)#This is a class atributes 
#the class atributes is not change because we change the value of a using object and it is not change the class atributes.


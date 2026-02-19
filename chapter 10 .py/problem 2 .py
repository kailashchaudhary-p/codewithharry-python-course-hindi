#Write a class “Calculator” capable of finding square, cube and square root of a number.

class calculator():
    a=int(input("Enter a Number:"))
    def square(self,a):
        print (a**2)
    def cube(self,a):
        print(a**3)
    def squareroot(self,a):
        print(a**0.5)
obj=calculator()
obj.square(obj.a)
obj.cube(obj.a)
obj.squareroot(obj.a)
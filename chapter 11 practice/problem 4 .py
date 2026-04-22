#Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
class cmplex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,c2):
        return cmplex(self.real+c2.real,self.imaginary+c2.imaginary)
    def __mul__(self,c2):
        return cmplex(self.real*c2.real-self.imaginary*c2.imaginary,self.real*c2.imaginary+self.imaginary*c2.real)
c1=cmplex(5,4)
c2=cmplex(3,8)
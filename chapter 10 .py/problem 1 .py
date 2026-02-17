#Create a class “Programmer” for storing information of few programmers working at Microsoft.
class programer:
    def __init__(self):
        self.name =input("Enter the nmae of programer:")
        self.age =int(input("Enter the age of programer:"))
        self.incriment=int(input("Enter the increment of programer:"))
        print(self.name,self.age,self.incriment)
        

object=programer()



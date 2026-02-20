#Create a class “Programmer” for storing information of few programmers working at Microsoft.
class programer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin
p=programer("ram",400000,144221)
print(p.name,p.salary,p.pin)



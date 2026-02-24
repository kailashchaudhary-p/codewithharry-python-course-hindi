#Create a class ‘Employee’ and add salary and increment properties to it.
#Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.
class Employee:
    def __init__(self):
        self.salary=20
        self.increment=40
    @property
    def salaryafterincrement(self):
        return self.salary + self.increment *(self.increment/100)
        @salaryafterincrement.setter
        def salaryafterincrement(self,increment):
            self.increment= self.salary * (increment/100)
e=Employee()
e.salaryafterincrement=30
print(e.increment)
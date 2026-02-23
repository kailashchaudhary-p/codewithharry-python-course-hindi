#Create a class ‘Employee’ and add salary and increment properties to it.
class Employee:
    def __init__(self,name,salary,increment):
        self.name=name
        self.salary=salary
        self.increment=increment
    def show(self):
        print(f"name of employee is {self.name} and salary is {self.salary} and increment is {self.increment}")
E=Employee("Abhinav chaudhary",50000,5000)
E.show()
#Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class animal:
    def __init__(self,name):
        self.name=name
        def show(self):
            print(f"name of animal is {self.name}")
            class pets(animal):
                def __init__(sewlf,name,owner):
                    super().__init__(name)
                    self.owner=owner
                    def show(self):
                        print(f"name of pet is {self.name} and owner is {self.owner}")
                        class dog(pets):
                            def __init__(self,name,owner,power):
                                super().__init__(name,owner)
                                self.power=power
                                def bark(self):
                                    print(f"{self.name} is barking with power {self.power}")
                                    a=animal("lion")
                                    p=pets("cat","wolf")
                                    d=dog("dog","owner",100)
                                    d.bark()
                                    
                                    


#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
import random
class train:
    def __init__(self,A,fro,to):
        self.A=A
        self.fro=fro
        self.to=to
    def bookticketr(self):
        print(f"Your Tiket is Booked The Train No. is{self.A} from {self.fro} to {self.to}")
        def getstatus(self):
            print(f"The Train No. is {self.A} from {self.fro} to {self.to} has 80 seats available")
            def getfare(self):
                print(f"The Train No. is {self.A} from {self.fro} to {self.to} {random.randint(500,2000)} is the fare for this train")
t=train(1258,"dehli","Punjab")
t.bookticketr()
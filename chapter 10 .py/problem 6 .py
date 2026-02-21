#Can you change the self-parameter inside a class to something else (say “harry”). Try changing slf to “self” or “harry” and see the effects
import random
class train:
    def __init__(slf,A,fro,to):#the use of self is not mandatory but it is a conversion to use self as the first parameter of the mathod of a class 
        slf.A=A
        slf.fro=fro
        slf.to=to
    def bookticketr(slf):
        print(f"Your Tiket is Booked The Train No. is{slf.A} from {slf.fro} to {slf.to}")
        def getstatus(slf):
            print(f"The Train No. is {slf.A} from {slf.fro} to {slf.to} has 80 seats available")
            def getfare(slf):
                print(f"The Train No. is {slf.A} from {slf.fro} to {slf.to} {random.randint(500,2000)} is the fare for this train")
t=train(1258,"dehli","Punjab")
t.bookticketr()#you can see the program is running 
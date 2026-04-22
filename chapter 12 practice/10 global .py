#Global variable 
a =411#this is the global variable
def fun():
    global a
    a=8#thi is the local variable
    print(a)
fun()
print(a)
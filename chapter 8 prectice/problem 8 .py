#Write a python function to print multiplication table of a given number.
def multiplication_table(n, i=1):#define function to print multiplication taable
    if i > 10:#base case
        return
    else:#recursive case
        print(f"{n} x {i} = {n * i}")#print multiplication value
        multiplication_table(n, i + 1)#recursive call
        sum= int(input("Enter a number to print its multiplication table:"))#take input from user
multiplication_table(sum)#call the function to print multiplication table
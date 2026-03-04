#Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
try:
    a = int(input('Enter a number a:'))
    b = int(input('Enter a number b:'))
    r=a/b
    print(r)
except ZeroDivisionError as e:
        print("error")
#The finally block is use to execute the code that we want to execute regardless of whether an exeption occurs or not it is use to clean up the resources that we have used in the program and it is use to close the file that we have opened in the program
def main():
    try:
        a =int(input("Enter the number :"))
        print(a)
    except Exception as e:
        print(e)
    finally:
        print("this is the finally block it will execute regardless of whether an exeption occurs or not")
main()
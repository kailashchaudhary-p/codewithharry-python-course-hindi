#Write a program to mine a log file and find out whether it contains ‘python’.
with open ("chapter 10 prectice/log.txt")as f:
    content=f.read()

    if("python" in content):
        print("yes python is present")
    else:
        print("python is not present")
   




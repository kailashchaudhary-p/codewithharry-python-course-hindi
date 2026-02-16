#Write a program to find out the line number where python is present from ques 6.
with open("chapter 10 prectice/log.txt")as f:
    content=f.readlines()

    for index,line in enumerate(content):
        if("python" in line):
            print(f"python is present at line number {index+1}")
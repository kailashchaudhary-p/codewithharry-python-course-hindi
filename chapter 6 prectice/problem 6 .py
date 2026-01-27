# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
marks=int(input("Enter your marks:"))#input function to enter the marks
if marks<100 and marks>=90:#Use the if statement to check the marks
    print("your grade isEx")
elif marks<90 and marks>=80:#use elif statement to check the marks
    print("your grade is A")
elif marks<80 and marks>=70:#use elif statement to check the marks
    print("your grade is B")
elif marks<70 and marks>=60:#use elif statement to check the marks
    print("your grade is C")
elif marks<60 and marks>=50:#use elif statement to check the marks
    print("your grade is d")
elif marks<50 and marks>=0:#use elif statement to check the marks
    print("your grade is f")
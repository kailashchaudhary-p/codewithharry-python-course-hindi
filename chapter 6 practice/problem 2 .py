#Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
sub1= int(input("Enter the marks of English="))#use input function
sub2= int(input("Enter the marks of Hindi="))#use input function
sub3= int(input("Enter the marks of Maths="))#use input function
total= sub1+sub2+sub3#calculate total marks
persentage=(total/300)*100#clculate the persanmtge
if sub1<33 or sub2<33 or sub3<33:
      print("YOu are fail .Try again")
elif persentage<40:
      print("you are fail.your persentage is less than 40%")
else:
    print("you are pass.lets celebrate" )
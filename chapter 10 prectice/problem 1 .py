# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’B
#read the file 
f = open('chapter 10 prectice/poem.txt')#create a file object to open the file in read mode
content=f.read()#read the content of the file
if 'twinkle' in content:#use if else statement
    print('twinkle is present in the file')
else:
    print('twinkle is not present in the file')
f.close()#close the file object
#now write in the txt file 
s = "hello kaise ho mera nam kailash hai m btech student hu or m sardar beant singh state university gurdaspur m padta hu "
f = open("chapter 10 prectice/hello.txt","w")
f.write(s)
f.close()
#add second line in this file 
f = open("chapter 10 prectice/hello.txt","a")
f.write("\nthis is the seccond line ")
f.close()
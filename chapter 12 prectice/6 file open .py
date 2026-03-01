#we use with statement to open a file and it automatically closes the file after the block of code is executed
with open("chapter 12 prectice/kailash.txt","r") as f:
    con=f.read()
    print(con)

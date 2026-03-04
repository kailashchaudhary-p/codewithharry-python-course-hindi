#Store the multiplication tables generated in problem 3 in a file named Tables.txt.
num= int(input("Enter a number:"))
tabel = [num*i for i in range(1,11)]
print(tabel)
with open ("chapter 12 prectice 1/tabel.txt","a") as f:
    f.write(str(tabel)+"\n")
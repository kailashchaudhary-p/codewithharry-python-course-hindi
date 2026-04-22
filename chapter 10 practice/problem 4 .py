#A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.
str='Donkey'
with open("chapter 10 prectice/d.txt",'r') as f:
    Connect=f.read()
    Connect=Connect.replace(str,'#####')
    with open ("chapter 10 prectice/d.txt",'w') as f:
        f.write(Connect)
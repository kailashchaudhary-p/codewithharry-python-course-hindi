#Repeat program 4 for a list of such words to be censored. 
list=['bad','good']
with open('chapter 10 prectice/prb5.txt','r') as f:
    content=f.read()
    for add in list:
        content=content.replace(add,'#'*len(list))
        with open('chapter 10 prectice/prb5.txt','w') as f:
            f.write(content)

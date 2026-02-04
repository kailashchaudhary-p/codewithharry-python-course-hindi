#Write a python function to remove a given word from a list ad strip it at the same time.
def rem(l,word):
    for i in l:
        l .remove(word)
    return l
l = ['apple','hello','happy']
print(rem(l,'happy'))
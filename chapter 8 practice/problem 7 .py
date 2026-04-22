#Write a python function to remove a given word from a list ad strip it at the same time.
def remove_and_strip(word_list, remove_word):#define function to remove and strip words
    return [word.strip() for word in word_list if word.strip() != remove_word]#example usage
words = ["  apple  ", "banana", "  orange  ", "apple", "  grape  "]#list of words
result = remove_and_strip(words, "apple")#remove "apple" and strip spaces
print(result)#print the result
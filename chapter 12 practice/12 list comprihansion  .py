#the list comprehantion is a concise way to create a list in python it is a syntactic sugar for the for loop and it is used to create a new list from an existing list by applying a condition or an expression to each element of the existing list
l=[1,2,3,44,4,5,6,7,8,9]
# list_square=[]
# for i in l:
#     list_square.append(i*i)
# print(list_square)
#using list comprehantion
list_square=[i*i for i in l]
print(list_square)
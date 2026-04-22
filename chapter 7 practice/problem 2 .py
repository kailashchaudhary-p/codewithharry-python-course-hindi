# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l: #use for loop to iterate through each name in the list
    if name.startswith("S"): #check if the name starts with 'S'
        print("Hello " + name) #greet the person whose name starts with 'S'
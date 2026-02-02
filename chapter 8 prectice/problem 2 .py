#Write a python program using function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):#define function to convert Celsius to Fahrenheit
    return  (celsius * 9/5) + 32 #return the Fahrenheit value
f = int(input("Enter temperature in Celsius: ")) #take input from user for Celsius temperature
print(celsius_to_fahrenheit(celsius=f)) #call the function and print the Fahrenheit value
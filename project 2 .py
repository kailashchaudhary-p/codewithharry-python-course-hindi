import random

number = random.randint(1,50)

print("welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 50.")
guess = int(input("can you guess the number="))
while guess !=number:
    if guess < number:
        print("too low, try again")
        guess = int(input("can you guess the number?"))
    elif guess > number:
        print("too high, try again")
        guess = int(input("can you guess the number?"))
    else:
        print("Congratulations! You guessed the number correctly.")
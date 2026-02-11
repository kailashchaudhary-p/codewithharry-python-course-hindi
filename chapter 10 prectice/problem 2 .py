#The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random
def game():
    print("Welcome to the game it create by kailash chaudhary")
    score = random.randint(0,50)
    print(f"your score is {score}")
    return score 
game()

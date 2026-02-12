#The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random#use randome 
def game():#create the function game
    print("Welcome to the game it create by kailash chaudhary")#print the walcome msg
    with open("chapter 10 prectice/highscore.txt") as f:#open the file
        hi_score = f.read()#read the file
    if hi_score == "":
        hi_score = int(hi_score)
    else:
         hi_score = int(hi_score)

    score = random.randint(0,50)#genrate randome score between 0 to 50
    print(f"your score is {score}")#use f string to print the score
    if score > hi_score:#check if the score is greater than hi score
        print("Congratulations! You have broken the Hi-score!")#print the congratulation msg
        with open("chapter 10 prectice/highscore.txt", "w") as f:#open the file in write mode
            f.write(str(score))#write the new hi score in the file
    return score 
game()

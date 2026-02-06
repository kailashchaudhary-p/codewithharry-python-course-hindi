'''We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.'''
import random
def game(com,you):
    if com==you:
        print('Tie')
    elif(com=='s'and you=='w')or(com=='w'and you=='g')or(com=='g'and you=='s'):
        print('Computer wins')
    else:
        print('You win')
print("Welcome to Snake, Water, Gun game!")
print("Enter 's' for Snake, 'w' for Water and 'g' for Gun")
com_dec=random.choice(['s','w','g'])
you=input("your turn:").lower()
if you not in ['s', 'w', 'g']:
    print("Invalid input! Please enter 's', 'w', or 'g'")
else:
    game(com_dec, you)
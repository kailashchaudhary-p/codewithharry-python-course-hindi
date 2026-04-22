'''We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.'''
import random

print("Welcome to Snake-Water-Gun Game!")
print("Rules: Snake beats Water, Water beats Gun, Gun beats Snake. Same choice = Draw.")

# Input number of rounds
try:
    num_rounds = int(input("Enter number of rounds: "))
except ValueError:
    print("Invalid input. Defaulting to 3 rounds.")
    num_rounds = 3

options = ['s', 'w', 'g']
user_score = 0
comp_score = 0
round_num = 1

while round_num <= num_rounds:
    print(f"\nRound {round_num}:")
    print("Enter s for Snake, w for Water, g for Gun")
    
    user_choice = input("Your choice: ").lower().strip()
    
    if user_choice not in options:
        print("Invalid choice! Skipping this round.")
        round_num += 1
        continue
    
    comp_choice = random.choice(options)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")
    
    # Determine winner
    if user_choice == comp_choice:
        print("It's a draw!")
    elif (user_choice == 's' and comp_choice == 'w') or \
         (user_choice == 'w' and comp_choice == 'g') or \
         (user_choice == 'g' and comp_choice == 's'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        comp_score += 1
    
    round_num += 1

# Final result
print("\nGame Over!")
print(f"Your score: {user_score}, Computer score: {comp_score}")

if user_score > comp_score:
    print("Congratulations! You won the game!")
elif comp_score > user_score:
    print("Computer won the game. Better luck next time!")
else:
    print("Match drawn!")

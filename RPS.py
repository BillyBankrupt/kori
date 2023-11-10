import random

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, Paper or Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You won this round!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won this round!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won this round!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a draw this round!")
        draws += 1
    
    else:
        print("You lost this round!")
        computer_wins += 1

print("You won", user_wins, "times")
print("You lost", computer_wins, "times")
print("You drew", draws, "times")

if user_wins > computer_wins:
    print("Congratulations! You win RPS!")
elif user_wins < computer_wins:
    print("Sorry, the computer won this time!")
else:
    print("It was a draw this time!")
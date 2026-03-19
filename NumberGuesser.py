import random

# Outer loop — controls replay
while True:
    secret = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20...")

    # Inner loop — controls guessing
    while True:
        guess = int(input("Your guess: "))
        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print("You got it! 🎉")
            break

    # Play again?
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        print("Let's go again!")
    else:
        print("Goodbye 👋")
        break

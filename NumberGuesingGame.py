import random

# Play rounds until the player says no
while True:
    # Pick a secret number
    secret = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20...")
    print(secret) # CHEAT LINE: delete this in Stage 4

    # Keep asking until they get it right
    while True:
        guess = int(input("Your guess: "))

        # Check the guess
        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print("You got it! 🎉")
            break  # leave the guessing loop

    # Play again?
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        print("Let's go again!")
    else:
        print("Goodbye 👋")
        break  # leave the game loop

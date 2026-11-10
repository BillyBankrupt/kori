import random

# Play rounds until the player says no
while True:
    # Difficulty options
    print("Choose a difficulty:")
    print("1 - Easy   (1 to 20)")
    print("2 - Medium (1 to 50)")
    print("3 - Hard   (1 to 100)")

    # User chooses difficulty level
    difficulty = input("Enter 1, 2 or 3: ")

    if difficulty == "1":
        top = 20
        limit = 5  # maximum number of guesses allowed
    elif difficulty == "2":
        top = 50
        limit = 6
    else:
        top = 100
        limit = 7

    # Pick a secret number
    secret = random.randint(1, top)
    print(f"I'm thinking of a number between 1 and {top}...")
    count = 0  # new variable to track guesses

    # Keep asking until they get it right
    while True:
        guess = int(input(f"Your guess ({count}/{limit}): "))
        count = count + 1  # add 1 every time they guess

        # Check the guess
        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print(f"You got it in {count} guesses! 🎉")
            break  # leave the guessing loop

        if count == limit:  # check if they've used all their guesses
            print(f"Out of guesses! The number was {secret}")
            break  # leave the guessing loop

    # Play again?
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        print("Let's go again!")
    else:
        print("Goodbye 👋")
        break  # leave the game loop

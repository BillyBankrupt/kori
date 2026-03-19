import random

# Stage 1
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
    elif difficulty == "2":
        top = 50
    else:
        top = 100
    # Stage 2 - Getting input
    secret = random.randint(1, top)
    print(f"I'm thinking of a number between 1 and {top}...")
    count = 0  # new variable to track guesses
    limit = 5  # maximum number of guesses allowed

    # Stage 3 — Conditionals (if/elif/else)
    while True:
        guess = int(input(f"Your guess ({count}/{limit}): "))
        count = count + 1  # add 1 every time they guess

        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print(f"You got it in {count} guesses! 🎉")
            break

        if count == limit:  # check if they've used all their guesses
                print(f"Out of guesses! The number was {secret}")
                break

    # Stage 4 - Play again?
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        print("Let's go again!")
    else:
        print("Goodbye 👋")
        break

import random
 
# Stage 1 — Variables & random
while True:
    secret = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20...")
 
    # Stage 2 – Getting Input — controls guessing
    while True:
        guess = int(input("Your guess: "))
        
        # Stage 3 — Conditionals (if/elif/else)
        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print("You got it! 🎉")
            break  # exits the inner loop
 
    # Stage 4 - Play again?
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() == "yes":
        print("Let's go again!")
    else:
        print("Goodbye 👋")
        break  # exits the outer loop

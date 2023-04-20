import random

num_rounds = 3
max_guesses = 6
score = 0

print("Welcome to the Number Guessing Game!")
print("You will play", num_rounds, "rounds. Each round, you have to guess a number between 1 and 100.")
print("You will score points based on the number of attempts taken to guess the number.")
print("Let's get started!\n")

for i in range(num_rounds):
    secret_number = random.randint(1, 100)
    num_guesses = 0
    print("Round", i+1, "starts now!")
    while num_guesses < max_guesses:
        guess = int(input("Guess a number between 1 and 100: "))
        num_guesses += 1
        if guess == secret_number:
            print("Congratulations! You guessed the secret number in", num_guesses, "guesses!")
            round_score = max_guesses - num_guesses + 1
            score += round_score
            print("You scored", round_score, "points in this round.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print("Sorry, you've reached the maximum number of guesses. The secret number was", secret_number)

print("\nAll rounds are finished!")
print("Your total score is", score)

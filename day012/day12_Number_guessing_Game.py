import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

number = random.randint(1, 99)

if difficulty == "hard":
    attempts_left = 5
elif difficulty == "easy":
    attempts_left = 10



player_guess = 0

def guess_info_printer(guess):
    if guess > number:
        print("Too high.")
        print("Guess again")
    elif guess < number:
        print("Too low.")
        print("Guess again")
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        return

def guess_function():
    print(f"You have {attempts_left} attempts remaining to guess the number.")
    return int(input("Make a guess: "))
    

while attempts_left != 0:
    player_guess = guess_function()
    attempts_left -= 1
    guess_info_printer(player_guess)

print("You've run out of guesses, you lose.")
    

import art
from random import randint

# Set global constant
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

# Prep 1: Function to check user guess compared to the actual answer.
def check_answer(user_guess, actual_answer, turns):
    """Compares user guess with the actual answer. Returns the remaining number of attempts."""
    if user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    elif user_guess > actual_answer:
        print("Too high!")
        return turns - 1
    else:
        print(f"You got it right!The correct answer was {actual_answer}")


# Prep 2: Function for setting difficulty level
def set_difficulty():
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard' \n").lower()
    if difficulty == 'easy':
        return EASY_ATTEMPTS
    elif difficulty == 'hard':
        return HARD_ATTEMPTS

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game! \n "
          "I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)  

    life = set_difficulty() 

    # Repeat the guessing functionality if they guess wrong
    guess = 0
    while guess != answer:
        print(f"You have {life} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        life = check_answer(guess, answer, life) # new value returned from function, then assigned back here.
        if life == 0:
            print("You lose. You have no more guesses left :( ")
            return
        elif guess != answer:
            print("Guess again!")

play_game()

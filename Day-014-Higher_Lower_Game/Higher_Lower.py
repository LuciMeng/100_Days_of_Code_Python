# import data from game data, logo from art
from game_data import data
from art import logo, vs #comma - and
import random

# Accumulate score while the user is right.
score = 0

def format_data(account):
    """Takes the account data and returns the printable format"""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

# generate A: Compare A: name, description, from country.
A = random.choice(data)
# against B: Compare B: name, description, from country.
B = random.choice(data)
while A == B:
    B = random.choice(data)

# Game part
while True:
    print(logo)
    print(f"Compare A: {format_data(A)}")
    print(vs)
    print(f"Against B: {format_data(B)}")

# Self Check
#     print(f"Follower of A: {A['follower_count']}")
#     print(f"Follower of B: {B['follower_count']}")

# Ask for input: Who has more followers? Type A or B:
    guess = input("Who has more followers? Type 'A' or 'B':").upper()

    print("\n"* 20)
# Figure out the correct answer:
    if A['follower_count'] > B['follower_count']:
        correct_answer = 'A'
    else:
        correct_answer = 'B'

# Compare guess with correct answer:
    if guess == correct_answer:
        score += 1
        print(f"You are right! Current score: {score}.")

# Carry B forward to A
        if correct_answer == 'B':
            A = B # B becomes A
        B = random.choice(data)
        while A == B:
            B = random.choice(data)
    else:
        print(f"Sorry, that's not right. Final score: {score}.")
        break


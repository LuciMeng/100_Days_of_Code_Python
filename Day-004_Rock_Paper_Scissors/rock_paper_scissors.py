import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
player_choice= int(input("What do you want to choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
if 0 <= player_choice <= 2:
    player = game[player_choice]
    print(player)

computer_choice = random.randint(0,2)
computer = game[computer_choice]
print(f"Computer chose{computer}")

if player_choice >= 3 or player_choice <0:
    print("You've typed an invalid number. You lose.")
elif player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > player_choice:
    print("You lose!")
elif player_choice == 2 and computer_choice == 0:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")

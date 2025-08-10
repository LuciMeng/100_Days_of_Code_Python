import random
import art

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def has_blackjack(hand):
    """Check if either player has Blackjack"""
    return len(hand) == 2 and 11 in hand and 10 in hand

def adjust_for_ace(hand):
    """Adjust Ace from 11 to 1"""
    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

def check_user_bust(hand):
    """Check if user is busted"""
    adjust_for_ace(hand)
    if sum(hand) > 21:
        print("You scored more than 21. Computer wins!")
        return True
    return False

def check_win(u_score, c_score):
    """Check for win"""
    print(f"Final computer score: {c_score}, "
          f"Final user score: {u_score}")
    if u_score > 21:
        print("You went over 21. Computer wins :(")
    elif c_score > 21:
        print("Opponent went over. You win!")
    elif u_score > c_score:
        print("You win!")
    elif c_score > u_score:
        print("You lose :(")
    else:
        print("It's a tie!")

def play_game():
    print(art.logo)
    computer_hand = []
    user_hand = []

    for _ in range(2):
        computer_hand.append(deal_card())
        user_hand.append(deal_card())

    user_score = sum(user_hand)
    computer_score = sum(computer_hand)
    print(f"Your cards: {user_hand}, your score: {user_score} \n"
          f"Computer first card: {computer_hand[0]}")

    if has_blackjack(computer_hand):
            print("Computer has a blackjack! Computer wins.")
    elif has_blackjack(user_hand) and not has_blackjack(computer_hand):
            print("User has a blackjack! User wins.")
    else: # If neither has blackjack, the code in the else: runs: user can draw, then computer draws, then final comparison.
        #User Turn to draw more cards
        while True:
            choice = input("Would you like to get another card? Y/N").lower()
            if choice == "y":
                user_hand.append(deal_card())
                print(f"Your hand: {user_hand}\n")
                if check_user_bust(user_hand):
                    exit()
            else:
                break

        while sum(computer_hand) < 17:
            computer_hand.append(deal_card())
            adjust_for_ace(computer_hand)
            computer_score = sum(computer_hand)

        # Final result
        print(f"Your final hand: {user_hand}, final score: {user_score} \n"
              f"Computer final hand: {computer_hand}, final score: {computer_score}")
        check_win(user_score, computer_score)


while input("Do you wnat to play a game of Blackjack?: 'y' or 'n'?").lower() == 'y':
    print("\n" * 20)
    play_game()





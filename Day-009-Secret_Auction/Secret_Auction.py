import art
print(art.logo)

def finding_winner(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} with a bid of ${highest_bid}.")

bids = {}
bidding_open = True
while bidding_open:
    name = input("What is your name?\n")
    bid = int(input("What is your bid? \n $"))
    bids[name] = bid 
    print(bids)

    more_bidders = input("Are there other bidders? Type 'yes' or 'no' \n").lower()
    if more_bidders == "yes":
        bidding_open = False
        finding_winner(bids)
    elif more_bidders == "no":
        print("\n" * 20) 

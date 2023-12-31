from art import logo
import os
clear = lambda: os.system('clear')

print(logo)
bids = {}

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")



bidding_finished = False

while bidding_finished == False:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        clear()

### secret auction
import os
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("Welcome to the secret auction program.")

bidder_dictionary = {}

def auction_program(participant_name, participant_bid):
    bidder_dictionary[participant_name] = participant_bid
    
    
new_bidder = "yes"
while new_bidder != "no":
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    auction_program(name, bid)
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
    os.system('cls')
high_bid = 0
for key in bidder_dictionary:
    if bidder_dictionary[key] > high_bid:
        high_bid = bidder_dictionary[key]
        winner = key
    
print(f"{winner} is the winner with a bid of {high_bid}$! ")

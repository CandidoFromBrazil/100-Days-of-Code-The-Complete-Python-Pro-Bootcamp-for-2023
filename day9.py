#link to game in replit: https://replit.com/@MatheusWillians/Blind-Auction?v=1, you can always fork it
#All the project and the inherent libraries are in the additional folder to be downloaded by you, is a folde named: day9.py.zip, enjoy it

#Blind Auction

from replit import clear
from art import logo

print(logo)
#creating the dictionary and a bool control variable
bids = {}
bidding_finished = False


#wsecond function created on line, used inside the first down below
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #for through the bid that will be given when function called
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        #addicting the value to a valuable, then checking if that value is higher than the prvious one, so as to convey a winner at the end
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


#while bidding_finished not False, the promp will keep asking whether or not the user wishes to continue the program
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    #real important line down here, it do say to our code that, our bids[key] = value, are equal to ou varuables: bids{name : price}
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes or 'no'.\n")
    #if to decide to continue or nor the while loop
    if should_continue == "no":
        bidding_finished = True
        #calling the find_highest_bidder() function once all participants are done with they bidding
        find_highest_bidder(bids)
    elif should_continue == "yes":
        #clear function from replit library
        clear()
"""
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 
"""

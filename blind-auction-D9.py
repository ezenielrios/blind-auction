from replit import clear
from art import logo #show logo from art.py file
print(logo)

bids = {} #starting empty dictionary
bidding_finished = False

#determing winner
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record: 
    bid_amount = bidding_record[bidder] #use key to get the value
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ") #Ask for name input
  price = int(input("What is your bid?: $")) #ask for bid price input
  bids[name] = price #in order to add to dictionary specify key[name] and value =price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n") 
  if should_continue == "no": #stops loop
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear() #clear output for fresh entries
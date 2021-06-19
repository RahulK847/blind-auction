from replit import clear
from art import logo
print(logo)
anyone_left=True
bid_info={}
while anyone_left:
  name = input("What's your Name: ")
  bid_amount = int(input("Your bid: $"))
  bid_info[name] = bid_amount
  other=input("Are their any other Bidders? Type 'yes' or 'no': ")
  if other=="no":
    anyone_left=False
  clear()
  higher_bid=0
  his_name = ""
for name in bid_info:
  if bid_info[name]>higher_bid:
    his_name = name
    higher_bid = bid_info[name]
print(f"The winner is {his_name} wtih the bid a of ${higher_bid}")

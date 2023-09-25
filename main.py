# vars we'll need
import random

war_cards = []
nums = [value for value in range(2, 11)] + ['J', 'Q', 'K', 'A']
suites = ['♠', '♣', '♢', '♡']
user_cards = []
comp_cards = []
user_cards_used = []
comp_cards_used = []
user_wins = 0
comp_wins = 0
message = ("Welcome to the card game of war. There will be two rounds. The player with the most wins wins. If there "
           "is a tie between rounds a third round will begin")

# creating the deck
for suit in suites:
    for num in nums:
        card = f"{num}{suit}"
        war_cards.append(card)

# ____________+
# |{num}      |
# |    {suit} |
# |       {num}|
# +__________+

# Shuffle the cards up randomly
random.shuffle(war_cards)

# test
print(war_cards)

# giving the user half the deck
user_cards = war_cards[:26]

print(user_cards)
# giving the comp half the deck
comp_cards = war_cards[26:]

# test
print(comp_cards)
print(len(user_cards))
print(len(comp_cards))
input("type flip or press enter to flip your card")
print(f"{comp_cards[0][0]} {user_cards[0][0]}")

# FIGURE OUT J, Q, K, A
# NOT WORKING 100%
if int(comp_cards[0][0]) > int(user_cards[0][0]):
    print(comp_wins)
else:
    print("pop")

# vars we'll need
import random

war_cards = []
nums = [value for value in range(2, 11)] + ['J', 'Q', 'K', 'A']
suites = ['♠', '♣', '♢', '♡']
user_cards = []
comp_cards = []
user_cards_used = []
comp_cards_used = []
comp_current_card = 0
user_current_card = 0
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
# print(war_cards)

# giving the user half the deck
user_cards = war_cards[:26]

# print(user_cards)
# giving the comp half the deck
comp_cards = war_cards[26:]

# test
# print(comp_cards)
# print(len(user_cards))
# print(len(comp_cards))
for i in range(1000):
    input("type flip or press enter to flip your card")
    print(f"computer cards:{comp_cards[0]} user cards:{user_cards[0]}")

    # FIGURE OUT J, Q, K, A
    # NOT WORKING 100%

    letter_cards = {
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    comp_current_card = comp_cards[0][0]
    user_current_card = user_cards[0][0]
    # Checking to see if it's not an integer by using letter_cards
    if comp_cards[0][0] in letter_cards.keys():

        comp_current_card = letter_cards[comp_cards[0][0]]
    # Checking to see if it's not an integer by using letter_cards
    if user_cards[0][0] in letter_cards.keys():
        # Defining comp_current_card to an integer equivalent of the character
        user_current_card = letter_cards[user_cards[0][0]]

    if int(comp_current_card) > int(user_current_card):
        comp_wins += 1
        print(f'Computer wins : {comp_wins}')
        comp_cards_used.append(user_cards.pop(0))
        comp_cards_used.append(comp_cards.pop(0))
    elif int(user_current_card) > int(comp_current_card):
        user_wins += 1
        print(f'User wins : {user_wins}')
        user_cards_used.append(comp_cards.pop(0))
        user_cards_used.append(user_cards.pop(0))
    else:
        print("I delcare WAR!!!!")

        comp_current_card = comp_cards[4][0]
        user_current_card = user_cards[4][0]
        # Checking to see if it's not an integer by using letter_cards
        if comp_cards[4][0] in letter_cards.keys():
            comp_current_card = letter_cards[comp_cards[4][0]]
        # Checking to see if it's not an integer by using letter_cards
        if user_cards[4][0] in letter_cards.keys():
            # Defining comp_current_card to an integer equivalent of the character
            user_current_card = letter_cards[user_cards[4][0]]

        if int(comp_current_card) > int(user_current_card):
            comp_wins += 1
            print(f"Computer wins : {comp_wins}")
            comp_cards_used.append(user_cards.pop(0))
            comp_cards_used.append(user_cards.pop(1))
            comp_cards_used.append(user_cards.pop(2))
            comp_cards_used.append(user_cards.pop(3))
            comp_cards_used.append(user_cards.pop(4))
            comp_cards_used.append(comp_cards.pop(0))
            comp_cards_used.append(comp_cards.pop(1))
            comp_cards_used.append(comp_cards.pop(2))
            comp_cards_used.append(comp_cards.pop(3))
            comp_cards_used.append(comp_cards.pop(4))
        elif int(user_current_card) > int(comp_current_card):
            user_wins += 1
            print(f'User wins : {user_wins}')
            user_cards_used.append(user_cards.pop(0))
            user_cards_used.append(user_cards.pop(1))
            user_cards_used.append(user_cards.pop(2))
            user_cards_used.append(user_cards.pop(3))
            user_cards_used.append(user_cards.pop(4))
            user_cards_used.append(comp_cards.pop(0))
            user_cards_used.append(comp_cards.pop(1))
            user_cards_used.append(comp_cards.pop(2))
            user_cards_used.append(comp_cards.pop(3))
            user_cards_used.append(comp_cards.pop(4))
        if comp_wins > 13:
            print("computer wins round")
        else:
            print("User wins round")
    # print(user_cards_used)
    # print(comp_cards_used)
    # print(user_cards)
    # print(comp_cards)
    #
    # for card in user_cards_used:
    #     if card in user_cards:
    #         print("bruh")
    # for card in comp_cards_used:
    #     if card in comp_cards:
    #         print("Bruh")


import random
point_player = 0
point_computer = 0
i = 1
# choose 10 random cards
while True:
    if point_player == 10 or point_computer == 10:
        break
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])

    #choosing one for computer and player randomly:
    card_1 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10,'J', 'Q', 'K', 'A'])
    Computer_card = card_1

    if card_1 == "J":
        card_1 = 11
    elif card_1 == "Q":
        card_1 = 12
    elif card_1 == "K":
        card_1 = 13
    elif card_1 == "A":
        card_1 = 14

    #choosing one for computer and player randomly:
    card_2 = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    Player_card = card_2
    if card_2 == "J":
        card_2 = 11
    elif card_2 == "Q":
        card_2 = 12
    elif card_2 == "K":
        card_2 = 13
    elif card_2 == "A":
        card_2 = 14

    #showing the cards:
    print ("Round",i,".Fight!"'\n')
    i += 1
    print("computer has:", Computer_card, suit, "Player has: ", Player_card, suit)

    if Computer_card == Player_card:
        print ("draw")
        continue

        #checking who got the bigger number
    elif card_2 > card_1:
        print ("point to player",'\n')
        point_player += 1
        continue
    elif card_1 > card_2:
        print ("point to computer"'\n')
        point_computer += 1
        continue

#printing outcome
if point_player == 10:
    print ("player wins the game")
    print("computer won: ", point_computer)
else:
    print ("computer wins the game")
    print("player won: ", point_player)
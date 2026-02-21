import random

#setting player in for (both players)
for i in range(1,3):
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card_1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    player_1 = card_1
    if card_1 == "J" or card_1 == "Q" or card_1 == "K":
        card_1 = 10
    elif card_1 == "A":
        card_1 = 1

    card_2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,'J', 'Q', 'K', 'A'])
    player = card_2
    if card_2 == "J" or card_2 == "Q" or card_2 == "K":
        card_2 = 10
    elif card_2 == "A":
        card_2 = 1

    print ("player 1 have: ", player_1, suit ,player, suit)
    total_1: int = card_1 + card_2
    player_1_final = total_1
    print ("your total is: ", total_1,'\n')
    choose = int(input("press 0 to stop"'\n' "press 1 to continue"'\n'))

    #getting another card
    if choose == 0:
        print ("you choose to stop🛑 your total is: ", total_1, '\n')

    if choose == 1:
            add_on = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
            player = add_on
            if add_on == "J" or add_on == "Q" or add_on == "K":
                add_on = 10
            elif add_on == "A":
                add_on = 1

            print ('\n'"you choose to continue, that is your add on card: ",add_on, suit)
            total_player_1 = total_1 + add_on
            player_1_final = total_player_1
            print ("your new total is: "'\n', total_player_1)

            #one last chance to win
            while total_player_1 < 21:
                Hit = int(input("would you like to Hit one last time?🎰" '\n' "if so, press 1, if not, press 0: "'\n'))
                if Hit == 1:
                    last = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
                    if last == "J" or last == "Q" or last == "K":
                        last = 10
                    elif last == "A":
                        last = 1
                    print("you choose to continue"'\n'"that is your last card: ", last, suit)
                    last_ = last + total_player_1
                    player_1_final = last_
                    print("your new total is: "'\n', last_)
                    break
                if Hit == 0:
                    print ("you choose to stop" , '\n')
                    break
    if i == 1:
        final_1 = player_1_final
        print("player 1️⃣ have: ",final_1, '\n')
        i += 1
    else:
        final_2 = player_1_final
        print("player 2️⃣ have: ",final_2, '\n')

#checking if it is a winner or a losser
if (final_2 > 21 and final_1 <= 21) or (final_1 <= 21 and final_1 > final_2):
    print ("player 1 wins!🤩")
elif (final_1 > 21 and final_2 <= 21) or (final_2 <= 21 and final_2 > final_1):
    print ("player 2 wins!🤩")
elif final_1 == final_2 and final_1 <= 21 and final_2 <= 21:
    print ("draw!😮")
elif final_1 > 21 and final_2 > 21:
    print ("Both lost!💀")
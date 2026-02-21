#1 ✊
#2 ✋
#3 ✌️

#player = input choice = 1-3
#print icon
#computer = random 1...3
#if player == computer
# elif player == 1 and computer == 2 --> computer win
# elif player == 1 and computer == 3 --> player win
# elif player == 2 and computer == 1 --> player win
# elif player == 2 and computer == 3 --> computer win
# elif player == 3 and computer == 2 --> player win
# elif player == 3 and computer == 1 --> computer win
import random
print ("1 is: ✊")
print ("2 is: ✋")
print ("3 is: ️✌️")
W = 0
L = 0
while True:
    player: int = int(input("enter 1 or 2 or 3: "))
    computer: int = random.randint(1,3)
    if player == computer:
        print ("draw")
        continue
    elif player == 1 and computer == 2:
        print ("you lost ❌", "computer choose: ✋ you choose: ✊")
        L = L + 1
    elif player == 1 and computer == 3:
        print ("yoy win 🥳", "computer choose: ✊ you choose: ✌️")
        W = W + 1
    elif player == 2 and computer == 1:
        print ("yoy win 🥳", "computer choose: ✊ you choose: ✋")
        W = W + 1
    elif player == 2 and computer == 3:
        print ("you lost ❌", "computer choose: ✌️ you choose: ✋")
        L = L + 1
    elif player == 3 and computer == 1:
        print ("you lost ❌", "computer choose: ✌️ you choose: ✊")
        L = L + 1
    elif player == 3 and computer == 2:
        print ("yoy win 🥳", "computer choose: ✋ you choose: ✌️")
        W = W + 1

    if L == 3:
        print ("i'm sorry, you lost")
        break
    if W ==3:
        print ("you crashed it!")
        break
    #elif player == 1 and computer == 2 or player == 2 and computer == 3 or player == 3 and computer == 1:
        #print ("you lost ❌")
    #elif player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        #print ("yoy win 🥳")


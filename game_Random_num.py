#random a number between 1-100 == lucky
#input number
#while user did not guess the number (must be between 1-100)
#if the user guessed lower than lucky, print "guess higher"
#if the user guessed higher than lucky, print "guess lower"
#if the user guessed the number - print "bingo"
#if the user guessed more than 7 times, exit and print "you lost!"

import random
print ("you have 7 tries!")
i = 0
lucky = random.randint (1,100)
while True:
    if i == 7:
        print ("You lost! 🥺")
        break
    else:
        guess = int(input("Enter a number between 1 and 100: "))
        if guess > 100 or guess < 1:
            print("Not a valid number")
            continue
        if guess > lucky:
            print ("guess lower ⬇️")
            i += 1
        elif guess < lucky:
            print ("guess higher ⬆️")
            i += 1
        if guess == lucky:
            print ("Bingo 🥳", "the number of the computer choose: ", lucky)
            break


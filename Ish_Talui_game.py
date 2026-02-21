import random

CAPITAL_CITIES = [
    "TOKYO", "PARIS", "LONDON", "BERLIN", "MADRID",
    "ROME", "VIENNA", "PRAGUE", "WARSAW", "ATHENS",
    "CAIRO", "ANKARA", "BEIJING", "SEOUL", "HANOI",
    "BANGKOK", "CANBERRA", "OTTAWA", "BRASILIA", "BUENOS AIRES"]

FOOD = ['PIZZA','HAMBURGER','MASHED POTATO','SALMON','STEAK','CHIPS','MEAT BALLS','PASTA','TIRAMISU','KETCHUP','TOAST','EGGS BENEDICT',
        'APPLE','WATERMELON','ONION RINGS','MUSHROOMS','ICE CREAM','BANANA','PANCAKE']

NAME = ['LIRAN','DANA','LIYA','JULY','GAL','AVI','RINAT','DAN','AMIT','ATI','CHRIS','EVIATAR','ANNA','LIOR']

GAME = ['CATCH','FOOTBALL','BASKETBALL','POKER','BLACKJACK','BASEBALL','GOLF','PING PONG','SOCCER','BINGO','DOMINO','MONOPOLY','HIDE AND SEEK']

ALL_LISTS = CAPITAL_CITIES + FOOD + NAME
all_set = set(ALL_LISTS)

selected_item = random.choice(ALL_LISTS)
if selected_item in FOOD:
    print("YOUR CATEGORY IS FOOD")
    print ('*'* 40 )
elif selected_item in NAME:
    print("YOUR CATEGORY IS NAMES")
    print ('*'* 40 )
elif selected_item in CAPITAL_CITIES:
    print("YOUR CATEGORY IS CAPITAL CITIES")
    print ('*'* 40 )


ALL_LISTS = selected_item
mask_city = ('_ ' * len(ALL_LISTS))
guesses_set = set()
got_valid_guesses = []
tries = 8
new_city_mask = ""

# 2. Mask should be in the length of the word
while new_city_mask != ALL_LISTS and tries != 0:
    if new_city_mask == "":
        print (mask_city)
    else:
        print (new_city_mask, '\n')
        new_city_mask = ""

    guess = input("guess a letter (space count): ").upper()

# 3.2.2   valid = (isalpha == True AND len(guess) == 1 AND guess not in guesses_set)
    if guess.isalpha() and len(guess) == 1 and guess not in guesses_set:
        guesses_set.add(guess)
    elif guess == ALL_LISTS:
        break
    else:
        guesses_set.add(guess)


    if guess in ALL_LISTS:
        for letter in ALL_LISTS:
            if letter == guess or letter in guesses_set:
                new_city_mask += letter
            else:
                new_city_mask += "_ "
        print (f"you guessed right! \n you have {tries} tries left")

    else:
        for letter in ALL_LISTS:
            if letter == guess or letter in guesses_set:
                new_city_mask += letter
            else:
                new_city_mask += "_ "
        tries -= 1
        print (f"you guessed wrong :( \n you have {tries} tries left")

if tries > 0:
    print (ALL_LISTS, '\n')
    print ("YOU WON THE GAME!")

else:
    print (f"YOU LOST THE GAME! the word was {ALL_LISTS.lower()}")

import random

rollagain = "yes"

while rollagain.lower() == "yes":
    symbol = random.randint(1,4)
    number = random.randint(1,13)
    symboltxt = ""
    numbertxt = ""
    if symbol == 1:
        symboltxt = "Spades"
    elif symbol == 2:
        symboltxt = "Hearts"
    elif symbol == 3:
        symboltxt = "Clubs"
    elif symbol == 4:
        symboltxt = "Diamonds"

    if number == 1:
        numbertxt = "Ace"
    elif number == 11:
        numbertxt = "Jack"
    elif number == 12:
        numbertxt = "Queen"
    elif number == 13:
        numbertxt = "King"
    else:
        numbertxt = str(number)

    print("You got " + numbertxt + " " + symboltxt + ".")
    rollagain = input("Type 'yes' to roll again: ")



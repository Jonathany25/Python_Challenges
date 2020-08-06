from random import randrange
from math import *

replay = "yes"

while replay.lower() == "yes":
    computerChoice = 50
    value = 0
    number = randrange(1, 100)
    win = False
    attempts = 0
    gamemode = input("\nType 'guess' to guess, or 'computer' to test a computer's skills: ")
    if gamemode.lower() != "guess" and gamemode.lower() != "computer":
        while gamemode.lower() != "guess" and gamemode.lower() != "computer":
            print("\nType a valid input!")
            gamemode = input("Type 'guess' to guess, or 'computer' to test a computer's skills: ")

    else:
        pass

    if gamemode.lower() == "guess":
        while not win:
            playerInput = int(input("Guess a number between 1 - 100: "))
            attempts +=1

            if playerInput == number:
                print("You win! You took " + str(attempts) + " attempts.")
                print("The number was " + str(number) + ".")
                win = True
            elif playerInput > number:
                print("Too large!")
            elif playerInput < number:
                print("Too small!")

    elif gamemode.lower() == "computer":
        playerNum = input("Choose a number between 1-100 for the computer to guess: ")

        if 1 <= int(playerNum) <= 100:
            pass
        else:
            while int(playerNum) < 1 or int(playerNum) > 100:
                print("\nType a valid input!")
                gamemode = input("Choose a number between 1-100 for the computer to guess: ")

        value = computerChoice
        playerNum = int(playerNum)

        while not win:
            print("\nComputer chose " + str(computerChoice) + ".")
            attempts+=1
            print(value)

            if computerChoice == playerNum:
                print("You win! It took " + str(attempts) + " attempts.")
                win = True
            elif computerChoice > playerNum:
                print("Too large!")
                value = int(ceil(value / 2))
                computerChoice = computerChoice - value
            elif computerChoice < playerNum:
                print("Too small!")
                value = int(ceil(value / 2))
                computerChoice = computerChoice + value

    replay = input("Type 'yes' to do it again: g")







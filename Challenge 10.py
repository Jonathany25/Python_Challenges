from random import randint

choices = ["scissor", "paper", "stone"]
wins = 0
replay = "yes"
print("Welcome to a game of Scissor, Paper, Stone")
while replay.lower() == "yes":
    print("You have won " + str(wins) + " times.")
    print("Choose Scissor, Paper or Stone.")
    player = input("Your Choice: ")
    computer = choices[randint(0, 2)]

    if player.lower() != "scissor" and player.lower() != "paper" and player.lower() != "stone":
        print("Input something valid!")

    elif player.lower() == computer:
        print("Tie!")

    elif player.lower() == "scissor":
        if computer == "paper":
            print("You Win!")
            wins +=1
        elif computer == "stone":
            print("You Lose!")

    elif player.lower() == "paper":
        if computer == "stone":
            print("You Win!")
            wins += 1
        elif computer == "scissor":
            print("You Lose!")

    elif player.lower() == "stone":
        if computer == "scissor":
            print("You Win!")
            wins += 1
        elif computer == "paper":
            print("You Lose!")
    print("Your opponent used " + computer + ".")
    replay = input("Type 'yes' to play again: ")

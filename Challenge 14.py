from random import randint
replay = "yes"

while replay.lower() == "yes":
    wins = 0
    lives = 2
    numbers = []
    playerInput = ""
    answer = ""
    numbers.append(randint(1, 13))
    while wins < 10 and lives > 0:
        print("You have " + str(lives) + " lives and " + str(wins) + " wins.")
        print("The number is " + str(numbers[0]))
        numbers.append(randint(1, 13))
        print(numbers)
        playerInput = input("Type H or L to guess whether the next number is higher or lower respectively: ")
        while playerInput.lower() != "h" and playerInput.lower() != "l":
            print("\nType a valid input!")
            playerInput = input("Type H or L to guess whether the next number is greater or smaller: ")
        if numbers[0] > numbers[1]:
            answer = "l"
        elif numbers[0] < numbers[1]:
            answer = "h"
        elif numbers[1] == numbers[0]:
            answer = "same"

        if answer == "same":
            print("You have gained a live!")
            lives += 1
        elif answer == playerInput.lower():
            print("Correct!")
            wins += 1
        elif answer != playerInput.lower():
            print("Wrong! You a lost a life!")
            lives -= 1
        numbers.pop(0)
    print("\n")
    if wins == 10:
        print("Victory!")
    elif lives == 0:
        print("Defeat!")
    print("The last number is " + str(numbers[0]))
    replay = input("Type 'yes' to play again: ")

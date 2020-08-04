from random import randint

print("The rules of this game are simple, a number is given and 1, 2 and 3 will keep on getting subtracted")
print("until it is 0, the one who reaches 0 loses.")

replay = "yes"

while replay == "yes":
    number = randint(20, 30)
    players = ["Computer", "Player"]
    first = randint(0, 1)
    win = False
    print("Then number is " + str(number) + ".")
    while not win:

        if first == 0:
            comnum = randint(1, 3)
            print("\nComputer subtracted " + str(comnum))
            number = number - comnum
            print("The number is now " + str(number))

            if number <= 0:
                print("You win!")
                break

            planum = int(input("\nChoose a number between 1 and 3: "))
            if 1 <= planum <= 3:
                print("Player subtracted " + str(planum))
                number = number - planum
                print("The number is now " + str(number))

            if number <= 0:
                print("You lose!")
                break

        elif first == 1:
            planum = int(input("\nChoose a number between 1 and 3: "))
            if 1 <= planum <= 3:
                print("Player subtracted " + str(planum))
                number = number - planum
                print("The number is now " + str(number))

            if number <= 0:
                print("You lose!")
                break

            comnum = randint(1, 3)
            print("\nComputer subtracted " + str(comnum))
            number = number - comnum
            print("The number is now " + str(number))

            if number <= 0:
                print("You win!")
                break

    replay = input("Type 'yes' to play again: ")

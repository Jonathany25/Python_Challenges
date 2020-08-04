import datetime as dt

first = ""
last = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
again = "yes"
highscore = 0.0
while again.lower() == "yes":
    if highscore == 0:
        print("\nThere is no highscore!")
    else:
        print("\nThe highscore is " + str(highscore) + ".")
    print("Let's see how fast you can type the alphabet")
    print("Type it like this: \n" + alphabet)
    input("Press ENTER to start.")
    first = dt.datetime.now()
    answer = input("Type it here: ")
    last = dt.datetime.now()
    delta = last - first
    time = round(delta.total_seconds(),2)
    if answer.lower() == alphabet:
        print("Nicely done! You did it in " + str(time) + " seconds.")

        if time < highscore or highscore == 0:
            highscorediff = abs(highscore - time)
            highscore = time
            print("You got the new highscore. You beat it by " + str(highscorediff) + " seconds.")
        else:
            highscorediff = time - highscore
            print("You were " + str(highscorediff) + " seconds away from the highscore.")
    else:
        print("You types it wrongly. Try again next time!")

    again = input("Type 'yes' to play again: ")


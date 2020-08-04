
import datetime as dt

state = 0
first = ""
last = ""
time = 10
redo = "yes"

while redo.lower()=="yes":
    print("\nTry to guess how long " + str(time) +" seconds is!\nPress ENTER to start and stop the timer!")
    input("Press ENTER to start!")
    first = dt.datetime.now()
    input("Press ENTER to stop!")
    last = dt.datetime.now()
    delta = last - first
    time_off = abs(time - float(delta.total_seconds()))
    print("You pressed at " + str(round(delta.total_seconds(),2)) + " seconds. You were " + str(round(time_off,2)) + " seconds off.")










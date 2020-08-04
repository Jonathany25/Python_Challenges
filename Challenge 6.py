from pynput.keyboard import  Key, Listener
import datetime as dt

state = 0
first = ""
last = ""
time = 10

print("Try to guess how long " + str(time) +" seconds is!\nPress ENTER to start and stop the timer!")

def on_press(key):
    global state
    global last
    global first
    keys = key
    if keys == Key.enter:
        if state == 1:
            last = dt.datetime.now()
            delta = last - first
            time_off = abs(time - float(delta.total_seconds()))
            print("You guessed " + str(round(delta.total_seconds(),2)) + " seconds. You were " + str(round(time_off,2)) + " seconds off.")
            return False

def on_release(key):
    global state
    global last
    global first
    keys = key
    if keys == Key.enter:
        if state == 0:
            first = dt.datetime.now()
            state = 1



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

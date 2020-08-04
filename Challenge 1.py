from pynput.keyboard import  Key, Listener
from colorama import init,Fore, Back, Style
init()

print("Why does Waldo wear stripes?")

def on_press(key):
    pass

def on_release(key):
    if key == Key.enter:
        print(Fore.RED + "Because he doesn’t want to be spotted.")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




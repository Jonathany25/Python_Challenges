from math import *


def pyramid(bottomLayer):
    base = 1
    spaces = int(floor(bottomLayer / 2))
    space = " "
    asterisk = "*"
    while base <= bottomLayer:
        layerS = ""
        layerA = ""
        for i in range(0, spaces):
            layerS += space
        for i in range(0, base):
            layerA += asterisk
        print(layerS, layerA)
        spaces = spaces - 1
        base = base + 2


baseLayer = input("Input a positive odd number: ")
pyramid(int(baseLayer))

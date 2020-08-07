import random
from math import *

row, column = (10, 10)
treasureMap = []
distances = [0]
win = False


def pythagoras(a, b):
    res = int(sqrt((a - x) ** 2 + (b - y) ** 2))
    return res


for i in range(0, column):
    column = []
    for j in range(0, row):
        column.append(0)
    treasureMap.append(column)

x = random.randint(0, 9)
y = random.randint(0, 9)
print(x, y)

treasureMap[x].pop(y)
treasureMap[x].insert(y, 1)

for i in treasureMap:
    print(i)
print("Guess where the treasure is!")

while not win:
    xin = int(input("Input x-coord(1-10): ")) - 1
    yin = int(input("Input y-coord(1-10): ")) - 1
    distance = pythagoras(xin, yin)
    distances.append(distance)

    if (xin, yin) == (x, y):
        print("You Win!")
    elif distances[0] < distances[1]:
        print("Warmer!")
    elif distances[0] > distances[1]:
        print("Cooler!")
    elif distances[0] == distances[1]:
        print("Same!")


for i in treasureMap:
    print(i)

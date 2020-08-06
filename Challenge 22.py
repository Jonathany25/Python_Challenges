import random

row, column = (10, 10)
array = []

for i in range(0, column):
    column = []
    for j in range(0, row):
        num = random.randint(0, 15)
        column.append(num)
    array.append(column)

for i in array:
    print(i)

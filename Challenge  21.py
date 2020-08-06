name = ""
names = []

while name.lower() != "exit":
    name = input("Write a name: ")
    names.append(name)
names.remove('exit')

for i in names:
    count = 0
    for n in range(0, len(names)):
        if i == names[n]:
            count += 1

    names = [word for word in names if word != i]

    if count > 1:
        print("There are " + str(count) + " duplicates of " + i)


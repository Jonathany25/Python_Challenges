factor = []
redo = "yes"
while redo.lower()=="yes":
    number = int(input("Input any number to find its factors: "))
    factor.clear()
    for i in range(1, number + 1):
        if number % i == 0:
            factor.append(i)
    factor.pop(0)
    if len(factor) == 1:
        print("It is a prime number.")
    else:
        print("The factors of " + str(number) + " excluding 1 are " + str(factor))
    redo = "Type 'yes' to find the factor of another number: "
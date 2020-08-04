redo = "yes"


def AND(first, second):
    res = first & second
    return res


def OR(first, second):
    res = first | second
    return res


def XOR(first, second):
    res = first ^ second
    return res


while redo.lower() == "yes":
    print("Please enter 1 or 0.")
    in1 = int(input("First input: "))
    in2 = int(input("Second input: "))
    operator = input("Input AND, OR, XOR, NAND, NOR:\n").upper()

    if in1 != 0 and in1 != 1:
        print("Invalid Input!1")

    elif in2 != 0 and in2 != 1:
        print("Invalid Input!2")

    elif operator != "AND" and operator != "OR" and operator != "XOR" and operator != "NAND" and operator != "NOR":
        print("Invalid Input!3")

    else:
        if operator.upper() == "AND":
            answer = AND(in1, in2)

        elif operator.upper() == "OR":
            answer = OR(in1, in2)

        elif operator.upper() == "XOR":
            answer = XOR(in1, in2)

        elif operator.upper() == "NAND":
            answer = not(AND(in1, in2))

        elif operator.upper() == "NOR":
            answer = not(OR(in1, in2))
        print(str(in1) + " " + operator.upper() + " " + str(in2) + " is " + str(answer))



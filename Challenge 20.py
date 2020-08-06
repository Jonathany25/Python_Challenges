fibonacci = [0, 1]

index = int(input("Type position of Fibonacci sequence(integer): "))

count = 0

while count != (index - 1):
    number = fibonacci[count] + fibonacci[count + 1]
    fibonacci.append(number)
    count += 1

print("Fibonacci number is " + str(fibonacci[index]))
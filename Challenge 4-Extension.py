distance = input("Enter the distance(m): ")
time = input("Enter the time(s): ")
speed = str(round((float(distance) / float(time)),2))
print("You have to travel at " + speed + "m/s at " + time + "s for " + distance + "m.")
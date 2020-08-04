import datetime as dt

now = dt.datetime.now()
year = int(input("Input the year you were born(yyyy): "))
month = int(input("Input the month you were born(mm): "))
dates = int(input("Input the date you were born(dd): "))
bd = dt.datetime(year, month, dates, )
delta = now - bd
print("You have lived for " + str(delta.days) + " days and " + str(int(delta.total_seconds())) + " seconds.")
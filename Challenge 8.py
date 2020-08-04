import datetime as dt
from math import *

now = dt.datetime.now()
year = int(input("Input the year you were born(yyyy): "))
month = int(input("Input the month you were born(mm): "))
dates = int(input("Input the date you were born(dd): "))
bd = dt.datetime(year, month, dates, )
delta = now - bd
years = floor(delta.days / 365.242)
yearsdiff = 18 - years
if years < 18:
    print("You can vote in " + yearsdiff + " years.")
elif years >= 18:
    print("You are allowed to vote.")
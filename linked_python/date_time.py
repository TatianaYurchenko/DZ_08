from datetime import datetime
from datetime import date
from datetime import time

def main():
    today = date.today()
    print(today)

# поличим порядковый номер дня недели и затем вытащим из масива его название
def weekday():
    today = date.today()
    days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
    print(days[today.weekday()])

weekday()

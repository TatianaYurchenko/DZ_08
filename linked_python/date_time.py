from datetime import datetime
from datetime import date
from datetime import timedelta

def main():
    today = date.today()
    print(today)

# поличим порядковый номер дня недели и затем вытащим из масива его название
def weekday():
    today = date.today()
    days = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
    print(days[today.weekday()])

# вытащить из текущей даты только время
def today_time():
    today = datetime.now()
    t = datetime.time(datetime.now())
    print(today)
    print(t)

# работа с форматами даты
# %y/%Y - Year, %a%A - weekday, %b%B - month, %d - day of month
def formatting_time():
    today = datetime.now()
    print(today.strftime(f'the current year is: %Y'))
    print(today.strftime('%a, %d %B, %y'))
# %c - locale's date and time, %x - lacale's date, %X - locale's time
    print(today.strftime(f'locale date and time: %c'))
    print(today.strftime(f'locale date: %x'))
    print(today.strftime(f'locale time: %X'))
#  %I/%H - Hour, %M - min, %S - sec, %p - locale's AM/PM
    print(today.strftime(f"%I/%H - Hour, %M - min, %S - sec, %p - locale's AM/PM"))

def scenario_involving_dates():
# days in future and in the past
#     future
    today = datetime.now()
    print('one year from now it will be', str(today + timedelta(days=365)))
    print('one year from now it will be', str(today + timedelta(weeks=2, days=3)))
#   past
#   calculate the date 1 week ago, formatted as a string
    t = datetime.today() - timedelta(weeks=1)
    s = t.strftime('%A %B %d %Y')
    print("One week ago it was",  s)
#   How many days until April Fools' Days
    today_date = date.today()
    afd = date(today_date.year, 4, 1)
    if afd < today_date:
        print("April Fools' Day already went:", ((today_date - afd).days))
        afd = afd.replace(year=today_date.year + 1)
    time_to_afd = afd - today_date
    print("It is", time_to_afd.days," days until the next April Fools' Day!")

def working_with_calendars():
    pass


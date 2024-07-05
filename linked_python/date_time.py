from datetime import datetime
from datetime import date
from datetime import timedelta
import calendar
#  класс timedelta  для выполнения математических действий с датами
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
# Необходимо импортировать calendar
def working_with_calendars():
    c = calendar.TextCalendar(calendar.MONDAY)
    str = c.formatmonth(2024, 6, 0, 0)
    print(str)
# TODO: create an HTML formatted calendar
    hc = calendar.HTMLCalendar(calendar.MONDAY)
    str = hc.formatmonth(2024,1)
    print(str)
# TODO: loop over the days of a month
    #  (zeroes mean that the day of the week is in an overlapping month)
    for i in c.itermonthdays(2024, 8):
        print(i)
def calendar_day():
    for day in calendar.month_name:
        print(day)
def temm_meeting():
    for m in range(1, 13):
        cal = calendar.monthcalendar(2024, m)
        print(m)
        print(cal)
        weekone = cal[0]
        weektwo = cal[1]
        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]
        print(calendar.month_name[m], meetday)
        
temm_meeting()
# Accespt 2 dates and show number of days between them
import datetime
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
date1 = datetime.date(year, month, day)

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
date2 = datetime.date(year, month, day)

print(abs(date1-date2))
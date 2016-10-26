import datetime
import calendar

def day_of_the_year():
	now = datetime.datetime.now()
	calendar.prmonth(now.year, now.month)
	day_of_the_month = int(input("Enter the day of the month: "))
	return(day_of_the_month, now.month, now.year)

print(day_of_the_year())
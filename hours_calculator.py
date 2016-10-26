import datetime
import calendar

#Inputs the day of the week
def day_list():
	while True:
		day_var = input("Enter day of the week(Mon, Tue, Wed, Thu, Fri, Sat, Sun): \n")
		day_check_list = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
		day_var = day_var.lower()
		if day_var in day_check_list:
			print("Input accepted\n")
			break
		print("Input incorrect, try again.")
	return day_var

#Inputs the day of the month
def day_of_the_year():
	now = datetime.datetime.now()
	calendar.prmonth(now.year, now.month)
	day_of_the_month = int(input("Enter the day of the month: "))
	return(day_of_the_month, now.month, now.year)

#Inputs beginning of the shift
def start_hours_list():
	while True:
		start_hour_var = input("Enter your beginning hours, in this format HH:MM \n")
		start_hour_list = start_hour_var.split(":")
		for i in start_hour_list:
			j = start_hour_list.index(i)
			start_hour_list[j] = int(start_hour_list[j])
		if start_hour_list[0] >= 0 and start_hour_list[0] < 24 \
		and start_hour_list[1] < 60 and start_hour_list[1] >= 0:
			print("Input accepted\n")
			break
		print("Input incorrect, try again.")
	return((start_hour_list[0], start_hour_list[1]))

#Inputs end of shift
def finish_hours_list():
	while True:
		start_hour_var = input("Enter your finishing hours, in this format HH:MM \n")
		start_hour_list = start_hour_var.split(":")
		for i in start_hour_list:
			j = start_hour_list.index(i)
			start_hour_list[j] = int(start_hour_list[j])
		if start_hour_list[0] >= 0 and start_hour_list[0] < 24 \
		and start_hour_list[1] < 60 and start_hour_list[1] >= 0:
			print("Input accepted\n")
			break
		print("Input incorrect, try again.")
	return((start_hour_list[0], start_hour_list[1]))


#Calculates how many hours you worked and subtracts breaks
def hour_calculator(begin_hours, begin_minutes, fin_hours, fin_minutes):
	hours_total = fin_hours - begin_hours
	if hours_total <= 0:
		hours_total+=24
	minutes_total = fin_minutes - begin_minutes
	if minutes_total <= 0:
		minutes_total+=60
		hours_total-=1
	elif minutes_total > 59:
		minutes_total-=60
		hours_total+=1
	print("hours test", hours_total, minutes_total)
	total_minutes = (hours_total * 60) + minutes_total
	#calculate breaks
	if total_minutes > (12*60):
		total_minutes-=30
	elif total_minutes <= (12*60) and total_minutes > (8*60):
		total_minutes-=30
	elif total_minutes <= (8*60) and total_minutes > (6*60):
		total_minutes-=15

	paid_hours = int(total_minutes/60)
	paid_minutes = total_minutes % 60

	return((paid_hours, paid_minutes))

#Calculates how many hours you worked in a week
def week_calculator(days_hours_input):
	week_hours = []
	days_hours_list = list(days_hours_input)
	for day in days_hours_list:
		day_list = list(day)
		pay_each_day = day_list[-1]
		week_hours.append(pay_each_day)
	print("days_hours_input: ", days_hours_input)
	print(week_hours)
	print(sum(week_hours))
	hours_worked = int(sum(week_hours)/60)
	minutes_worked = sum(week_hours)%60
	print("Total amount of hours worked this week is: %d hours and %d minutes" % (hours_worked, minutes_worked))
	return(hours_worked, minutes_worked, sum(week_hours))

#Brings functions together
def week_organiser():
	day_hours_counter = []
	user_input = None
	while True:
		user_input = input("Press ENTER to input a day or type 'End' if you'd like to finish:  \n")
		if user_input.lower() == "end":
			break
		else:
			day_input = day_list()
			day_date, month_date, year_date = day_of_the_year()
			start_hours, start_minutes = start_hours_list()
			finish_hours, finish_minutes = finish_hours_list()
			print(day_input, start_hours, start_minutes, finish_hours, finish_minutes) #Delete this later
			paid_hours, paid_minutes = hour_calculator(start_hours, start_minutes, finish_hours, finish_minutes)
			paid_total = paid_hours * 60 + paid_minutes
			day_hours_counter.append((day_input, day_date, month_date, year_date, start_hours, start_minutes, finish_hours, finish_minutes, paid_hours,\
			paid_minutes, paid_total))
	hours_worked, minutes_worked, total_minutes = week_calculator(day_hours_counter)




def main():
	week_organiser()


main()
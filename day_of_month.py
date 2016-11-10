import datetime
import calendar

now = datetime.datetime.now()
cal = calendar.Calendar()
this_year = now.year
this_month = 1 #Change to now.monthdays2calendar when finished testing
month_list = cal.monthdays2calendar(now.year, this_month)

def day_list():
	day_dict = {
	"mon" : 0,
	"tue" : 1,
	"wed" : 2,
	"thu" : 3,
	"fri" : 4,
	"sat" : 5,
	"sun" : 6
	}
	while True:
		day_var = input("Enter day of the week(Mon, Tue, Wed, Thu, Fri, Sat, Sun): \n")
		day_check_list = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
		day_var = day_var.lower()
		if day_var in day_check_list:
			print("Input accepted\n")
			break
		print("Input incorrect, try again.")

	return (day_var, day_dict[day_var])

def day_of_the_year_now():

	#Finds index of this week and the day of the week
	for i in month_list:
		for j in i:
			day_of_month, day_of_week = j
			if day_of_month == now.day: 
				current_week_index = month_list.index(i)
				current_day_of_week = day_of_week
				return(current_week_index, current_day_of_week)

def day_of_the_year_working(day_tuple, some_day_input):
	current_week_index, current_day_of_week = day_tuple

	#Moves the index -1 if it's the beginning of the week
	#and handles if week index is 0
	current_day_of_week = 0 #Delete this later, testing stuff
	if current_day_of_week == 0:
		work_week_index = current_week_index - 1
		if work_week_index < 0:
			last_month = cal.monthdays2calendar(now.year, this_month-1) #This is the problem with the wrong week when testing january input
			last_week_last_month = last_month[-1]
	else:
		work_week_index = current_week_index

	work_week_list = month_list[work_week_index]
	#Find a better way to do this loop
	for day in work_week_list:
		day_of_month, day_of_week = day
		if day_of_week == some_day_input:
			day_date = day_of_month
			month_date = this_month
			if day_date == 0:
				last_month = cal.monthdays2calendar(now.year, this_month-1)
				last_week_last_month = last_month[-1]
				for last_month_day in last_week_last_month:
					print(last_month_day)
					day_of_last_month, day_of_last_week = last_month_day
					print("test", day_of_last_month, day_of_last_week)
					if day_of_week == some_day_input:
						day_date = day_of_last_month
						month_date = this_month - 1
						if month_date <= 0:
							month_date = 12 - month_date
							print("test2", month_date)
						break
			break
	print(day_date, month_date)
	


		
day_text_input, day_number_input = day_list()
day_of_the_year_working(day_of_the_year_now(), day_number_input)
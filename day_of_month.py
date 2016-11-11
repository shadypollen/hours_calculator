import datetime
import calendar

now = datetime.datetime.now()
cal = calendar.Calendar()
this_year = now.year
this_month = now.month 
month_list = cal.monthdays2calendar(now.year, this_month)
current_day_of_month = 7#now.day

def day_list():
	#Returns the day of the week you've worked and it's ordinal number
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
			if day_of_month == current_day_of_month: 
				current_week_index = month_list.index(i)
				current_day_of_week = day_of_week
				print(current_week_index, current_day_of_week)
				return(current_week_index, current_day_of_week)

def work_week_index_finder(day_tuple):
	current_week_index, current_day_of_week = day_tuple
	is_it_last_month = False
	if current_day_of_week == 0:
		work_week_index = current_week_index - 1
		if work_week_index <= 0:
			is_it_last_month = True
	else:
		work_week_index = current_week_index
	print(work_week_index, is_it_last_month)
	return(work_week_index, is_it_last_month)

def find_list_of_last_week(work_week_index, is_it_last_month):
	if is_it_last_month == True:
		work_month = this_month - 1
		if work_month <= 0:
			work_month = 13 - this_month
			work_year = this_year - 1
		else:
			work_year = this_year
	else:
		work_month = this_month
		work_year = this_year
	print(work_month, work_year)
	return(work_month, work_year)
	
def find_day_and_month_of_working(work_month, work_year, day_ordinal_output, is_it_last_month, work_week_index):
	print("testtest", day_ordinal_output)
	if is_it_last_month == True:
		work_week_list = cal.monthdays2calendar(work_year, work_month)
		print(work_week_list)
		for week in reversed(work_week_list):
			for day in reversed(week):
				day_of_month, day_of_week = day
				if day_of_week == day_ordinal_output:
					if day_of_month == 0:
						next_week_list = cal.monthdays2calendar(work_year, work_month+1)[0]
						for day in next_week_list:
							day_of_month, day_of_week = day 
							if day_of_week == day_ordinal_output:
								return(day_of_month)
					else:
						return(day_of_month)
	else:
		work_week_list = cal.monthdays2calendar(work_year, work_month)
		for day in work_week_list[work_week_index]:
			day_of_month, day_of_week = day 
			if day_of_week == day_ordinal_output:
				if day_of_month == 0:
					next_week_list = cal.monthdays2calendar(work_year, work_month+1)[0]
					for day in next_week_list:
						day_of_month, day_of_week = day 
						if day_of_week == day_ordinal_output:
							return(day_of_month)
				else:
					return(day_of_month)
	
	


		
day_text_output, day_ordinal_output = day_list()
print("test1", day_ordinal_output)
today_week_output = day_of_the_year_now()
work_week_index, is_it_last_month = work_week_index_finder(today_week_output)
work_month, work_year = find_list_of_last_week(work_week_index, is_it_last_month)
worked_day_of_month = find_day_and_month_of_working(work_month, work_year, day_ordinal_output, is_it_last_month, work_week_index)
print("worked day of month", worked_day_of_month, "worked month ouput:",work_month)
"""Output worked_day_of_month, worked_month and worked_year"""

#Figure out a way to properly write months
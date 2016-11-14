import datetime
import calendar

now = datetime.datetime.now()
cal = calendar.Calendar()
this_year = now.year
this_month = now.month 
month_list = cal.monthdays2calendar(now.year, this_month)
current_day_of_month = now.day

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

def find_week_index_by_day_m(month_list, search_day):
	#Finds index of this week and the day of the week
	for week in month_list:
		for day in week:
			day_of_month, day_of_week = day
			if day_of_month == search_day: 
				current_week_index = month_list.index(week)
				current_day_of_week = day_of_week
				return(current_week_index, current_day_of_week)

def find_day_w_in_last_month(month_list, search_day_w):
	for day in month_list[-1]:
		day_m, day_w = day 
		if day_w == search_day_w:
			return(day_m)

def work_week_index_finder(work_week_index, current_day_of_week, day_ordinal_output):
	if current_day_of_week == 0:
		work_week_index -= 1
	for day in month_list[work_week_index]:
		day_m, day_w = day
		if day_w == day_ordinal_output:
			if day_m == 0:
				last_month_list = cal.monthdays2calendar(now.year, this_month-1)
				worked_day_m = find_day_w_in_last_month(last_month_list, day_ordinal_output)
				return(this_month-1, worked_day_m)
			elif day_m != 0:
				return(this_month, day_m)

		
day_text_output, day_ordinal_output = day_list()
current_week_index, current_day_of_week = find_week_index_by_day_m(month_list, current_day_of_month)
work_month, work_day_m = work_week_index_finder(current_week_index,
	 current_day_of_week, day_ordinal_output)
print("Day worked: %d, month worked: %d" % (work_day_m, work_month))
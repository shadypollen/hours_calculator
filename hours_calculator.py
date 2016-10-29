import datetime
import calendar
import sqlite3

conn = sqlite3.connect("workhours.db")
cursor = conn.cursor()

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
#Work on a better way to calculate the date using last week and today's day, so it 
#won't cause bugs on weeks that have a start of the next month in them
def day_of_the_year():
	now = datetime.datetime.now()
	calendar.prmonth(now.year, now.month)
	day_of_the_month = int(input("Enter the day of the month: "))
	return(day_of_the_month, now.month, now.year)

def which_week(year, month, day):
	date_that_week = datetime.date(year, month, day)
	no_of_week = date_that_week.isocalendar()[1]
	return no_of_week

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

def start_end_hours_string(start_hours, start_minutes, finish_hours, finish_minutes):
	return_string = "%.2i:%.2i-%.2i:%.2i" % (start_hours, start_minutes, finish_hours, finish_minutes)
	return return_string


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

def hour_string_output(paid_hours, paid_minutes):
	return_string = "%ih:%im" % (paid_hours, paid_minutes)
	return return_string

def estimate_pay(paid_total):
	raw_estimate_val = (8.2/60) * paid_total
	output_string = round(raw_estimate_val, 2)
	return output_string

#Calculates how many hours you worked in a week
#NB! Be careful of which value is selected as "pay_each_day"
def week_calculator(days_hours_input):
	week_hours = []
	days_hours_list = list(days_hours_input)
	for day in days_hours_list:
		week_hours.append(day)
	sum_hours = sum(week_hours)
	print(week_hours)
	print(sum_hours)
	hours_worked = int(sum_hours/60)
	minutes_worked = sum_hours%60
	output_string = "%.2ih %.2im" % (hours_worked, minutes_worked)
	print(output_string)

	paid_total_pw = (8.2/60)* sum_hours
	paid_total_pw = round(paid_total_pw, 2)
	print(paid_total_pw)
	return(output_string, paid_total_pw)



def create_table():
	cursor.execute("""CREATE TABLE IF NOT EXISTS week_hours 
		(no_of_week INTEGER, hours_worked_weekly TEXT, week_pay_estimate REAL)""")
	cursor.execute("""CREATE TABLE IF NOT EXISTS day_hours 
		(no_of_week INTEGER, what_day TEXT, full_date TEXT, start_fin_hours TEXT, hours_worked_daily TEXT, daily_pay_estimate REAL)""")


def daily_sql_insert(day_hours_counter):
	list_of_days = list(day_hours_counter)
	for day in list_of_days:
		no_of_week, day_of_week, date, start_fin_hours, paid_hours, estimated_pay = day
		cursor.execute("""INSERT INTO day_hours 
			(no_of_week, what_day, full_date, start_fin_hours, hours_worked_daily, daily_pay_estimate) 
			VALUES(?, ?, ?, ?, ?, ?)""", (no_of_week, day_of_week, date, start_fin_hours, paid_hours, estimated_pay))
		conn.commit()

def weekly_sql_insert(week_number, hours_pw, paid_pw):
	cursor.execute("""INSERT INTO week_hours
		(no_of_week, hours_worked_weekly, week_pay_estimate)
		VALUES(?, ?, ?)""", (week_number, hours_pw, paid_pw))
	conn.commit()
		
#Brings functions together
def var_collector():
	day_hours_counter = []
	weekly_hours_counter = []
	global week_number
	create_table()
	while True:
		user_input = input("Press ENTER to input a day or type 'End' if you'd like to finish:  \n")
		if user_input.lower() == "end":
			#These are the vars needed for the weekly table

			hours_pw, paid_pw = week_calculator(weekly_hours_counter)
			daily_sql_insert(day_hours_counter)
			weekly_sql_insert(week_number, hours_pw, paid_pw)
			cursor.close()
			conn.close()
			break
		else:
			#These are the vars needed for the daily table

			#outputs the day of the week
			day_input = day_list()
			#outputs a string of the month's day
			day_date, month_date, year_date = day_of_the_year()
			date_string = str("%d-%d-%d" % (day_date, month_date, year_date))

			week_number = which_week(year_date, month_date, day_date)
			#inputs for beginning and end of shift
			start_hours, start_minutes = start_hours_list()
			finish_hours, finish_minutes = finish_hours_list()
			start_fin_hours_return = start_end_hours_string(start_hours, start_minutes, finish_hours, finish_minutes)
			#calculates the amount of hours worked - breaks
			paid_hours, paid_minutes = hour_calculator(start_hours, start_minutes, finish_hours, finish_minutes)
			hours_output_string = hour_string_output(paid_hours, paid_minutes)
			paid_total = paid_hours * 60 + paid_minutes
			#estimates the pay
			estimated_pay = estimate_pay(paid_total)
			#appends all the values for each day as a tuple in a list
			day_hours_counter.append((week_number, day_input, date_string, 
				start_fin_hours_return, hours_output_string, estimated_pay))
			weekly_hours_counter.append(paid_total)
	#displays the total hours worked per week
	
	
	#creates the table and writes inputs in it





def main():
	var_collector()


main()


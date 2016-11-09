import sqlite3
import day_class

conn = sqlite3.connect("workhours.db")
cursor = conn.cursor()


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
			weekly_sql_insert(day_var.week_number, hours_pw, paid_pw)
			cursor.close()
			conn.close()
			break
		else:
			#These are the vars needed for the daily table
			day_var = day_class.day_container()
			#appends all the values for each day as a tuple in a list
			day_hours_counter.append((day_var.week_number, day_var.day_input, day_var.date_string, 
				day_var.start_fin_hours_return, day_var.hours_output_string, day_var.estimated_pay))
			weekly_hours_counter.append(day_var.paid_total)





def main():
	var_collector()


main()


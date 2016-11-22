import day_class
import write_sql_actions
import hold_sql_actions

def week_calculator(days_hours_input):
	week_hours = []
	days_hours_list = list(days_hours_input)
	for day in days_hours_list:
		week_hours.append(day)
	sum_hours = sum(week_hours)
	hours_worked = int(sum_hours/60)
	minutes_worked = sum_hours%60
	output_string = "%.2ih %.2im" % (hours_worked, minutes_worked)
	paid_total_pw = (8.2/60)* sum_hours
	paid_total_pw = round(paid_total_pw, 2)
	return(output_string, paid_total_pw)

#Brings functions together
def var_collector():
	day_hours_counter = []
	weekly_hours_counter = []
	while True:
		print("Press ENTER to input a day.\r")
		print("Type 'Hold' if you'd like to leave your hours on hold.\r")
		user_input = input("Type 'End' if you'd like to write current days into the database.\n")
		if user_input.lower() == "end":
			#These are the vars needed for the weekly table
			sql_object = write_sql_actions.sqlite_actions()
			sql_hold_object = hold_sql_actions.sqlite_actions()
			hold_hours = sql_hold_object.fetch_days()
			hold_paid_total = sql_hold_object.fetch_total_hours()
			hold_week_no = sql_hold_object.fetch_week_no()
			weekly_hours_counter.append(hold_paid_total)
			for day in hold_hours:
				day_hours_counter.append(day)
			
	#####Figure out a way how to week_calculator with hold functions
	#####Tip:Make another table for hold_hours where you keep the paid total values to later extract them

			hours_pw, paid_pw = week_calculator(weekly_hours_counter)
			sql_object.daily_sql_insert(day_hours_counter)
			if hold_week_no is None:
				sql_object.weekly_sql_insert(day_var.week_number, hours_pw, paid_pw)
			else:
				sql_object.weekly_sql_insert(hold_week_no[0], hours_pw, paid_pw)
			sql_object.sql_close()
			sql_hold_object.sql_delete_and_close()
			break

		elif user_input.lower() == "hold":
			sql_hold_object = hold_sql_actions.sqlite_actions()
			sql_hold_object.daily_sql_insert(day_hours_counter)
			sql_hold_object.paid_total_insert(weekly_hours_counter, day_var.week_number)
			sql_hold_object.sql_close()
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


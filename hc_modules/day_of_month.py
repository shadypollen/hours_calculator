import datetime
import calendar

now = datetime.datetime.now()
cal = calendar.Calendar()
this_year = now.year
this_month = now.month 
current_day_of_month = now.day
month_list = cal.monthdays2calendar(this_year, this_month)


class date_container:
	def __init__(self):
		self.day_text_output, self.day_ordinal_output = self.day_list()
		self.current_week_index, self.current_day_of_week = self.find_week_index_by_day_m(month_list, current_day_of_month)
		self.work_month, self.work_day, self.work_year = self.work_week_index_finder(self.current_week_index,
	 	self.current_day_of_week, self.day_ordinal_output)
		print("You worked on",self.work_day, self.work_month, self.work_year) 


	def day_list(self):
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

	def find_week_index_by_day_m(self, month_list, search_day):
		#Finds index of this week and the day of the week
		for week in month_list:
			for day in week:
				day_of_month, day_of_week = day
				if day_of_month == search_day: 
					current_week_index = month_list.index(week)
					current_day_of_week = day_of_week
					return(current_week_index, current_day_of_week)

	def find_day_w_in_last_month(self, month_list, search_day_w):
		#finds the day you've worked in the last month
		for day in month_list[-1]:
			day_m, day_w = day 
			if day_w == search_day_w:
				return(day_m)


	def work_week_index_finder(self, work_week_index, current_day_of_week, day_ordinal_output):
		#works for middle-of-the-month calculations but not for beginning-month calcs
		if current_day_of_week <= day_ordinal_output:
			work_week_index -= 1
			print("test test")
		for day in month_list[work_week_index]:
			day_m, day_w = day
			if day_w == day_ordinal_output:
				if day_m == 0:
					working_year = this_year
					last_month = this_month-1
					if last_month < 1:
						last_month = 12
						working_year = this_year - 1
					last_month_list = cal.monthdays2calendar(working_year, last_month)
					worked_day_m = self.find_day_w_in_last_month(last_month_list, day_ordinal_output)
					return(last_month, worked_day_m, working_year)
				elif day_m != 0:
					return(this_month, day_m, this_year)

	def which_week(self):
		date_that_week = datetime.date(self.work_year, self.work_month, self.work_day)
		no_of_week = date_that_week.isocalendar()[1]
		return no_of_week



		



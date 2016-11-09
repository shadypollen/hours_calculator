import datetime
import calendar

class day_container:
	def __init__(self):
		self.day_input = self.day_list()
		self.day_date, self.month_date, self.year_date = self.day_of_the_year()
		self.date_string = str("%d-%d-%d" % (self.day_date, self.month_date, self.year_date))
		self.week_number = self.which_week(self.year_date, self.month_date, self.day_date)
		#inputs for beginning and end of shift
		self.start_hours, self.start_minutes = self.start_hours_list()
		self.finish_hours, self.finish_minutes = self.finish_hours_list()
		self.start_fin_hours_return = self.start_end_hours_string(self.start_hours,
			self.start_minutes, self.finish_hours, self.finish_minutes)
		#calculates the amount of hours worked - breaks
		self.paid_hours, self.paid_minutes = self.hour_calculator(self.start_hours, 
			self.start_minutes, self.finish_hours, self.finish_minutes)
		self.hours_output_string = self.hour_string_output(self.paid_hours, self.paid_minutes)
		self.paid_total = self.paid_hours * 60 + self.paid_minutes
		#estimates the pay
		self.estimated_pay = self.estimate_pay(self.paid_total)

	#Inputs the day of the week
	def day_list(self):
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
	def day_of_the_year(self):
		now = datetime.datetime.now()
		calendar.prmonth(now.year, now.month)
		day_of_the_month = int(input("Enter the day of the month: "))
		return(day_of_the_month, now.month, now.year)

	def which_week(self, year, month, day):
		date_that_week = datetime.date(year, month, day)
		no_of_week = date_that_week.isocalendar()[1]
		return no_of_week

	#Inputs beginning of the shift
	def start_hours_list(self):
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
	def finish_hours_list(self):
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

	def start_end_hours_string(self, start_hours, start_minutes, finish_hours, finish_minutes):
		return_string = "%.2i:%.2i-%.2i:%.2i" % (start_hours, start_minutes, finish_hours, finish_minutes)
		return return_string

	#Calculates how many hours you worked and subtracts breaks
	#REWRITE THIS LATER WITH DIVMODS
	def hour_calculator(self, begin_hours, begin_minutes, fin_hours, fin_minutes):
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

	def hour_string_output(self, paid_hours, paid_minutes):
		return_string = "%ih:%im" % (paid_hours, paid_minutes)
		return return_string

	def estimate_pay(self, paid_total):
		raw_estimate_val = (8.2/60) * paid_total
		output_string = round(raw_estimate_val, 2)
		return output_string


test = day_container()
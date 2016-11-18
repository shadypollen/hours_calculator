import sqlite3

conn = sqlite3.connect("_workhours.db")
cursor = conn.cursor()
hold_hours = []

class sqlite_actions:
	def __init__(self):
		self.create_table()

	def create_table(self):
		cursor.execute("""CREATE TABLE IF NOT EXISTS day_hours 
			(no_of_week INTEGER, what_day TEXT, full_date TEXT, start_fin_hours TEXT, hours_worked_daily TEXT, daily_pay_estimate REAL)""")

	def daily_sql_insert(self, day_hours_counter):
			list_of_days = list(day_hours_counter)
			for day in list_of_days:
				no_of_week, day_of_week, date, start_fin_hours, paid_hours, estimated_pay = day
				cursor.execute("""INSERT INTO day_hours 
					(no_of_week, what_day, full_date, start_fin_hours, hours_worked_daily, daily_pay_estimate) 
					VALUES(?, ?, ?, ?, ?, ?)""", (no_of_week, day_of_week, date, start_fin_hours, paid_hours, estimated_pay))
				conn.commit()

	def fetch_days(self):
		cursor.execute("SELECT * FROM day_hours")
		for row in cursor.fetchall():
			hold_hours.append(row)
		print(hold_hours)


	def sql_close(self):
		cursor.close()
		conn.close()

if __name__ == "__main__":
	test = sqlite_actions()

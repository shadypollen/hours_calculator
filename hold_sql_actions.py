import sqlite3

conn = sqlite3.connect("hold_workhours.db")
cursor = conn.cursor()

class sqlite_actions:
	def __init__(self):
		self.create_table()

	def create_table(self):
		cursor.execute("""CREATE TABLE IF NOT EXISTS day_hours 
			(no_of_week INTEGER, what_day TEXT, full_date TEXT, start_fin_hours TEXT, hours_worked_daily TEXT, daily_pay_estimate REAL)""")
		cursor.execute("""CREATE TABLE IF NOT EXISTS hold_pay_total
			(hold_paid_minutes INTEGER, no_of_week INTEGER)""")

	def daily_sql_insert(self, day_hours_counter):
			list_of_days = list(day_hours_counter)
			for day in list_of_days:
				no_of_week, day_of_week, date, start_fin_hours, paid_hours, estimated_pay = day
				cursor.execute("""INSERT INTO day_hours 
					(no_of_week, what_day, full_date, start_fin_hours, hours_worked_daily, daily_pay_estimate) 
					VALUES(?, ?, ?, ?, ?, ?)""", (no_of_week, day_of_week, date, start_fin_hours, paid_hours, estimated_pay))
				conn.commit()

	def paid_total_insert(self, weekly_hours_counter, no_of_week):
			list_of_hours_worked = list(weekly_hours_counter)
			for day in list_of_hours_worked:
				cursor.execute("""INSERT INTO hold_pay_total
					(hold_paid_minutes, no_of_week)
					VALUES(?, ?)""", (day, no_of_week))
				conn.commit()

	def fetch_days(self):
		hold_days = []
		cursor.execute("SELECT * FROM day_hours")
		for row in cursor.fetchall():
			hold_days.append(row)
		return hold_days

	def fetch_total_hours(self):
		hold_hours = []
		cursor.execute("SELECT hold_paid_minutes FROM hold_pay_total")
		[hold_hours.append(row[0]) for row in cursor.fetchall()]
		paid_total = sum(hold_hours)
		return paid_total

	def fetch_week_no(self):
		cursor.execute("SELECT no_of_week FROM hold_pay_total")
		week_no = cursor.fetchone()
		return week_no

	def sql_delete_and_close(self):
		cursor.execute("""DROP TABLE hold_pay_total""")
		cursor.execute("""DROP TABLE day_hours""")
		cursor.close()
		conn.close()

	def sql_close(self):
		cursor.close()
		conn.close()

if __name__ == "__main__":
	test = sqlite_actions()

# Work Hours Calculator

A small CLI app that records the day you've worked, your hours, subtracts unpaid times from break and records data into a SQLite-database.

##Necessary libraries
* SQLite
* Python 3.5 or newer

##Using the app

Download the zip of the master branch or clone the repository and run
```
python3 hours_calculator.py
```

##Features

* Automatically calculates last week's day, month and year based on the day of the week you input(Mon-Sun)
* Able to hold hours before inputting them into the main DB via the hold command
* Stores days worked in two tables - one for a weekly overview and another for a day-by-day view of days worked in a week

##Future plans

* Improve configurability
* Make the day of the month finding module more flexible
* Add an option for using GUI implemented via tkinter

##Author

* **Aleksandr Leokin** - *Initial work* - [shadypollen](https://github.com/shadypollen)

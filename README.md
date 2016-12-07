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

* Automatically calculates last week's day, month and year based on the day of the week you input(Mon-Sun). For example, if you input Friday and today is Tuesday, it will automatically find last Friday's date.
* Able to hold hours before inputting them into the main DB via the hold command
* Stores days worked in two tables - one for a weekly overview and another for a day-by-day view of days worked in a week

##Future plans

* Improve configurability
* Add an option to display hours on hold
* Create a fork with GUI implemented via tkinter
* Port the program as a web app using Flask

##Author

* **Aleksandr Leokin** - *Initial work* - [shadypollen](https://github.com/shadypollen)

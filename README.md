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

Follow the instructions given on screen and after you have entered all the necessary data the program will create 2 tables. One is for a day-by-day view of how much you've worked per week and the second one is a weekly overview.

##Author

* **Aleksandr Leokin** - *Initial work* - [shadypollen](https://github.com/shadypollen)

##Future plans

* Add an option for using GUI implemented via tkinter

##Update log

* 21.11.16 - Added a hold function

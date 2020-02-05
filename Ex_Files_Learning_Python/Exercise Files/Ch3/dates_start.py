#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime
def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("heute: ",today)
  print("Datum-Komponenten: ",today.day,today.month,today.year)
  # print out the date's individual components

  # retrieve today's weekday (0=Monday, 6=Sunday)
  days = ["montag","dienstag","mittwoch","donnerstag","freitag","samstag","sonntag"]
  print("heute ist ", days[today.weekday()])
  
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("datetime heute : ", today)

  # Get the current time
  t = datetime.time(datetime.now())
  print(t)

  
if __name__ == "__main__":
  main();
  
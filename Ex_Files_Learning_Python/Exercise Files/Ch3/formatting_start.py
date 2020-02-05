#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  print(now.strftime("in Jahr des Herrn:  %Y"))
  print(now.strftime("Pretty Date:  %a, %d %B, %y"))
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("Pretty Date:  %a, %d %B, %y"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Datum/Uhrzeit:  %c"))
  print(now.strftime("Uhrzeit:  %X"))
  print(now.strftime("Datum:  %x"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("die Zeit/12h:  %I:%M:%S %p"))
  print(now.strftime("die Zeit/24h:  %H:%M:%S"))


if __name__ == "__main__":
  main();

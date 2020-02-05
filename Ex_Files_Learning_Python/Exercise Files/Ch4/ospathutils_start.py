#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print("exists:" + str(path.exists("textfile2.txt")))
  print("a file:" + str(path.isfile("textfile2.txt")))
  print("a directory:" + str(path.isdir("textfile2.txt")))
  # Work with file paths
  print("realpath:" + str(path.realpath("textfile2.txt")))
  print("path and name:" + str(path.split(path.realpath("textfile2.txt"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("textfile2.txt"))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("textfile2.txt")))
  # Calculate how long ago the item was modified
  td = datetime.datetime.now()-datetime.datetime.fromtimestamp(
    path.getmtime("textfile2.txt")
  )
  print("vor " +str(td)+ " wurde diese datei modifiziert")
  print("vor " +str(td.total_seconds())+ " sec wurde diese datei modifiziert")
if __name__ == "__main__":
  main()

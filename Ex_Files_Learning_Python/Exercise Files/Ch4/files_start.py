#
# Read and write files using the built-in Python file methods
#
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():  
  # Open a file for writing and create it if it doesn't exist
  #f = open("textfile2.txt","w+")

  # Open the file for appending text to the end
  f = open("textfile2.txt","r")

  # write some lines of data to the file
  now = datetime.now()
  for i in range(20):
      line = "Heute in " +str(i) + " Tagen: " + str(now + timedelta(days=i))
     # f.write(line+"\r\n")
  # close the file when done
  #f.close()
  
  # Open the file back up and read the contents
  if f.mode == 'r':
        #contents = f.read()
      fl = f.readlines()
      for x in fl:
          print(x)
      #print(contents)
    
if __name__ == "__main__":
  main()

#
# Example file for working with conditional statements
#
# print("test")
def main():
  x, y = 100, 100
  
  # conditional flow uses if, elif, else  
  if (x < y):
        st = "x < y"
  elif (x==y):
        st = "gleich"
  else:
        st = "x was anderes y"
  print (st)
  # conditional statements let you use "a if C else b"
  st = "x is y" if (x<y) else "x >nnn y"
  print (st)

if __name__ == "__main__":
  main()

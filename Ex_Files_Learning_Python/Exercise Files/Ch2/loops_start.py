#
# Example file for working with loops
#

def main():
  x = 0
  n = 10

  # define a while loop
  while (x < n):
      # 0;1;2;3;4;5;6;7;8;9;
      print(x, end=";")
      x = x + 1


  # define a for loop
  print("\n------------------------------------------------------")
  tools = ["Rad","Lenker","Klingel","Bremse","Lampe"]
  for tool in tools:
    print(tool)

  # use a for loop over a collection
  for a in range(90,101):
    print(a, end=";")
 
  # use the break and continue statements
  print("\n")
  for i,tool in enumerate(tools):
        if (tool == "Klingel"): break 
        print(tool,i)

  #using the enumerate() function to get index 


if __name__ == "__main__":
  main()

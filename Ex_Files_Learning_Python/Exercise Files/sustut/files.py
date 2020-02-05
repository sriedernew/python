def main(): 

    f = open("kleine_paddelei.txt","a+")

    # in einer Dauerschleife. Ein do ... wihle habe ich nicht gefunden
    while True:
        x = input("Enter boot:")
        if x == "ende":
            break
        y = input("Enter km:")
        z = input("Enter Min:")
        text = "{},{},{}\n"
        print(text.format(x, y, z))
        f.write(text.format(x, y, z))
    f.close()

    # nach dem beenden des Schreibvorgang zu machen, ist sauberer
    f = open("kleine_paddelei.txt","r")
    mw = 0.00
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
          print(x.lower().split(",")[0])
          mw = mw+float(x.split(",")[1])
        text = "im Mittel war ich {} km unterweg"
        print(text.format(round(mw/len(fl),2)))
          
# damit ich main nicht extra aufrufen muß
if __name__ == "__main__":
  main()
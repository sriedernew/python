def main():
    text = "b={} ist größer als a={}"
    a = 33
    b = 200
    # größer als
    if b > a:
        print(text.format(str(b),str(a)))
    # b ist nicht a
    if b != a:
        text = "b={} ist nicht a={}"
        print(text.format(str(b),str(a)))
    # wenn ... dann ..., sonst das ...
    if b == a:
        text = "b={} ist a={}"
    else:
        text = "b={} ist nicht a={}"
    print(text.format(str(b),str(a)))
     # wenn ... dann ..., aber wenn ... dann so ... und sonst das ...
    if b == a:
        text = "b={} ist a={}"
    elif b < a:
        text = "b={} ist kleiner als a={}"
    else:
        text = "b={} ist nicht a={}"
    print(text.format(str(b),str(a)))
    text = "b={} ist größer als a={}"
    # Kurzfassung if
    if a < b: print(text.format(str(b),str(a)))
    # Kurzfassung else if
    print("b={} ist größer als a={}".format(str(b),str(a))) if a > b else print("b={} ist nicht a={}".format(str(b),str(a)))

    # and, or, || oder && geht nicht
    if a < b or a < 200:
        print("test or")
    else:
        print("test else or")
        
# damit ich main nicht extra aufrufen muß
if __name__ == "__main__":
  main()
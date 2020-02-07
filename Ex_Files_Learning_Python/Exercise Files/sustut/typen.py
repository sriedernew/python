def main(): 
    # int zu str = str(6) = "6"
    s = "Ein Casting für "
    print(s+str(2))
    print(type(s+str(2)))

    # str zu int = int("9") = 9
    print(9*int("9"))
    print(type(9*int("9")))

    # str zu float
    print(10+float("9.123")) #19.122999999999998 interessant 
    print(type(10+float("9.123")))

    # float zu int
    print(10+int(9.123))
    print(type(10+int(9.123)))

    # komplexe Zahlen
    x = 1j
    print(x)
    print(type(x))

    # arrays = List
    x = ["Tanker","Passenger","Tug","Container Ship","General Cargo Ship"]
    print(x)
    print(type(x))

    # Tubel = Samlung
    x = ("Tanker","Passenger","Tug","Container Ship","General Cargo Ship")
    print(x)
    print(type(x))

    # Set = Hash
    x = {"Tanker","Passenger","Tug","Container Ship","General Cargo Ship"}
    print(x)
    print(type(x))

    # Dic ~ assoziatives Array, Hash
    x = {"name":"Queen Mary II","Type":"passanger","Flag":"Panama"}
    print(x)
    print(type(x))
    print(x["name"])
    #print(x.name)

    # Range = von 1 bis 10
    x = range(20)
    print(x)
    print(type(x))

    # Boolean = Bool
    x = True
    print(x)
    print(type(x))

    # Boolean = Bool
    x = 2 > 3
    print(x)
    print(type(x))

    print(bool(False))
    print(bool(None))
    print(bool(0))
    print(bool(""))
    print(bool(()))
    print(bool([]))
    print(bool({}))
    a=""
    b=None
    print(bool(a))
    if bool(a):
        print ("a hat einen Inhalt")
    else:
        print ("a ist leer")
    
    if bool(b):
        print ("b ist da")
    else:
        print ("b ist nicht da")

    if b:
        print ("b ist da")
    else:
        print ("b ist nicht da")

# damit ich main nicht extra aufrufen muß
if __name__ == "__main__":
  main()
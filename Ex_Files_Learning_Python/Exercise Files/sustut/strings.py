def main(): 
    s = "Hallo Welt:"
    print (s)
    print(s+str(42))
    
# Eigenname in Anführungstriche
    s = 'Hallo "Susann"'
    print (s)

# von Zeichen 1 bis 4 beginnt mit 0, juchhu wie in Excel
    print(s[1])
    print(s[1:4]) # Slicing
    print(s[-4:-1]) # negativ Slicing

# die Suche nach dem großem S
    x = "S" in s
    print(x)
    x = "S" not in s
    print(x)
    print(s.find("S"))

# wie lang ist der String
    print(len(s))

# Trim heißt hier Strip
    s = " Hallo Welt! Hallo Susann."
    print(s)
    print(s.strip())

# alles klein alles gross
    print(s.strip().lower())
    print(s.strip().upper())

# böse Zeichen entfernen
    bs = "Wegner &ngt Söhne in Magś\nElektrohandel"
    print(bs)
    print(bs.replace("\n"," "))

# ich packe meinen Koffer und lege einen Strumpf, ein paar Schuhe usw.
    print(bs.replace("\n"," ").replace("ś","s").replace("&ngt","&"))
    print(bs.replace("\n"," ").replace("ś","s").replace("&ngt","&").encode())

# aus string mach arrays explode heißt hier split
    sa = "Monika, Bärbel, Gudrun, Sabine"
    ars = sa.split(", ")
    print (ars)
    print (ars[2])
    print (len(ars[2]))
    print (len(ars))

# string format, wie printf
    alter = 12
    gross = 40
    text = "Meine Nichte ist {} Jahre alt."
    print(text.format(alter))
    text = "Meine Nichte ist {} Jahre alt und 1 Meter {} groß."
    print(text.format(alter,gross))
    text = "Meine Nichte ist {1} Jahre alt und 1 Meter {0} groß."
    print(text.format(alter,gross))

# für die ASCII-Kunst
    text = "x"
    x = text.zfill(10)
    print(x)

# wenn man mal etwas teilen muß
    text = "Heinz Martin, Alter 89"
    x = text.partition(", Alter")
    print(x)
    name = x[0]
    alter = x[2]
    text = "Meine Opa ist {1} Jahre alt und heißt {0}."
    print(text.format(name,alter))

# 3 auf einen Streich
    text = "3 {1} im Haar, {2} an den Ohren und {0} an den Hüften."
    x, y, z = "Orange", "Banana", "Kirchen"
    print(text.format(y,x,z))

# damit ich main nicht extra aufrufen muß
if __name__ == "__main__":
  main()
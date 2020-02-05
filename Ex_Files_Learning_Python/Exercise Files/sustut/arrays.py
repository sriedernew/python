# Arrays, Listen, Hash, Tupels, Dictionaris, Json

def main():
# Eine Liste = ein normales Array
    schiffe = ["QM II","Titatic","United Staats","Deutschland","Frau Glitscher"]
    print(type(schiffe))
    print(schiffe)
    print(schiffe[1])
    print(len(schiffe))
    print(str(schiffe))
    nummern = [1,2,3,4,5]
    print(type(nummern))
    print(nummern)
    print(nummern[1])
    print(len(nummern))
    for x in schiffe:
      print(x)

# anhängen
    schiffe.append("River Queen")
    for x in schiffe:
      print(x)

# suchen und wie oft gefunden
    print(schiffe.count("Deutschland"))

# löschen
    schiffe.pop(0)
    for x in schiffe:
      print(x)

# löschen mit suchstring
    schiffe.remove("Frau Glitscher")
    for x in schiffe:
      print(x)

# wiede voll
    print("------------------------------------------------------------------------------")
    schiffe = ["QM II","Titatic","United Staats","Deutschland","Frau Glitscher"]
    for x in schiffe:
      print(x)

# sortieren
    print("------------------------------------------------------------------------------")
    schiffe.sort()
    for x in schiffe:
          print(x)

# sortieren mit Function der Länge nach
    print("------------------------------------------------------------------------------")
    schiffe.sort(key=sortFunc)
    for x in schiffe:
          print(x)
    print("------------------------------------------------------------------------------")  

# Tuple, Arrays in runden Klammern?
    baeume = ("kiefer", "tanne", "linde", "erle", "eiche", "esche", "fichte")
    print(type(baeume))
    print(baeume[2:5])
    if "erle" in baeume:
      print("Erle ist drinn")
    # print(baeume.sort()) -> AttributeError: 'tuple' object has no attribute 'sort'
    # tuble kann man nicht verlängern also baeume[7] = "Buchsbaum" geht nicht
    # man kann es als vordefinierte Auswahlliste benutzen
    x = baeume.index("linde")
    print(x)
    print("------------------------------------------------------------------------------")  

# Set, Hashlist
    tiere = {"hund","katze","maus","hase","fuchs","reh"}
    print(type(tiere))
    #print(tiere[2:5]) geht nicht
    for x in tiere:
        print(x)
    print("reh" in tiere)
    tiere.add("leoprad")
    for x in tiere:
        print(x)
    tiere.update(["leopard","hund","katze","maus","hase","fuchs","reh"])
    for x in tiere:
        print(x)
    pflanzen ={"baum","blume","gras","strauch","getreide"}
    arten = tiere.union(pflanzen)
    for x in arten:
        print(x)
    print("------------------------------------------------------------------------------")  

# Dictionaries, assoziatieve Arrays, Hash
    schiff = {
    "name": "QM II",
    "flag": "Pananma",
    "type": "Passenger"
    }
    print(type(schiff))
    print(schiff)
    print(schiff["name"])
    schiff["name"] = "Deutschland"
    print(schiff["name"])
    schiff["imo"] = 9955992
    for x in schiff:
        print(x,schiff[x])
    for x in schiff.values():
        print(x)
    schiffe = {
        "schiff1" : {
            "name" : "QM ||",
            "year" : 2004
        },
        "schiff2" : {
            "name" : "Deutschlands",
            "year" : 1987
        },
        "schiff3" : {
            "name" : ["River Queen","tante emmma"],
            "year" : 1847
        }
    }
    print(type(schiffe))
    print(schiffe["schiff3"]["name"][1])

# damit ich main nicht extra aufrufen muß
def sortFunc(e):
    return len(e)

if __name__ == "__main__":
  main()
# Function mit parameter als Dictionary
def plusRechnung(**zahlen):
    summe=0
    print(type(zahlen))
    for summant in zahlen.values():
        summe = summe + summant
    print(summe)
plusRechnung(a=54,b=33,c=123)

# Function mit parameter tupel
def plusRechnungBesser(*zahlen):
    summe=0
    print(type(zahlen))
    for summant in zahlen:
        summe = summe + summant
    print(summe)
plusRechnungBesser(54,33,23)

def fileLesen(filename):
    f = open(filename,"r")
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
          print(x) 
fileLesen("kleine_paddelei.txt")
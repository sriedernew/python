# ein Kommentar
# eine Berechnung
a = 22.34
b = 0.99
c = a/b
print(c)
# rechenfunktion
def runden(wert):
    print (round(wert))
    print (round(wert,2))
    # mit return kein none
    return round(wert,1)
print(runden(c))
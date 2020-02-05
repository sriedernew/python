import numpy
import matplotlib.pyplot as plt
from scipy import stats
def main(): 
    f = open("kleine_paddelei.txt","r")
    mw = 0.00
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
          print(x.lower().split(",")[0])
          mw = mw+float(x.split(",")[1])
        text = "im Mittel war ich {} km unterweg"

# Mittelwert mit summe und len
        print(text.format(round(mw/len(fl),2)))

# mit numpy
        ar_km = []
        ar_time = []
        for x in fl:
            ar_km.append(float(x.split(",")[1]))
            ar_time.append(int(x.split(",")[2]))
        text = "numpy: Im Mittel war ich {} km unterweg."
        print(text.format(round(numpy.mean(ar_km),2)))
        text = "numpy: In der Mitte steht {} km."
        print(text.format(numpy.median(ar_km)))
        text = "stats: Am meisten bin ich {} km gepaddelt und zwar {} mal."
        print(text.format(float(stats.mode(ar_km)[0]),int(stats.mode(ar_km)[1])))

        text = "numpy: Die Standardabweichung ist {} km."
        print(text.format(round(numpy.std(ar_km),2)))
        text = "numpy: Die Variance ist {} km."
        print(text.format(round(numpy.var(ar_km),2)))

        text = "numpy: {} Prozent der zu erwartenden gepaddelten km könnten den Wert {} haben, wenns nach der Normalverteilung geht."
        print(text.format(round(numpy.percentile(ar_km,20),2),20))

# Grafik plotten
        print("Chart 1")
        x = numpy.random.uniform(0.0, 5.0, 250)
        plt.hist(x, 100)
        plt.show()

# geht das auch mit ar_km
        print("Chart 2")
        plt.hist(ar_km, 10)
        plt.show()

# geht das auch mit ar_km und numpy
        x = numpy.random.normal(numpy.min(ar_km),numpy.median(ar_km),250)
        print("Chart 3")
        plt.hist(x, 100)
        plt.show()
          
# Punkte im Diagramm
        print("Chart 4")
        plt.scatter(ar_time, ar_km)
        plt.show()

# Punkte im LinienDiagramm
        print("Chart 5")
        slope, intercept, r, p, std_err = stats.linregress(ar_time, ar_km)

        def myfunc(x):
            return slope * x + intercept

        mymodel = list(map(myfunc, ar_time))

        plt.scatter(ar_time, ar_km)
        plt.plot(ar_time,mymodel)
        plt.legend(["linie","punkte"])
        plt.xlabel('Minuten')
        plt.ylabel('Km')
        plt.show()
        
# damit ich main nicht extra aufrufen muß
if __name__ == "__main__":
  main()
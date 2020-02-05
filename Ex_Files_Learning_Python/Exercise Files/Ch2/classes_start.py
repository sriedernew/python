#
# Example file for working with classes
#
class meinClass():
      def methode1(self):
            print("Meine Class methode 1")

      def methode2(self, einString):
            print("Meine Class methode 2 "+einString)
      
class andereClass(meinClass):
      def methode1(self):
            meinClass.methode1(self)
            print("andere methode 1")

      def methode2(self, einString):
            print("andere methode 2 "+einString)

def main():
  c = meinClass()
  c.methode1()
  c.methode2("Hallo")
  a = andereClass()
  a.methode1()
  a.methode2("Test")
if __name__ == "__main__":
  main()

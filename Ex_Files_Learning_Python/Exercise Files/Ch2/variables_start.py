# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)

# # re-declaring the variable works
f="ffffffffffffffffffffffffff"
print(f)

# # ERROR: variables of different types cannot be combined
print("hallo" +str(123))

# Global vs. local variables in functions
def meinFunktion():
    f="hallo"
    print(f)

meinFunktion()
print (f) 

del f
print(f)



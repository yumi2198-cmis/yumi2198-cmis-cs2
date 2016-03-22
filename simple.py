import math
def pastaadults(x):#this defines the amount of spaghetti needed for the adults
    a = x * 100 #one adult needs about 100g of spaghetti
    return a

def pastakids(y): #this defines the amount of spaghetti needed for the children
    b = y * 60 #one child needs about 60g of spaghetti
    return b 

def sumpasta(a, b): #sum of children and adult spaghetti
    w = a + b
    return w

def output(name, adultpasta, kidpasta, everyone):
    return """
Hello there, {}!
Did you know that you will need this amount of pasta in grams to cook for your people:
{} + {} = {}
""" .format(name, adultpasta, kidpasta, everyone) #adding the number of pasta needed for children and adults.

#defines everything the functions will do 
def main():
    name = raw_input("Hello, what is your name?: ")
    adults = raw_input("Okay. How many adults will be eating your spaghetti?: ")
    kids = raw_input("How many kids will be eating your spaghetti?: ")
    adultpasta = pastaadults(int(adults))
    kidpasta = pastakids(int(kids))
    everyone = sumpasta(float(adultpasta), float(kidpasta))
    print output(name, adultpasta, kidpasta, everyone)
    print "I hope you adults and " + str(kids) + " kids have a great meal!"
main ()

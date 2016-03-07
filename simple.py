import math
def multiply(x):#this defines the amount of spaghetti needed for the adults
    a = x * 100 #one adult needs about 100g of spaghetti
    return a

def bmultiply(y): #this defines the amount of spaghetti needed for the children
    b = y * 60 #one child needs about 60g of spaghetti
    return b 

def add(a, b): #sum of children and adult spaghetti
    w = a + b
    return w

def output(name, a, b, w):
    return """
Hello there, {}!
Did you know that you will need this amount of pasta in grams to cook for your people:
{} + {} = {}
""" .format(name, a, b, w) #adding the number of pasta needed for children and adults.

#defines everything the functions will do 
def main():
    name = raw_input("Hello, what is your name?: ")
    x = raw_input("Okay. How many adults will be eating your spaghetti?: ")
    y = raw_input("How many kids will be eating your spaghetti?: ")
    a = multiply(int(x))
    b = bmultiply(int(y))
    w = add(int(a), int(b))
    print output(name, a, b, w)

main ()

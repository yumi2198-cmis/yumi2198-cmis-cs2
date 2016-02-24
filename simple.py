import math
def multiply(x):
    a = x * 100
    return a

def bmultiply(y):
    b = y * 60
    return b 

def add(a, b):
    w = a + b
    return w

def output(name, a, b, w):
    return """
Hello there, {}!
Did you know that you will need this amount of pasta in grams to cook for your people:
{} + {} = {}
""" .format(name, a, b, w)

def main():
    name = raw_input("Hello, what is your name?: ")
    x = raw_input("Okay. How many adults will be eating your spaghetti?: ")
    y = raw_input("How many kids will be eating your spaghetti?: ")
    a = multiply(int(x))
    b = bmultiply(int(y))
    w = add(int(a), int(b))
    print output(name, a, b, w)

main ()

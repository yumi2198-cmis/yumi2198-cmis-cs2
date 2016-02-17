def multiply(x):
    b = x * 100
    return b

def kmultiply(y):
    k = y * 60
    return k 

def add(z, k):
    r = z + k
    return r

def output(name, b, k, r):
    return """
Hello there, {}!
Did you know that you need this amount of pasta in grams to cook for your people:
{} + {} = {}
""" .format(name, b, k, r)

def main():
    name = raw_input("Hello, what is your name?: ")
    x = raw_input("Okay. How many adults will be eating your spaghetti?: ")
    y = raw_input("How many kids will be eating your spaghetti?: ")
    r = add(int(b), int(k))
    print output(name, b, k, r)

main ()

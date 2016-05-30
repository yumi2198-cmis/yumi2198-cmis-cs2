import random
#Eat at a Korean restaurant with the choices of Kimbab and Soup. If you don't like any, you can leave.

def start(hello):
    if hello == "Hi!":
        print "Hold on for the game!"

def start2(kimchi):
    if kimchi == "I love kimchi":
        print "Great, that's perfect! The game will start now."

def getready(car):
    print "Dinner! Choose something to ride!"
    if car == "Audi":
        print "You chose the Audi."
    elif car == "BMW":
        print "You're bringing your BMW."
    else:
        car == "Toyota"
        print "You're going to dinner in your Toyota."

def pet(namess):
    if namess == "Dog":
        print "You're bringing a dog."
    elif namess == "Cat" or namess == "cat":
        print "You're bringing a cat with you."
    else:
        namess == "Rabbit"
        return "You chose a rabbit."
    
def hunger(decision):
    if decision == "yes":
        print "Amazing! Welcome to the KoreaKorea Restaurant!"
        choice = raw_input("Choose True or False to determine what you will eat: ")
        food(choice)
    else:
        decision =="no"
        print "WHY?"

def food(decision2):
    if decision2 == "True":
        print "We will serve your kimchi right now!."
    else:
        decision2 == "False"
        print "We will serve your soup now!" 
	
		
def drink(drinkoption):
    if drinkoption == "yes":
        print "We will definitely surprise you!"
    else:
        drinkoption == "no"
        print "That's not good."

def drinkchoice(surprise):
    surprise2 = float(surprise * random.random())
    print surprise2
    if surprise2 > random.randint(1, 10):
        print "You got a bottle of water!"
	elif surprise2 < random.randint(1, 10):
		print "You are getting nothing!"
	else: 
        print "You got a soju!"

def output(car, namess):
    return """
You have chosen to wear the {} car and pet {}.
ENjoy your meal!!
""".format(car, namess)

def main():
    hello = raw_input("Type 'Hi!': ")
    start(hello)
    kimchi = raw_input("Type 'I love kimchi': ")
    start2(kimchi)
    print "Dinner! Choose something to ride!"
    car = raw_input("Choose one of these brands to determine your car 'Toyota, BMW, Audi': ")
    getready(car)
    namess = raw_input("Choose one of these animals to determine your pet 'Dog, Cat, Rabbit': ")
    pet(namess)
    decision = raw_input("Are you hungry?: ")
    hunger(decision)
    decision3 = raw_input("Would u like some beverage to drink?: ")
    drink(decision3)
    surprise = int(raw_input("Choose a number between 1 and 10: "))
    drinkchoice(surprise)
    print output(car, namess) 
main()


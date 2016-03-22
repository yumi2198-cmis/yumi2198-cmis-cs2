import math
import random
def subtract(a, b):
	c = a - b
	return c

def correct():
	print "You're correct"

def choose(c, d):
	chosen = random.randint(c, d)

def final(a, b):
	return "I'm thinking of a number from" + str(a) + "to" + str(b)
 
def output(chosen, guess, under):
    return """
The target was {}
Your guess was {}.
That's under by {}.
""" .format(chosen, guess, under) 

def output2(chosen, guess, over):
	return """
The target was {}
Your guess was {}
That's over by {}.
""".format(chosen, guess, over) 

def main():
	num = raw_input("What is the minimum number?: ")
	num2 = raw_input("What is the maximum number?: ")
	chosen = random.randint(int(num), int(num2))
	print final(int(num), int(num2))
	guess = raw_input("What do you think it is?: ")
	if int(guess) == int(chosen):
		correct()
	if int(guess) < int(chosen):
		under = subtract(int(chosen), int(guess))
		print output (chosen, guess, under)
	if int(guess) > int(chosen):
		over = subtract(int(guess), int(chosen))
		print output2 (chosen, guess, over)
		
main ()

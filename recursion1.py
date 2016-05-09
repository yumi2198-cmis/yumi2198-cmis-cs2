import math
import random

def correct():
	print "You're correct"

def choose(c, d):
	chosen = random.randint(c, d)

def final(a, b):
	return "I'm thinking of a number from" + str(a) + "to" + str(b)

def toohigh():
	print "Your number is too high"

def toolow():
	print "Your number is too low" 

def main():
	num = raw_input("What is the minimum number?: ")
	num2 = raw_input("What is the maximum number?: ")
	chosen = random.randint(int(num), int(num2))
	print final(int(num), int(num2))
	def guess ():
		guess = raw_input("Guess a number: ")
		if int(guess) == int(chosen):
			correct()
		else:
			guess()
		
main ()

	
	

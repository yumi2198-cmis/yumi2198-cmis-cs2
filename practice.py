import math
import random

def correct():
	print "You're correct"

def choose(c, d):
	chosen = random.randint(c, d)

def final(a, b):
	return "I'm thinking of a number from " + str(a) + " to " + str(b)

def guess (chosen, time):
	answer = raw_input("Guess a number: ")
	if int(answer) == int(chosen):
		correct()
	if time == 5:
		print "Sorry your chance is gone now. But play again!"
	elif int(answer) < int(chosen):
		print "Number is too low"
		guess(chosen, time+1)
	else:
		print "Number is too high"
		guess(chosen, time+1)

def repeat(
def main():
	num = raw_input("What is the minimum number?: ")
	num2 = raw_input("What is the maximum number?: ")
	chosen = random.randint(int(num), int(num2))
	print final(int(num), int(num2))
	repeat ()
	time = 1
	guess (chosen, time)




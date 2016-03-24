import math
import random

def areacircle(a):
	circle = (a**2)*math.pi
	return circle 

def areatriangle(a):
	triangle = 1/2*a*4
	return triangle

def chosen(a, b):
	choose = random.randint(a, b)
	return choose

def subtract(a, b):
	under = a - b
	return under

def areas(a, b):
	return "The areas of the circle is: " +str(a) + " and the area of the triangle is" + str(b) + "."

def final(a, b):
	print "I've chosen a number between " + str(a) + " and " + str(b) +".This will be the number of radius of your circle and height of your triangle(with a base of 4). Now once I give you the areas of both circle and triangle, you need to guess what the chosen number was" 

def output(chosen, guess, under):
	return"""
Hello! The chosen number for the radius of circle and base of triangle was {}.
Your guess was {}.
You were under {}.
""".format(chosen, guess, under)

def wrongunder(userguess, choose, under):
	return """
You've chosen {} as your guess.
However the chosen number was {}.
This means you're under {} from the right answer.
""".format(userguess, choose, under)

def wrongover(userguess, choose, over):
	return """
You've chosen {} as your guess.
However the chosen number was {}.
This means you're over {} from the right answer.
""".format(userguess, choose, over)

def correct():
	print "You're a genius!"

def main():
	num = raw_input("Choose a number from 1-20: ")
	num1 = raw_input("Choose another one within the same range: ")
	choose = chosen(int(num), int(num1))
	print final(int(num), int(num1))
	circlearea = areacircle(int(choose))
	trianglearea = areatriangle(int(choose)) 
	print areas(int(circlearea), int(trianglearea))
	userguess = raw_input("Now can you guess which number we chose?: ")
	if int(userguess) < int(choose):
		under = subtract(int(choose), int(userguess))
		print wrongunder
	if int(userguess) > int(choose):
		over = subtract(int(userguess), int(choose))
		print wrongover
	if int(userguess) == int(choose):
		correct ()
main()

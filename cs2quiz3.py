#Section 1: Terminology
# 1) What is a recursive function?
# Recursive function is a function that calls itself in the definition.
#
#
# 2) What happens if there is no base case defined in a recursive function?
#
#If there is no base case defined in a recursive function, it means you will get an error message because without a base case, the recursion function will call itself without stopping.
#
# 3) What is the first thing to consider when designing a recursive function?
#
#The first thing to condsider when designing a recursive function is to make sure it has a base case
#
# 4) How do we put data into a function call?
#You define it in the main function with raw_input
# 
# 5) How do we get data out of a function call?
#
#You get data out of a function call by suing the return key
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 1 + function1(2, 5), 1+function1(2,4), 1+function1(2,3), 1+function1(2,2), 1 + function1(2,1), 2
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = 4

#c1 = -2
#c2 =4
#c3 = 45

#d1 =6
#d2 = 8
#d3 =4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.
import math

def average(num):
	num = raw_input("Next: ")
	if num == "":
		return done(num) #base case
	else:
		num = float(num) #recursive case
		if n % 2 == 1:
		return avg(n)
def main():
	num = raw_input("Next: ")
	print "The average of all your odd numbers was " +float(avg) + "."
main()

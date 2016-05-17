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
#a2 = 1 + function1(6, 1), 6
#a3 = -1

#b1 = 2
#b2 = 1 + function2(1, 0), 0
#b3 = 1 + function2(-1, 4), 1+function2(0,0), 0

#c1 = 1+function3(-2,2), function3(-2,1), =1+function3(-2,0), 0
#c2 =4
#c3 = 10+function2(5,4), 9+Function3(5,3), 8+function3(5,2), 7+function(5,1), 6+function3(5,0), 5

#d1 =6
#d2 = 1+function3(3,1,3), 7
#d3 =1-function4(2,2,1), 1-function(1,1,2), 4

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.
import math

def done(num):
	if num % 2 == 1:
		
	print "The average sum of your odd numbers is" 
def series(num):
	if num == "":
		return done(num)
	else:
		series(num)

def main():
	num = raw_input("Next: ")
	series(num)
main()

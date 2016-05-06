import math

#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#q1 a) 2 == 3
#q2 b) a > b and b == c
#q3 c) x == c or a > x
#
#q4 2) What does 'return' do?
# In python programming, return has the job of taking an argument and giving out the result. It basically shows what argument a certain "def" does. 
#
#
#
#3) What are 2 ways indentation is important in python code?
#q5 a) Indentation is important because some values of a definition can go in as a sub value such as using "if:" and then having another indentation provides the identification of the argument belonging in the if section.
#q6 b)When something in your programming goes wrong you can easily go back to where you were struggling to debug. 
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#q7 problem1_a) -36
#q8 problem1_b) -square root of 3
#q9 problem1_c) 0 
#q10 problem1_d) -5
#
#q11 problem2_a)True
#q12 problem2_b)False
#q13 problem2_c)True
#q14 problem2_d)False
#
#q15 problem3_a) 0.3
#q16 problem3_b) 0.5
#q17 problem3_c) 0.5
#q18 problem3_d) 0.5
#
#q19 problem4_a) 7
#q20 problem4_b) 5
#q21 problem4_c) 0.125
#q22 problem4_d) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def choosebiggest(a, b, c):
	if a > b and a > c:
		return a
	if b > a and b > c:
		return b
	if c > a and c > b:
		return c

def samenumbers(a, b, c):
	if a == b and b == c and c == a:
		return False
	else: 
		return True

def main ():
	print "Please type three different numbers in"
	A = float(raw_input("A: "))
	B = float(raw_input("B: "))
 	C = float(raw_input("C: "))
	if samenumbers (A, B, C):
		result = choosebiggest(A, B, C)
		print "The largest number of your three numbers was {}".format(result)
	else:
		print "You did not follow the directions"

main()

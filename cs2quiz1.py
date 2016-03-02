#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# The symble = is used as an assignment operator. It gives value to a variable.
#
#
#2 3pts) Write a technical definition for 'function'
#
#A named sequence of statements that performs a certain operation.
#
#3 1pt) What does the keyword "return" do?
#
#The keyword "return" works like a vending machine; it spits out the definition or the operation you asked for.
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: boolean - True, False
#	2: integer - -21, 0
#	3: floating point - 4.5, 1.0
#	4: string "Hello, there", "Computer", "science"
#	5: tuple ("Yumi", "Seventeen", 2, "Hi")
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#Function definition is a statement that creates a new function, specifying its name, and the statements it executes. Function call is a statement that executes the function, consisting function name followed by an argument list. 
#
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:programmer writes code
#	2:programmer feeds code to interpreter
#	3:interpreter executes lines of code 1 at a time
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math

def diameter(a):
	return math.sqrt(a / (math.pi)) * 2

def total(f, g, h):
	d = f + g + h
	return d 

def output(f, g, h, d):
	return """
Circle	Diameter
c1      {}
c2      {}
c3      {}
TOTALS  {}
""".format(f, g, h, d)

def main():
	a = raw_input("Area of C1: ")
	b = raw_input("Area of C2: ")
	c = raw_input("Area of C3: ")
	f = diameter(int(a))
	g = diameter(int(b))
	h = diameter(int(c))
	d = total(f, g, h)
	print output(f, g, h, d)

main()
	
        

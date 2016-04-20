import math

def average(a, b, c, d, e):
	avrg = ((a + b + c + d + e) /5)
	return avrg

def wrong():
	print "Your value is not valid"

def output(avrg, integerpart, oddeven):
	return """
The average is {}
The integer part of the average is {}
The integer part is {}
""".format(avrg, integerpart, oddeven)

def even():
	print "Even"

def odd():
	print "odd"

def main():
	print "This program will ask you for 5 integer or float values. It will calculate the average of all values from 0 inclusive to 10 exclusive. It will print out wehther the sulting average even or odd"
	n0 = raw_input("n0: ")
	if float(n0) > 10 or float(n0) < 0:
		wrong ()
	n1 = raw_input("n1: ")
	if float(n1) > 10 or float(n1) < 0:
		wrong ()
	n2 = raw_input("n2: ")
	if float(n2) > 10 or float(n2) < 0:
		wrong ()
	n3 = raw_input("n3: ")
	if float(n3) > 10 or float(n3) < 0:
		wrong ()
	n4 = raw_input("n4: ")
	if float(n4) > 10 or float(n4) < 0:
		wrong ()
	avrg = average(float(n0), float(n1), float(n2), float(n3), float(n4))
	integerpart = float(avrg)
	if ((int(avrg)/2)*2) == int(avrg):
		oddeven == even ()
	if int(avrg) != ((int(avrg)/2)*2):
		oddeven == odd ()
	print output(avrg, integerpart, oddeven)

main()

def add(a,b): #define the functions by adding
	return a+b

def sub (x,y):#define the fuctions by subtracting
	return x-y

def mul(e,f):#define the fuctions by multiplying
	return e*f

def div (j,k):#define the fuctions by diving 
	return (j/k)

def hours_from_seconds (a):#define the fuctions to fine number of seconds in an hour
    return a / 3600

import math
def circle_area (a): #define the area of the circle by using math.pi
    return math.pi * (a**2)

def sphere_volume (a): #define the fuctions to find the volume of a sphere
    return 1.33333333333 * 3.14159265359 * (a**3)

def avg_volume (a, b):#define the fuctions to fine the average volume
   
    return (sphere_volume(a) + sphere_volume(b)) /2

def area(a,b,c): #define the fuctions to find the area of a circle
	s= (a+b+c) / 2 
	return (s*(s - a) * (s - b) * (s - c)) ** 0.5


def right_align (word):#this will right align the message
    return (80-len(word))*(" ") + word

def center (word):#this will center the message
    return (40-len(word))*(" ")+word

def msg_box (word): #this will put the message in a box
    return "+" + ((len(word)+4)*"-") + "+" + "\n" + "|" + (2*" ") + (word)+ (2*" ") + "|" + "\n" + "+" + ((len(word)+4)*"-") + "+"

c1= add (3,4)
print c1 
c2= add (5,6)
print c2 
z1= sub (5,3)
print z1
z2= sub (4,8)
print z2
g1= mul (4,4)
print g1
g2= mul (9,4)
print g2
L1= div (2.0,3)
print L1
L2= div (1.0,3)
print L2
I1= hours_from_seconds (86400)
print I1
I2= hours_from_seconds (56900)
print I2
a1= circle_area (5)
print a1
a2= circle_area (9)
print a2
b1= sphere_volume (5)
print b1
b2= sphere_volume (7)
print b2
d1 = avg_volume (10,20)
print d1
d2 = avg_volume (20,21)
print d2
area1= area (3.0,2.0,4.0)
print area1
area2= area (5.0,2.0,5.0)
print area2
e1= right_align ("Waddup")
print e1
e2= right_align ("Hello")
print e2
g1= center ("Hello")
print g1
g2= center ("It's me")
print g2 
h1=  msg_box ("Hello")
print h1
h2=  msg_box ("I love you!")
print h2
k1= msg_box ("I eat cats!")
print k1
k2= msg_box ("I eat dogs!")
print k2
print msg_box (str(c1))
print msg_box (str(c2))
print msg_box (str(z1))
print msg_box (str(z2))
print msg_box (str(g1))
print msg_box (str(g2))
print msg_box (str(L1))
print msg_box (str(L2))
print msg_box (str(I1))
print msg_box (str(I2))
print msg_box (str(a1))
print msg_box (str(a2))
print msg_box (str(b1))
print msg_box (str(b2))
print msg_box (str(d1))
print msg_box (str(d2))
print msg_box (str(area1))
print msg_box (str(area2))
print msg_box (str(e1))
print msg_box (str(e2))
print msg_box (str(g1))
print msg_box (str(g2))
print msg_box (str(h1))
print msg_box (str(h2))
print msg_box (str(k1))
print msg_box (str(k2))

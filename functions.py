import math
def add(a, b):
    return a + b #adds the two variables together
   
add (3, 4)

def sub(a, b):
    return a - b #subtract the second variable from the first variable

add (5,3)

def mul(a, b): 
    return a * b #two values of variable are multiplied together

mul (4, 4)

def div(a, b):
    return a / b #you divide the first variable and the second variable

div (2, 3)

def hours_from_seconds (a): #the variable represents the seconds
    return a * 3600 #to convert the certain given amount of seconds to hours, the variable must be multiplied by 3600

hours_from_seconds (86400)

def circle_area (a): #the variable represents the radius of a circle
    return a ** 2 * math.pi #this equation reprsents that the variable must be squared and multiplied by pi to find the area of a circle
    
circle_area (5)

def sphere_volume (a): #the variable represents the radius of a circle 
    return (4/3)*math.pi*(a**3) #to find a volume of a sphere, you multiplied 4/3 and p with the cubed radius

sphere_volume (5)
 
def avg_volume (a, b): #the two variables show two distinct radius of two different circles
    c = float(a/2)
    d = float(b/2)
    z = float(4/3)
    return(((z)*math.pi*(c**3)) + ((z)*math.pi*(d**3)))#to find the average volume of two spheres, you need to find the volume of sphere 1 with the "a" variable and then the volume of sphere 2. Once done, you add the volumes of two different sphere together and then divide by 2 for the average number.

avg_volume (10, 20)

def area (a, b, c):
    s = (a + b + c) /2
    return (math.sqrt(float((s(s-a)(s-b)(s-c))))

def right_align(a):
    print(" "*80 - len(a))

print right_align("Hello")

def center (term):
    return str ((40-len(term)*" " +term)

print center("Hello")

def msg_box(txt):
    return "+" + ((len(word)+4)*"-") + "+" + "\n" + "|" +  (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"

print msg_box("Hello")
print msg_box("I eat cats!")
a = add(3, 4)
b = sub(5, 3)
c = mul(4, 4)
d = div(2, 3)
e = hours_from_seconds (86400)
f = circle_area(5)
g = sphere_volume(5)
h = avg_volume (10, 20)
i = area(1, 2, 2.5)
j = right_align ("Hello")
k=center ("Hello")

print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(c))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(i))
print msg_box(str(j))
print msg_box(str(k))


def countup(n):
	while n < 100:
		print n 
		n += 1

def countdown(n):
	while n > 0: 
		print n
		n -= 1

def countfrom(x, y):
	while x < y:
		print x
		x += 1 
	while x > y:
		print x 
		x -= 1
	if x == y:
		print y

def addodds(n):
	total = 0
	while n > 0:
		n -= 1
		if n % 2 == 1:
			total += int(n)
	return "Sum: {}".format(total)
			
	
print addodds(5)

def dots(h, k):
	out = " " 
	x = 0
	while x < h:
		out += "."
		x += 1
	

dots(5,10)	

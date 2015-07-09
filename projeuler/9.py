#find the pythagorean triple that sums to 1000
#takes a while, but works!

def ispyth(num1,num2,num3):
	if num1**2 + num2**2 == num3**2:
		return True
	if num2**2 + num3**2 == num1**2:
		return True
	if num1**2 + num3**2 == num2**2:
		return True
	else:
		return False


for x in range(1,1000):
	for y in range(1,1000):
		for z in range(1,1000):
			if x + y + z == 1000:
				if ispyth(x,y,z):
					print x*y*z
					break


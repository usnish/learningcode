def gcd(a,b):
	while b:
		a, b = b, a%b
	return a

value = 1

for x in range(1,21):
	value = value * x/gcd(x,value)

print value





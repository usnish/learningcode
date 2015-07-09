#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
value = 0
for x in range(1,101):
	for y in range(1,101):
		if x != y:
			value += x*y

print value

#explanation: Because the square of the sum is really just a large inner product, 
#this for loop takes that inner product but doesn't add any terms that are found in
#the sum of the squares 